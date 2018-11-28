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

int N,T,X, a[10005];	

int main()
{
	cin>>T;
	FOR(t,1,T+1){
		cin>>N>>X;
		FOR(i,0,N){
			cin>>a[i];
		}
		sort(a,a+N);
		int front=0, back=N-1;
		int ans=N;
		while(front<back){
			if(a[front] + a[back] <= X){
				--ans;
				++front;
				--back;
			}
			else
				--back;
		}

		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
