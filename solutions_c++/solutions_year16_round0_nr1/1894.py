#include <cstdio>
#include <stdlib.h>
#include <algorithm>

using namespace std;
const int maxn = 10000010;
char a[maxn];
int ver[10];
int main(){
	int t;
	scanf("%d",&t);
	long long mx=0;
	for(int i=0;i<t;i++){
		for(int j=0;j<10;j++)ver[j]=0;
		long long n;
		scanf("%lld",&n);
		if(n==0)printf("Case #%d: INSOMNIA\n",i+1);
		else{
			int u=1;

			while(1){
				long long at=n*u;
				int j=0;
				while(at>0){
					a[j]=at%10+'0';
					at/=10;
					j++;
				}
				a[j]='\0';
				j=0;
				while(a[j]!='\0'){
					//printf("%c\n",a[j]);
					ver[a[j]-'0']=1;
					j++;
				}
				int ok=1;
				for(int k=0;k<10;k++){
					if(ver[k]==0)ok=0;
				}
				if(ok)break;
				u++;
			}
			printf("Case #%d: %lld\n",i+1,n*u);
		}
	}

}