#include <stdio.h>
int n;
long long m,print,print2;
void pro(){
	long long k=1,save=m;
	int i;
	print=2;
	for(i=1;i<n;i++)
		k<<=1;
	if(k*2==save)
		print=save-1;
	else{
		while(save>k){
			save-=k;
			print<<=1;
			k>>=1;
		}
		print-=2;
	}
	k=1;
	for(i=0;i<n;i++)
		k<<=1;
	print2=1;
	while(m<k){
		print2*=2;
		k>>=1;
	}
	k=1;
	for(i=0;i<n;i++)
		k<<=1;
	print2=k-print2;
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test,testt;
	scanf("%d",&testt);
	for(test=1;test<=testt;test++){
		scanf("%d %lld",&n,&m);
		pro();
		printf("Case #%d: %lld %lld\n",test,print,print2);
	}
	return 0;
}
