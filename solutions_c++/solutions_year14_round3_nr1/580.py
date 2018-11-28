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

LL gcd ( LL a, LL b )
{
  if ( a==0 ) return b;
  return gcd ( b%a, a );
}

LL P,Q;
int T;
int main()
{
	cin>>T;
	char inp[50], *num;
	vector <LL> pow2;
	pow2.pb(1);
	FOR(i,1,42)
		pow2.pb(pow2[i-1]*2);
	FOR(t,1,T+1){
		cin>>inp;
		num = strtok(inp,"/ \n");
		P = atol(num);
		num = strtok(NULL,"/ \n");
		Q = atol(num);

		LL g = gcd(P,Q);
		P /= g;
		Q /= g;
		bool present = false;
		FOR(i,0,pow2.size()){
			if(pow2[i]==Q){
				present = true;
				break;
			}
			if(pow2[i]>Q)
				break;
		}
		if(!present){
			cout<<"Case #"<<t<<": impossible"<<endl;
			continue;
		}
		int turns = 0;
		while(Q!=1){
			turns++;
			Q/=2;
			if(P>Q)
				break;
			//cout<<"p/q = "<<P<<"/"<<Q<<endl; 
			
		}
		cout<<"Case #"<<t<<": "<<turns<<endl;
	}
	return 0;
}
