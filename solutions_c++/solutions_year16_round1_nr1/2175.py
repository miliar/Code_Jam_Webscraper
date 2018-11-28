#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#include<set>
#include<map>
#include<cmath>
#include<cstdlib>
#include<complex>
#include<sstream>
#include<iomanip>

using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
#define For(i,a,b) for(int i=a;i<b;i++)
#define pb(x) push_back(x)
#define ll long long
#define VI vector<int>

int main(){
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	rep(g,t){
		string s;
		cin >> s;

		cout << "Case #" << g+1 << ": ";
		string ans = s.substr(0,1);
		for(int i=1;i<s.length();i++)
			if(s[i] >= ans[0]){
				string tmp = "";
				tmp +=s[i];
				ans = tmp + ans;
			}else
				ans+=s[i];
		cout << ans << endl;
	}
	return 0;
}
