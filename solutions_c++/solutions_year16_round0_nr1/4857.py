#include<bits/stdc++.h>
using namespace std;
int a[11];

void split(int x)
{
	while(x){
		a[x%10]=1;
		x/=10;
	}
}

void fuck()
{
	int i,n,x;
	memset(a,0,sizeof(a));
	scanf("%d",&n);
	if(n==0){
		printf("INSOMNIA\n");
		return;
	}
	for(i=n;i;i+=n){
		split(i);
		if(accumulate(a,a+10,0)==10) break;
	}
	printf("%d\n",i);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
   int i,t;
   scanf("%d",&t);
   for(i=1;i<=t;i++){
	   printf("Case #%d: ",i);
	   fuck();
   }
 return 0;
}

