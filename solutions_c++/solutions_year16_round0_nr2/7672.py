#include <iostream>
#include <string.h>
#include <string>
using namespace std;

#define REPS(i,s,n) for(int i=s;i<n;i++)
#define REP(i,n) REPS(i,0,n)
typedef long long LL;

#define max_N 1005

int main() {
    int T;
    cin >>T;
    cin.ignore();
    
    for(int t=1; t<=T; t++) {
        
        LL ans = 0;
        string s;
        
        cin >>s;
        
        REP(i, s.size()-1) {
            if (s[i] != s[i+1]) ans++;
        }
        if (s[s.size()-1] == '-') ans++;
        
        cout <<"Case #" <<t <<": " <<ans <<endl;
    
    }
    return 0;
}
