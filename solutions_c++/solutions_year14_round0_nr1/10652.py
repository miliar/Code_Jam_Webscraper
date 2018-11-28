#include <iostream>
#include <map>
#include <list>
#include <algorithm>

using namespace std;


int readNum(){
    int t;
    cin >> t;
    return (int) t;
}

int main(){
   
    int t = readNum();
    for(int i=1;i<=t;i++){
        list<int> p;
        list<int> r;
        int q1 = readNum();
        int n;
        for(int j=1;j<=4;j++){
            for(int k=1;k<=4;k++){
                cin >> n;  
                if(j==q1){
                    p.push_back(n);
                }
            }
        }
        int q2 = readNum();
        for(int j=1;j<=4;j++){
            for(int k=1;k<=4;k++){
                cin >> n;  
                if(j==q2){
                    if (find(p.begin(), p.end(), n) != p.end()) {
                        r.push_back(n);
                    }
                }
            }
        }
        cout << "Case #" << i << ": ";
        if(r.size() == 1){
            cout << r.back() << endl;
        } else if (r.size() > 1){
            cout << "Bad magician!" << endl;
        } else {
            cout << "Volunteer cheated!" << endl;
        }
        p.empty();
        r.empty();
    }
}
