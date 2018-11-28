#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<cstdio>
#include<cassert>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<vector>
#include<ctime>

using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b)  ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))

#define MP make_pair
#define pb push_back
#define inf  1000000000
#define maxn 1000005
#define maxc 100001
#define MP make_pair

typedef long long LL;
typedef pair<int,int> pi;
typedef pair<pi,pi> pii;
//typedef __int64 LL;

int files[100005];
int f[100005];
int cnt[706];

int main()
{
	int i,j,k,tests,cs=0,K,n,x;

	//freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);
	scanf("%d",&tests);

	while(tests--)
	{
	   cin>>n>>x;
	   multiset<pi> S;
	   MEM(cnt,0);
	   for(i=0;i<n;i++)
	   {
	       cin>>files[i];
	       cnt[files[i]]++;
	   }


      //sort(files,files+n);
      int ans=0;

      for(i=x;i>=1;i--)
      {
         int rem = x-i;
         if(cnt[i]==0) continue;


       //  printf("%d %d\n",i,cnt[i]);
         for(j=rem;j>=1;j--)
         {
            int use = MIN(cnt[j],cnt[i]);
            if(j==i)
            {

               ans+= cnt[i]/2;
               cnt[i]%=2;
            }
            else
            {
               ans+=use;
               cnt[j]-=use;
               cnt[i]-=use;
            }

            if(cnt[i]==0) break;
         }
         ans+=cnt[i];
         cnt[i]=0;
      }

		printf("Case #%d: %d\n",++cs,ans);
	}

	return 0;
}
