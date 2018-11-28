#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);i++)

int main(){
	int T;
    cin >> T;
    REP(t,T){
        cout << "Case #" << t+1 << ": ";
        int n;
        cin >> n;
        vector<int> a(n);
        REP(i,n) cin >> a[i];
        int y=0,z=0;
        for(int i=1;i<n;i++){
            if(a[i]<a[i-1]) y+=(a[i-1]-a[i]);
        }
        double rate=0;
        for(int i=1;i<n;i++){
            if(a[i]<a[i-1]){
                int m=a[i-1]-a[i];
                rate=max(rate,m/10.0);
            }
        }
        for(int i=1;i<n;i++){
            z+=min((int)(10*rate),a[i-1]);
        }
        cout << y << " " << z << endl;
    }
	return 0;
}

