#include<stdio.h>
#include<string.h>
#include<math.h>
#include<map>
#include<vector>
#include<algorithm>
#include<iostream>
using namespace std;
#define maxn 100010
#define LL long long
LL r,tot;
LL cal(LL n)
{
	return n*(n+1)/2;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k;
	int t,cas;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		cin>>r>>tot;
		LL L,R;
		L=1;R=tot;
		LL res=0;
		while(L<=R){
			LL mid=(L+R)/2;
		//	cout<<mid<<endl;
			if(2*mid+2*r-1<=tot/mid){
				res=mid;
				L=mid+1;
			}else R=mid-1;
		}
		printf("Case #%d: ",cas);
		cout<<res<<endl;
	}
	return 0;
}
