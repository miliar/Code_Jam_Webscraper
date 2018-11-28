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
        LL N;
        cin >>N;
        
        if (N != 0) {
            
            LL ans = 0;
            bool seen[10];
            REP(i,10) seen[i] = false;
            
            while (1) {
                ans += N;
                
                LL num = ans;
                while (num) {
                    seen[num % 10] = true;
                    num /= 10;
                }
                
                bool seenall = true;
                REP(i,10) if (!seen[i]) seenall = false;
                
                if (seenall) break;
            }
            
            cout <<"Case #" <<t <<": " <<ans <<endl;
        }
        
        else {
            cout <<"Case #" <<t <<": INSOMNIA" <<endl;
        }
    
    }
    return 0;
}
