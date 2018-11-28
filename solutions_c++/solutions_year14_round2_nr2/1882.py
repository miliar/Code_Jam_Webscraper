#include<cstdio>

void f(){
	int a,b,k;
	scanf("%d%d%d",&a,&b,&k);
	int l=0;
	for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
			if((i&j)<k)l++;
	printf("%d\n",l);
}

int main(){
	int a;
	scanf("%d",&a);
	for(int i=1;i<=a;i++){
		printf("Case #%d: ",i);
		f();
	}
}
