#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <iomanip>
#include <queue>
#include <iterator>
#include <fstream>
#include <cmath>
using namespace std;


int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
#define cin in
#define cout out


    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++) {
        cout<<"Case #"<<cas<<": ";


        string s;
        cin>>s;
        int n;
        cin>>n;
        int res = 0;
        bool nop = false;
        for(int c=0;c<s.size();c++) {
            if(s[c]=='-') {
                if(c+n<=s.size()){
                    res++;
                    for(int c2=0;c2<n;c2++) {
                        s[c+c2] = (s[c+c2]=='-'?'+':'-');
                    }
                } else {
                    nop = true;
                }
            }
        }

        if(nop) {
            cout<<"IMPOSSIBLE"<<endl;
        } else {
            cout<<res<<endl;
        }
    }

}
