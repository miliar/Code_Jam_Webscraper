// small test case only 1 & 2 
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<vector>
#include<map>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;
int main()
{
	int ct,t,df[5]={1,4,9,121,484},a,b,cnt;
	freopen("D:\\input.txt","r",stdin);
    freopen("D:\\output.txt","w",stdout);
	scanf("%d",&ct);
/*	int N,a[168],p=1,cnt;
    N=1000;
	a[0]=2;
     int M=(N-1)/2;
     int x=(floor(sqrt(N))-1)/2,i,j;
     vector<bool> S(M+1,0);
     for (i=1;i<=x;i++)
         if (!S[i])
            for (j=2*i*(i+1);j<=M;j+=(2*i+1))
                S[j]=1;
     for (i=1;i<=M;i++)
         if (!S[i]){ a[p]=2*i+1; p++;}
	//for (i=0;i<168;i++) printf("%d\n",a[i]);*/
	for(t=1;t<=ct;t++)
	{
		cnt=0;
		scanf("%d",&a);scanf("%d",&b);
		if(df[0]>=a && b>=df[0]) cnt++;
		if(df[1]>=a && b>=df[1]) cnt++;
		if(df[2]>=a && b>=df[2]) cnt++;
		if(df[3]>=a && b>=df[3]) cnt++;
		if(df[4]>=a && b>=df[4]) cnt++;
		printf("Case #%d: %d\n",t,cnt);
	}
	return 0;
}

