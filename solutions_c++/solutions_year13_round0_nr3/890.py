#include <set>
#include <cmath>
#include <stack>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#define pi acos(-1)
#define INF 0x7fffffff
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrvec(x,siz) for(int xx=0;x<=siz;xx++)  x[xx].clear();
#define fop   freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
long long  num[1011]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,
	4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004ll,
	404090404ll,10000200001ll,10221412201ll,12102420121ll,12345654321ll,40000800004ll,1000002000001ll,
	1002003002001ll,1004006004001ll,1020304030201ll,1022325232201ll,1024348434201ll,1210024200121ll,
	1212225222121ll,1214428244121ll,1232346432321ll,1234567654321ll,4000008000004ll,4004009004004ll};
int main()
{
    int t,cas=0;
    fop;
    scanf("%d",&t);
    while(t--)
    {
    	long long L,R;
    	int cnt=0;
    	scanf("%I64d %I64d",&L,&R);
    	for(int i=0;num[i]!=0;i++)
    		if(num[i]>=L&&num[i]<=R)
    			  cnt++;
    	printf("Case #%d: %d\n",++cas,cnt);
    }
}
