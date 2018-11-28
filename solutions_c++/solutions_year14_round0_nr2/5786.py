// =====================================================================================
// 
//       Filename:  cookie.cpp
// 
//        Version:  1.0
//        Created:  Saturday 12 April 2014 05:11:03  IST
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
	int t,i,j,k,n=1;
	double cur,c,f,x,time,t1,t2;
	si(t);
	while(t--)
	{
		cur=2.0f;
		time=0.0f;
		scanf("%lf%lf%lf",&c,&f,&x);
		while(1)
		{
			t1=x/cur;
			t2=c/cur + x/(cur+f);
			if(t1<t2)
			{
				time+=t1;
				break;
			}
			else
			{
				time+=c/cur;
				cur+=f;
			}
		}
		printf("Case #%d: %lf\n",n++,time);
	}

}

