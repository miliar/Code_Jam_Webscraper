#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);i++)

int main(){
	int T;
    cin >> T;
    REP(t,T){
        cout << "Case #" << t+1 << ": ";
        int n,res=0,crr=0;
        string ad;
        cin >> n >> ad;
        REP(i,n+1){
            int s=ad[i]-'0';
            if(s==0) continue;
            res+=max(i-crr,0);
            crr+=s+max(i-crr,0);
        }
        cout << res << endl;
    }
	return 0;
}

