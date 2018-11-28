#include <bits/stdc++.h>
#define X first
#define Y second
#define PI pair<int,int>
#define SIZ 51001001
using namespace std;
long long arr[SIZ];
long long poww[11][18];
vector <long long> V;
long long ans[12];
long long a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z;
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf(" %I64d",&t);
	//PREPROC
	for(i=1;i<SIZ;i++)arr[i]=i;
	for(i=2;i<SIZ;i++){
		if(arr[i]){
			V.push_back(i);
			for(j=i+i;j<SIZ;j+=i)arr[j]=0;
		}
	}
	for(i=1;i<=10;i++){
		poww[i][0]=1;
		for(j=1;j<=15;j++){
			poww[i][j]=poww[i][j-1]*i;
		}
	}
	// REAL COMP
	for(l=1;l<=t;l++){
		printf("Case #%I64d:\n",l);
		scanf(" %I64d %I64d",&n,&z);
		for(i=0;i<(1LL<<(n-2));i++){
			for(j=2;j<=10;j++){
				s=poww[j][0]+poww[j][n-1];
				for(k=0;k<n-2;k++)s+=(((1<<k)&i)!=0)*poww[j][k+1];
				for(k=0;k<V.size();k++){
					if(V[k]>=s)continue;
					if(s%V[k]==0){
						ans[j]=V[k];
						break;
					}
				}
				if(k==V.size())break;
			}
			if(j==11){
				printf("1");
				for(k=n-3;k>=0;k--)printf("%d",((1<<k)&i)!=0);
				printf("1");
				for(k=2;k<=10;k++)printf(" %I64d",ans[k]);
				printf("\n");
				z--;
			}
			if(z==0)break;
		}
	}
	return 0;
}