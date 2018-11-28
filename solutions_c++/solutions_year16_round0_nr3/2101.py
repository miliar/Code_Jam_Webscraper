#include<stdio.h>
long long int a[510];
int an;
int n,m;
char p[40];
int pl;
void writep(long long int x){
	pl=0;
	while(x!=0){
		p[pl]='0'+x%2;
		pl++;
		x/=2;
	}
	p[pl]=0;
}
long long int readp(){
	long long int x,i;
	x=0;
	for(i=pl-1;i>=0;i--){
		x*=2;
		x+=p[i]-'0';
	}
	return x;
}
int main(){
	int i,j;
	freopen("output.txt","w",stdout);
	scanf("%d%d",&n,&m);
	an=0;
	for(i=(1<<(n/2-1))+1;an<m;i+=2){
		writep(i);
		for(j=pl-1;j>=0;j--){
			p[j*2+1]=p[j];
			p[j*2]=p[j];
		}
		pl*=2;
		a[an]=readp();
		an++;
	}
	printf("Case #1:\n");
	for(i=0;i<m;i++){
		writep(a[i]);
		printf("%s",p);
		for(j=2;j<=10;j++){
			printf(" %d",j+1);
		}
		printf("\n");
	}
}