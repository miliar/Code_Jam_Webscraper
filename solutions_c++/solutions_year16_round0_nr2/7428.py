	#include<vector>
	#include<iostream>
	#include<stdio.h>
	#include<bitset>
	#include<algorithm>
	#include<functional>
	#include<numeric>
	#include<utility>
	#include<sstream>
	#include<iostream>
	#include<iomanip>
	#include<cstdio>
	#include<cmath>
	#include<math.h>
	#include<cstdlib>
	#include<ctime>
	#include<cstring>
	#include<climits>
	#include<sstream>
	#include<string.h>
	#include<set>
	#include<map>
	#include<utility>
	#include<stack>
	#include<queue>
	#include<deque>
	#include<list>
	#include<bitset>

	#define ll long long
	#define FL(i,a,b) for(ll i=a;i<b;i++)
	#define FOR(i,n) for(ll i=0;i<n;i++)
	#define SORTF(x) sort(x.begin(),x.end(),func);
	#define SORT(x) sort(x.begin(),x.end())
	#define pb(x) push_back(x)
	#define SET(v, val) memset(v, val, sizeof(v)) ;
	#define RSORT(v) { SORT(v) ; REVERSE(v) ; }
	#define ALL(v) v.begin(),v.end()
	#define REVERSE(v) { reverse(ALL(v)) ; }
	#define UNIQUE(v) unique((v).begin(), (v).end())
	#define RUNIQUE(v) { SORT(v) ; (v).resize(UNIQUE(v) - (v).begin()) ; }
	#define fill(x,n) memset(x,n,sizeof(x))
	#define sl(x) scanf("%lld",&x)
	#define mp make_pair
	#define mod 1000000007

	#include <iostream>
using namespace std;

int main() {
	ll t;
	cin >> t;
	ll count = 1;
	while(t--) {
		string s;
		cin >> s;
		ll ans = 0;
		string s1 = s;
		cout << "Case #" << count << ": ";

		while(true) {
			int l = s1.length();
			string s1="";
			int c;
			for(c=l-1;c>=0;c--) {
				if(s[c] == '-')
					break;
			}

			FOR(j,c+1) s1+=s[j];

			int f1 = 1;
			FOR(i,c+1) {
				if(s1[i] == '-') {
					f1=0;
					break;
				}
			}
			if(f1){
				cout << ans << endl;
				count++;
				break;
			}

			if(s1[0] == '+') {
				for(int i=0;i<c+1;i++) {
					if(s[i] == '+') s[i] = '-';
					else s[i] = '+';
				}
				ans++;
			}
			else {
				for(int i=0;i<c+1;i++) {
					if(s[i] == '+') s[i] = '-';
					else s[i] = '+';
				}
				string s2 = "";
				for(int i=c;i>=0;i--) {
					s2 += s1[i];
				}
				s1 = s2;
				ans++;
			}
		}

	}



	return 0;
}