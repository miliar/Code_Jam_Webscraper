#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <ctime>
#include<cassert>

using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef pair<int,int> pi;
typedef pair<int,pi> pii;

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000
#define   M 1000000007

#define maxn 1000000
#define maxt 100000
#define M 1000002013
typedef long long LL;


LL COST(LL x,LL n)
{
   LL ret= ((x*n)%M - x*(x-1)/2)%M;
   if(ret<0) ret+=M;
   return ret;
}

int main()
{
	int i,j,k,tests,m,n,cs=0;


	//gen();return 0;

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);


	scanf("%d",&tests);


	while(tests--)
	{
	   cin>>n>>m;
	   vector<int> A;

	   map<int,LL> S,T;
	   vector<pii> all;

      LL cost=0;

	   for(i=0;i<m;i++)
		{
		   int a,b,p;
		   cin>>a>>b>>p;
		   if(T.find(b)==T.end()) T[b]=0;
		   A.pb(a); A.pb(b);
		   T[b]+=p;
		   LL cc=COST(b-a,n);
		   cc=(cc*p)%M;
		   //cout<<cc<<endl;
		   cost=(cost+cc)%M;
		   all.pb(MP(p,MP(a,b)));
		}

		sort(A.begin(),A.end());

      LL ans=0;

		for(i=0;i<A.size();i++)
		{
		   if(i && A[i]==A[i-1]) continue;
         int a=A[i];

         for(j=0;j<all.size();j++)
            if(all[j].second.first==a)
               {
                  int x=all[j].second.first;
                  if(S.find(x)==S.end()) S[x]=0;
                  //printf("**%d %d\n",x,all[j].first);
                  S[x]+= all[j].first;
               }

         LL cnt=T[a];

         for(j=i;j>=0 && cnt>0;j--)
         {
            LL c=S[A[j]];
            LL tot = MIN(c,cnt);
            //printf("%d %d %I64d %I64d %I64d\n",a,A[j],c,tot,cnt);
            cnt-=tot;
            S[A[j]]-=tot;
            LL cc = COST(A[i]-A[j],n);
            cc=(cc*tot)%M;
            ans=(ans+cc)%M;
         }
		}
      //printf("%I64d %I64d\n",cost,ans);
		ans=(cost-ans)%M;
		if(ans<0) ans+=M;

      printf("Case #%d: %I64d\n",++cs,ans);

	}
	return 0;
}
