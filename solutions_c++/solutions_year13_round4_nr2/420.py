#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<vector>

using namespace::std;

int ca;
__int64 n,p,la1,la2,k,n2,m;
__int64 d[1005];
__int64 d1[1005];

void input(){
	int i;
	scanf("%I64d %I64d",&n,&p);
	n2=1;
	k=0;
	for(i=1;i<=n;i++)
		n2*=2;
	la2=n2;
	if(p==n2)
		la1=p-1,la2=p-1;
	else{
	m=0;
	while(p>k){
		n2/=2;
		k+=n2;
		++m;
	}
	la1=d[m]-1;
	m=0;
	n2=la2;
	while(p<n2){
		n2/=2;
		++m;
	}
	la2-=d1[m+1];
	}
}

void process(){
	int i;
	d[1]=1;
	for(i=2;i<=51;++i){
		d[i]=d[i-1]*2;
		if((d[i]+1)/2==d[i-1])
			d[i]++;
	}
	d1[1]=1;
	for(i=2;i<=51;++i){
		d1[i]=d1[i-1]*2;
		if((d1[i]-1)/2==d1[i-1])
			d1[i]--;
	}
}

void output(){
	printf("Case #%d: %I64d %I64d\n",ca,la1,la2);
}

int main(){
	int i,t;
	freopen("B-large.in","rt",stdin);
	freopen("output.txt","wt", stdout);
		process();
	scanf("%d",&t);
	while(t--){
		la1=la2=0;
		ca++;
		input();
		output();
	}
	return 0;
}