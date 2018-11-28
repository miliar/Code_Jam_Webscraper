#include<bits/stdc++.h>
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
{
	int tst,t,i,j,d,arr[3005],ans;
	scanf("%d",&t);
	for(tst=1;tst<=t;tst++)
	{	scanf("%d",&d);
		for(i=1;i<=d;i++)
		scanf("%d",&arr[i]);
		sort(arr+1,arr+d+1);
		//printf("tst %d",tst);
		ans=rec(arr,d);
		//printf("tst %d",tst);
		printf("Case #%d: %d\n",tst,ans);
	}
		return 0;
}