#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <sstream>
#include <iomanip>
using namespace std;

#define FOR(i,x,n) for(int i=x;i<n;++i)
#define RFOR(i,x,n) for(int i=x;i>=n;--i)
#define ST 0.000000001
#define MOD 1000000007
#define pb(a) push_back(a)
#define b() begin()
#define e() end()
#define CLR(a,x) memset(a,x,sizeof(a))
#define sz(x) (int)x.size()
#define MP make_pair
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define LL long long
#define VI vector < int >
#define VUI vector < unsigned int >
#define VLL vector < long long >
#define VD vector < double >
#define PII pair < int , int >
#define INF 2147483647
#define LLINF 9223372036854775807
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define sd(a) scanf("%lf",&a)

double C, F, x, X, r, t, t1, t2;
int T, n;


int main()
{
	//setiosflags(ios::fixed);
	cin>>T;
	FOR(n,1,T+1){
		r = 2.0;
		t = 0;
		x = 0.0;
		cin>>C>>F>>X;
		while(x < X){
			t1 = C/r + (X - x)/(r+F);
			t2 = (X - x)/r;
			if(t2 <= t1){
				t += t2;
				x = X;
			}
			else{
				t += C/r;
				r += F;
			}
		}
		cout<<"Case #"<<n<<": ";
		cout<<fixed<<setprecision(7)<<t;
		cout<<endl;
	}
	return 0;
}
