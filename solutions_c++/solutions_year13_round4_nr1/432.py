#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<vector>

#define MO 1000002013

using namespace::std;

int ca;
__int64 la,n,m,p1,p2;
__int64 a[5][100005];
__int64 pr[100005];

void input(){
	int i;
	scanf("%I64d %I64d",&n,&m);
	p1=0,p2=0;
	for(i=1;i<=m;i++){
		scanf("%I64d %I64d %I64d",&a[1][i],&a[2][i],&a[3][i]);
		pr[i]=(a[2][i]-a[1][i])*n-((a[2][i]-a[1][i])*(a[2][i]-a[1][i]-1))/2;
		pr[i]%=MO;
		p1+=pr[i]*a[3][i];
		p1%=MO;
	}
}

void process(){
	__int64 i,j,m1=m,i1,i2=m;
	__int64 mi;
	for(i1=1;i1<=i2;i1++){
		if(i1!=1 && m==m1)
			break;
		m=m1;
	for(i=1;i<=m;i++)
	{
		for(j=i+1;j<=m;j++)
		{
			if(a[1][i]<a[1][j] && a[2][i]<a[2][j] && a[2][i]>=a[1][j]){
				mi=a[3][i];
				if(mi>a[3][j])
					mi=a[3][j];
				a[3][i]-=mi;
				a[3][j]-=mi;
				if(mi!=0){
				a[1][++m1]=a[1][i],a[2][m1]=a[2][j],a[3][m1]=mi;
				a[1][++m1]=a[1][j],a[2][m1]=a[2][i],a[3][m1]=mi;
				}
			}
			else if(a[1][i]>a[1][j] && a[2][i]>a[2][j] && a[2][j]>=a[1][i]){
				mi=a[3][i];
				if(mi>a[3][j])
					mi=a[3][j];
				a[3][i]-=mi;
				a[3][j]-=mi;
				if(mi!=0){
				a[1][++m1]=a[1][j],a[2][m1]=a[2][i],a[3][m1]=mi;
				a[1][++m1]=a[1][i],a[2][m1]=a[2][j],a[3][m1]=mi;
				}
			}
		}
	}
	}
	m=m1;
	for(i=1;i<=m;i++){
		pr[i]=(a[2][i]-a[1][i])*n-((a[2][i]-a[1][i])*(a[2][i]-a[1][i]-1))/2;
		pr[i]%=MO;
		p2+=pr[i]*a[3][i];
		p2%=MO;
	}
	la=(p1-p2)%MO;
	if(la<0)
		la+=MO;
}

void output(){
	printf("Case #%d: %I64d\n",ca,la);
}

int main(){
	int i,t;
	freopen("A-small-attempt1.in","rt",stdin);
	freopen("output.txt","wt", stdout);
	scanf("%d",&t);
	while(t--){
		la=0;
		ca++;
		input();
		process();
		output();
	}
	return 0;
}