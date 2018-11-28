#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<utility>
#include<cstring>
#include<cmath>
#define LL long long int
#define mod 1000000007
#define vi vector<int>
#define vvi vector < vi >
#define pii pair<int,int>
#define all(c) c.begin(),c.end()
#define sf(x) scanf("%d",&x);
#define sf2(x,y) scanf("%d%d",&x,&y);
#define mem(a,val) memset(a,val,sizeof(a))
#define nl printf("\n");
#define pb push_back
#define mp make_pair
#define f first
#define s second
using namespace std;
int rec(int arr[],int cnt)
{	int mx,i,b[2005],x,y;
	mx=arr[cnt];
	//printf("val %d\n",mx);
	if(mx<=3) return mx;
	for(i=1;i<=cnt;i++) b[i]=arr[i]-1;
	x=mx/2;y=(mx+1)/2;
	if(mx==9){x=3;y=6;}
	arr[cnt]=x;arr[cnt+1]=y;
	sort(arr+1,arr+cnt+2);
	return 1+min(rec(b,cnt),rec(arr,cnt+1));
}
int main()
{	freopen("googleinput.txt","r",stdin);
    freopen("googleoutput.txt","w",stdout);
	int tst,t,i,j,d,arr[2005],ans;
	sf(t);
	for(tst=1;tst<=t;tst++)
	{	sf(d);
		for(i=1;i<=d;i++)sf(arr[i]);
		sort(arr+1,arr+d+1);
		ans=rec(arr,d);
		printf("Case #%d: %d\n",tst,ans);
	}
		return 0;
}


