#include<iostream>
#include<cstring>

using namespace std;



int main() {
	int T; cin >> T;
	for(int _case = 1; _case <= T; _case++) {
        long x =0, ans =0, n;
        string p;
        cin >> n >> p;
        for(long i=0; i<=n; i++){
            if(x>=i)
                x += p[i] - '0';
            else{
                ans += i-x;
                x = i;
                x += p[i] - '0';
            }
        }
        cout << "Case #" << _case << ':' << ' ' << ans << endl;
	}
	return 0;
}
