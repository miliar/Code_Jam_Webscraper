#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<vector>

using namespace::std;

int ca,n;
int a[2005];
int b[2005];
int la[2005];
int ch[2005];

int r[2005][2005];
int bo1[2005];

int d1[2005];
int d2[2005];

void input(){
	int i;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
		scanf("%d",&a[i]);
	for(i=1;i<=n;i++)
		scanf("%d",&b[i]);
}

void process(){
	int i,j,o;
	for(i=1;i<=n;i++)
		for(j=1;j<=n;j++)
			r[i][j]=0,bo1[i]=0,ch[i]=0;
	ch[n+1]=0;
	for(i=2;i<=n;i++)
		for(j=1;j<i;j++)
			if(a[i]<=a[j])
				r[j][i]=1,bo1[j]++;;
	for(i=n-1;i>=1;i--)
		for(j=i+1;j<=n;j++)
			if(b[i]<=b[j])
				r[j][i]=1,bo1[j]++;
}
void output(){
	int i;
	printf("Case #%d:",ca);
	for(i=1;i<=n;i++)
		printf(" %d",la[i]);
	printf(" \n");
}
void pro(int le){
	int i,j,o;
	if(le==n+1){
	//	printf("hi\n");
		o=0;
		for(i=0;i<=n+1;i++)
			d1[i]=d2[i]=0;
		for(i=1;i<=n;i++){
			d1[i]=1;
			for(j=1;j<i;j++)
				if(la[i]>la[j] && d1[i]<d1[j]+1)
					d1[i]=d1[j]+1;
			if(d1[i]!=a[i])
				o++;
		}
		for(i=n;i>=1;i--){
			d2[i]=1;
			for(j=i+1;j<=n;j++)
				if(la[i]>la[j] && d2[i]<d2[j]+1)
					d2[i]=d2[j]+1;
			if(d2[i]!=b[i])
				o++;
		}
		if(o==0){
			output();
			ch[n+1]=1;
	//		exit(1);
		}
		return;
	}
	if(ch[n+1]==1)
		return;
	o=0;
	for(i=1;i<=n;i++)
		if(bo1[i]==0 && ch[i]==0){
			o=i;
			la[o]=le;
			ch[o]=1;
	//printf("hi\n");
			for(j=1;j<=n;j++)
				bo1[j]-=r[j][o];
			pro(le+1);
			for(j=1;j<=n;j++)
				bo1[j]+=r[j][o];
			ch[o]=0;
		}
	if(o==0)
		return;
}


int main(){
	int i,t;
//	freopen("input.txt","rt",stdin);
	freopen("C-small-attempt1.in","rt",stdin);
	freopen("output.txt","wt", stdout);
	scanf("%d",&t);
	while(t--){
		ca++;
		input();
		process();
		pro(1);
	}
	return 0;
}