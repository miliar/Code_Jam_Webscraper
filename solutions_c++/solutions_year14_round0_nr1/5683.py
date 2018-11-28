/*Mayoor Bishnoi*/

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<list>
#include<map>
#include<queue>
#include<stack>

#define inp(n) scanf("%d",&n);
#define inp2(x,y) scanf("%d%d",&x,&y);
#define inpl(n) scanf("%lld",&n);
#define inpl2(x,y) scanf("%lld%lld",&x,&y);
#define out(n) printf("%d\n",n);
#define outl(n) printf("%lld\n",n);
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORR(i,b,a) for(int i=b-1;i>=a;i--)
#define PB(a) push_back(a)
#define C(x) printf("%d\n",x);

using namespace std;

typedef vector< int > vi;
typedef pair< int,int > pii;
typedef vector< pii > vpii;
typedef list< int > li;
typedef long long ll;
typedef unsigned long long ull;

/*int gcd(int a,int b)
{
	while(b)
		b^=a^=b^=a%=b;
	return a;
}*/

main()
{
	int t,x,y,mat1[4][4],mat2[4][4],n=1;
	inp(t)
	while(t--)
	{
		inp(x)
		FOR(i,0,4)
			FOR(j,0,4)
				inp(mat1[i][j])
		inp(y)
		FOR(i,0,4)
			FOR(j,0,4)
				inp(mat2[i][j])
		int c=0,ans;
		FOR(i,0,4)
			FOR(j,0,4)
			{
				if(mat1[x-1][i] == mat2[y-1][j])
				{
					c++;
					ans=mat1[x-1][i];
				}
			}
		if(c == 1)
			printf("Case #%d: %d\n",n++,ans);
		else if(c == 0)
			printf("Case #%d: Volunteer cheated!\n",n++);
		else
			printf("Case #%d: Bad magician!\n",n++);
	}
	return 0;
}