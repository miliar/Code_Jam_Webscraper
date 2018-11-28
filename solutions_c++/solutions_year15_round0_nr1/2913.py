#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for (int cases = 1; cases<=T; cases++) {
		int smax;
		cin>>smax;
		string s;
		cin>>s;
		vector <int> a(smax+1);
		for (int i = 0; i<s.size(); i++) {
            a[i] = s[i]-'0';
		}
		int res = 0;
		int cnt = 0;
		int n = s.size();
		for (int i = 0; i<n; i++) {
            if (cnt>=i) {
                cnt += a[i];
            }
            else {
                res += i-cnt;
                cnt = i+a[i];
            }
		}
		cout<<"Case #"<<cases<<": "<<res<<endl;
	}
}
