#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <bitset>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#define lli long long int
#define ii pair<int,int>
#define mp make_pair
#define mod 1000000007
#define inf 999999999

using namespace std;

inline void inp(int &n ) {//fast input function
	n=0;
	int ch=getchar_unlocked(),sign=1;
	while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getchar_unlocked();}
	while( ch >= '0' && ch <= '9' )
		n=(n<<3)+(n<<1)+ ch-'0', ch=getchar_unlocked();
	n=n*sign;
}

int t,n,ans;

string s;

int main() {
	// freopen("inp", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	inp(t);

	for(int a=1;a<=t;a++) {
		inp(n);
		cin>>s;

		ans=0;
		int val=0;

		for(int i=0;i<=n;i++) {
			if(i<=val) {
				val+=s[i]-'0';
			}
			else {
				ans+=(i-val);
				val=i+s[i]-'0';
			}
		}

		printf("Case #%d: %d\n",a,ans);
	}




	return 0;
}