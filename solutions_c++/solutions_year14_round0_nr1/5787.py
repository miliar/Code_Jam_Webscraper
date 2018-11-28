// =====================================================================================
// 
//       Filename:  magic.cpp
// 
//        Version:  1.0
//        Created:  Saturday 12 April 2014 04:59:42  IST
//       Revision:  none
//       Compiler:  g++
// 
//         Author:  Aniruddh Kanojia (Samfisher), aniruddhkanojia94@gmail.com
//        Company:  
// 
// =====================================================================================
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<list>
#include<vector>
#include<map>
#include<set>
#include<deque>
#define pl(x) printf("%lld",x)
#define pls(x) printf("%lld ",x)
#define pln(x) printf("%lld\n",x)
#define pi(x) printf("%d",x)
#define pis(x) printf("%d ",x)
#define pin(x) printf("%d\n",x)
#define ps(x) printf("%s",x)
#define pss(x) printf("%s ",x)
#define psn(x) printf("%s\n",x)
#define pc(x) printf("%c",x)
#define pcs(x) printf("%c ",x)
#define pcn(x) printf("%c\n",x)
#define ll long long int
#define vii  vector<int>::iterator 
#define vli  vector<ll>::iterator 
#define vi  vector<int> 
#define vl  vector<ll> 
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define ss(x) scanf("%s",&x)
#define sc(x) scanf("%c",&x)
#define s2i(x,y) scanf("%d%d",&x,&y)
#define s3i(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define s2l(x,y) scanf("%lld%lld",&x,&y)
#define s3l(x,y,z) scanf("%lld%lld%lld",&x,&y,&z)
#define pb(x) push_back(x)
#define pf(x) push_front(x)
#define mp(x,y) make_pair<int,int>(x,y)
#define REP(i,a,b) for(i=a;i<=b;i++)
#define gc  getchar
#define dbg(x,y) printf("%s %d\n",x,y)
#define MOD 1000000007
using namespace std;
int main()
{
	int t,i,j,k,n,cnt,q=1;
	si(t);
	int A[4][4]={0},B[4][4]={0},a,b,c,C[4]={0};
	while(t--)
	{
		
		cnt=0;
		si(a);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				si(A[i][j]);
			}
		}
		for(j=0;j<4;j++)
			C[j]=A[a-1][j];
		si(b);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				si(A[i][j]);
			}
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(C[i]==A[b-1][j])
				{
					cnt++;
					c=C[i];
				}
			}
		}
		printf("Case #%d: ",q);
		if(cnt==0)
			printf("Volunteer cheated!\n");
		else if(cnt==1)
			printf("%d\n",c);
		else
			printf("Bad magician!\n");
		q++;
	}

}

