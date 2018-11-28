/*
*
* solved by Ahmed Kamal
*/
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<cstring>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<bitset>
#include<queue>
#include<utility>
#include<algorithm>
#include<functional>

using namespace std;

typedef long long int LL ;
#define vi vector<int>
#define ii pair<int,int>
#define vii vector< pair<int,int> >
#define sc(x) scanf("%d",&x)
double const EPS = 2.22045e-016;
#define INF (1<<29)

#define ALL(v)				((v).begin()), ((v).end())
#define SZ(v)				((int)((v).size()))
#define CLR(v, d)			memset(v, d, sizeof(v))
#define LOOP(i, n)		for(int i=0;i<(int)(n);++i)

#define PB	push_back
typedef vector<double>    VD;
typedef vector<string>    VS;
LL gcd(LL a, LL b) { return (b == 0 ? a : gcd(b, a % b)); }

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

int ts;sc(ts);
LOOP(t,ts){
	LL p,q;
	scanf("%lld/%lld",&p,&q);
	LL b = gcd (q,p);
	p/=b;
	q/=b;
	if( q & (q-1) ){
		printf("Case #%d: impossible\n",t+1);
		continue;
	}
   if(p==1 && q==1){
    printf("Case #%d: 0\n",t+1);
	continue;
}

	LL g=1;
	while((float(p)/float(q)) < 0.5){
      g++;
      p*=2;
	}
	if(g < 40)
	   printf("Case #%d: %lld\n",t+1,g);
	else
		printf("Case #%d: impossible\n",t+1);

}
return 0;
}
