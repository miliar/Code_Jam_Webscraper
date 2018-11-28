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
	int t,n;
	cin >> t;
	rep(g,t){
		string s;
		cin >> s;
		n = s.length();
		char c = '+';
		int cnt = 0;
		for(int i = n-1;i>=0;i--)
			if(s[i] != c){
				cnt++;
				c = s[i];
			}
		cout << "Case #" << g+1 << ": " << cnt << endl;
	}
	return 0;
}
