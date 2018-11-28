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

int t;
double c,f,x;
double ans,val,val1,val2;

int main() {
	// B-large.in
	// freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-large.in","r",stdin);
	freopen("out.txt", "w", stdout);

	inp(t);

	for(int a=1;a<=t;a++) {
		cin>>c>>f>>x;

		ans=x/2.0;
		val=0;
		val1=2.0;

		while(1) {
			val+=c/val1;
			val1+=f;

			val2=x/val1+val;

			// cout<<" "<<val2<<" "<<val1<<endl;
			if(val2>ans)
				break;
			else
				ans=val2;
		}
		printf("Case #%d: %.7f\n", a,ans);
	}


	return 0;
}