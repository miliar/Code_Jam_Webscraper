// for small test case
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
	int t,n,a,b,i,j,k,flag,p[101][101],q[101][101],cnt1,cnt2,cnt3,cnt4;
	freopen("D:\\input.txt","r",stdin);
	freopen("D:\\output.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&a,&b);
		for(i=0;i<a;i++) for(j=0;j<b;j++)scanf("%d",&p[i][j]);
		for(i=0;i<a;i++) for(j=0;j<b;j++) q[i][j]=2;
		for(i=0;i<a;i++){
			for(j=0;j<b;j++){
				cnt1=0; cnt2=0; flag=0;
				if(p[i][j]==1){
					for(k=0;k<a;k++) cnt1+=p[k][j];
					for(k=0;k<b;k++) cnt2+=p[i][k];	
					//printf("..%d..%d..\n",cnt1,cnt2);
					if(cnt1==a || cnt2==b) {flag=45; // goto l;
					}
					else {flag=85; goto l;
					}
					}
		}	
	}l:
	if(flag==85 ) printf("Case #%d: NO\n",100-t);
	else printf("Case #%d: YES\n",100-t);
}
	return 0;
}

