#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define sz size()
#define pii pair<int,int>
#define mp make_pair
#define ff first
#define ss second
#define all(v) (v).begin(),(v).end()

int k;
string s;

int f()
{
	int ans=0;
	bool flag = 1;

	for(int i = 0;i < s.sz;i++){

		if(s[i] == '-'){

			if(i+k <= s.sz){

				for(int j = 0;j < k;j++)s[i+j] = ( (s[i+j] == '-') ? '+' : '-');

				ans++;
			}
			else {

				flag = 0;
				break;
			}
		}
	}
	if(!flag)return 1e8;
	return ans;
}

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	//std::ios_base::sync_with_stdio(false);

	int t;
	string a;

	cin >> t;

	for(int cases =1;cases <= t;cases++){

		cin >> a >> k;

		s = a;

		int ans = f();
		s = a;
		reverse(all(s));
		ans = min(ans,f());

		if(ans == 1e8)cout << "Case #" << cases << ": " << "IMPOSSIBLE" << endl;
		else cout << "Case #" << cases << ": " << ans << endl;
	}
	return 0;
}