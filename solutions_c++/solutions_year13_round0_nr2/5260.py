#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iomanip>
#include <list>

using namespace std;
#define deb(a) cout<<#a<<":"<<a<<endl;

int main() {
    int T;
    cin>>T;
    
    for(int t=1; t<=T; t++) {
        int n,m;
        int g[105][105] = {0};
        cin>>n>>m;
        
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                cin>>g[i][j];
            }
        }
        
        string res = "YES";
        bool fail1, fail2;
        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {

                fail1 = 0;
                fail2 = 0;

                for(int a=0; a<m; a++) {
                    if(g[i][a] > g[i][j]) {
                        fail1 = 1;
                        break;
                    }
                }
                
                for(int a=0; a<n; a++) {
                    if(g[a][j] > g[i][j]) {
                        fail2 = 1;
                        break;
                    }
                }
                
                if(fail1 && fail2) {break;}
            }
            
            if(fail1 && fail2) {
                res = "NO";
                break;
            }
        }
        
        cout<<"Case #"<<t<<": "<<res<<endl;
    }
    return 0;
}