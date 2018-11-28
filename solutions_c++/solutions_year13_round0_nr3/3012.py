#include<stdio.h>
#include<string.h>
#include<math.h>
#define ll long long
#define MAX 105

ll a,b,n;

int cs(int u){
	int a[MAX];
	int al=0,i;
	while(u){
		a[al++]=u%10;
		u/=10;
	}
	int f=1;
	for(i=0;i<al/2;i++)
		if(a[i]!=a[al-i-1]){
			f=0;
			break;
		}
	return f;
}

void check(int x){
	int k=sqrt(x);
	if(k*k!=x)return;
	if(cs(k)&&cs(x))n++;
}

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int t,ti=1;
	scanf("%d",&t);
	while(t--){
		n=0;
		int i;
		scanf("%d %d",&a,&b);
		for(i=a;i<=b;i++)
			check(i);
		printf("Case #%d: %d\n",ti++,n);
	}
	return 0;
}