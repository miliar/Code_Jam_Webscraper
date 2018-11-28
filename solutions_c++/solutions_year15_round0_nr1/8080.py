#include <bits/stdc++.h>

using namespace std;

#define rep(i,a,b) for(int i = a;i < b;i++)

int main()
{
	int T,n;
	cin >> T;
	rep(t,0,T) {
		cin >> n;
		string val;
		cin >> val;
		long long int answer = 0,num_up = 0;
		long long int vals[n + 1];
		rep(i,0,n + 1) {
			vals[i] = val[i] - '0';
			if(i == 0) {
				num_up = vals[i];
			}
			else if(vals[i] != 0) {
				if(num_up >= i) {
					num_up += vals[i];
				}
				else {
					answer += (i - num_up);
					num_up += (i - num_up);
					num_up += vals[i];
				}
			}
		}
		cout << "Case #" << t + 1 << ": " << answer << endl;
	}
	return 0;
}