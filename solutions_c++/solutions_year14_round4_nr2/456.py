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

int arr[1005];

int main()
{
	int i,j,k,tests,cs=0,K,n;

	//freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
	freopen("B-large.in","r",stdin); freopen("B-large.out","w",stdout);
	scanf("%d",&tests);

	while(tests--)
	{
	   scanf("%d",&n);
	   vector<int> tmp;
	   for(i=0;i<n;i++) cin>>arr[i],tmp.pb(arr[i]);
	   sort(tmp.begin(),tmp.end());

	   int l=0,r=n-1,ans=0;

	   for(i=0;i<tmp.size();i++)
	   {
	      int v=tmp[i];
         //printf("%d\n",v);
	      for(j=l;j<=r;j++)
            if(v==arr[j]) break;

         int p=j;
        // printf("%d %d\n",v,j);
         if(j-l < r-j)
         {
            ans+=(j-l);
            for(k=j;k>l;k--) arr[k]=arr[k-1];
           // puts("j");
            arr[l]=v;
            l++;
         }
         else
         {
            ans+=(r-j);
            for(k=j;k<r;k++) arr[k]=arr[k+1];
            arr[r]=v;
            r--;
         }
	   }



		printf("Case #%d: %d\n",++cs,ans);
	}

	return 0;
}
