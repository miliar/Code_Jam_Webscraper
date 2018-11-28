#include<bits/stdc++.h>
using namespace std;
int b[100],n,c;
long long ans[100];

long long factor(long long x)
{
	long long i;
	double s=sqrt(1.0*x);
	for(i=2;i<=s;i++)
		if(x%i==0) return i;
	return 0;
}

void tran(long long x)
{
	int pos=2;
	memset(b,0,sizeof(b));
	b[1]=b[n]=1;
	while(x){
		b[pos++]=x%2;
		x=x/2;
	}
}

void fuck()
{
	long long i,num,tmp;
	int cnt,j,k,C=0,p;
	bool f;
	scanf("%d%d",&n,&c);
	p=(1ll<<(n-1));
	for(i=0;i<p;i++){
		tran(i);
		f=1;cnt=1;
		for(k=2;k<=10;k++){
			num=0;
			for(j=n;j>=1;j--) num=num*k+b[j];
			tmp=factor(num);
			if(!tmp) {f=0;break;}
			else ans[cnt++]=tmp;
		}
		if(f){
			for(j=n;j>=1;j--)
				printf("%d",b[j]);
			for(j=1;j<10;j++)
				printf(" %d",ans[j]);
			C++;puts("");
		}
		if(C==c) break;
	}
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int i,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d:\n",i);
		fuck();
	}
 return 0;
}
