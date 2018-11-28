#include <iostream>
#include<algorithm>
#include<fstream>
#include<list>
using namespace std;
struct node{
    char c;
    int x;
};
bool cmp(node a,node b){
    return a.x>b.x;
}
list<char> l;
node no[1001];
int main()
{
    ifstream in;
    ofstream out;
    in.open("E:\\project\\A-large(1).in");
    out.open("E:\\project\\round1-a-large.txt");
    string s;int t,k;
    in>>t;k=0;
    while(t--){
            k++;
        in>>s;
        l.clear();
        int len=s.length();
        l.push_back(s[0]);
        for(int i=1;i<len;i++){
            if(s[i]>=l.front())l.push_front(s[i]);
            else l.push_back(s[i]);
        }
        out<<"Case #"<<k<<": ";
        for(int i=0;i<len;i++){
            out<<l.front();
            l.pop_front();
        }
        out<<endl;
    }
    in.close();
    out.close();
    return 0;
}
