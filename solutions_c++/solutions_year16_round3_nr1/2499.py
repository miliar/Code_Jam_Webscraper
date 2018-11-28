
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>

using namespace std;
struct Node {
    int num;
    char party;
    
    friend bool operator< (Node n1, Node n2)
    {
        if (n1.num < n2.num)
            return n1.num<n2.num;
        else if (n1.num == n2.num) {
            return n1.party>n2.party;
        }
        return false;
    }
    
};

//bool cmp(Node a,Node b) {
//    return a.num<b.num;
//}

int main(int argc, const char * argv[]) {
    ofstream ofs;
    ifstream ifs;
    ofs.open("/Users/dengjc/Desktop/A-small.out");
    ifs.open("/Users/dengjc/Desktop/A-small-attempt0.in");
    if (!ofs.is_open()||!ifs.is_open()) {
        cout<<"打开文件出错"<<endl;
        return 1;
    }
    
    int T;
    ifs>>T;
//    cin>>T;
    
    for (int i=1; i<=T; i++) {
        ofs<<"Case #"<<i<<": ";
        int N;
        ifs>>N;
        int total = 0;
        priority_queue<Node> pr;
        map<int,char> mp;
        char P = 'A';
        for (int j=0; j<N; j++) {
            Node tmp;
            ifs>>tmp.num;
            total+=tmp.num;
            tmp.party = P++;
            pr.push(tmp);
        }
        while (!pr.empty()) {
            Node large1 = pr.top();
            pr.pop();
            
            Node next = pr.top();
            
            if (large1.num>=2) {
                if (next.num/(double)(total-2) <= 0.5) {
                    large1.num -= 2;
                    if (large1.num>0) {
                        pr.push(large1);
                    }
                    ofs<<large1.party<<large1.party;
                    total -= 2;
                } else {
                    pr.pop();
                    large1.num -= 1;
                    next.num -= 1;
                    if (large1.num>0) {
                        pr.push(large1);
                    }
                    if (next.num>0) {
                        pr.push(next);
                    }
                    ofs<<large1.party<<next.party;
                    total -= 2;
                }
            } else if(large1.num == 1){
                ofs<<large1.party;
                if (next.num/(double)(total-1) > 0.5) {
                    pr.pop();
                    ofs<<next.party;
                    next.num -= 1;
                    if (next.num>0) {
                        pr.push(next);
                    }
                    total -= 1;
                }
                total -= 1;
            } else {
                
            }
            
            ofs<<" ";
            
        }
//    ofs<<"Case #"<<i<<": "<<result<<endl;
        ofs<<endl;
    }
    
    
}


