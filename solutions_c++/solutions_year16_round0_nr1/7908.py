#include<iostream>
#include<cstdio>
#include<algorithm>
#define N 10
using namespace std;
bool bz[N];
int n,sum;
bool jian(int x){
	while (x){
		int y=x%10;
		if (!bz[y]){
			bz[y]=1;
			if ((++sum)==10)return 1;
		}
		x/=10;
	}
	return 0;
}
int main(){
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int k=1;k<=T;k++){
		scanf("%d",&n);
		if (!n){
			printf("Case #%d: INSOMNIA\n",k);
			continue;
		}
		int  x=0;
		for (int i=0;i<10;i++)bz[i]=0;
		sum=0;
		while (!jian(x+=n));
		printf("Case #%d: %d\n",k,x);
	}
	return 0;
}
