#include<stdio.h>
#include<algorithm>
using namespace std;
int c[11000];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		int a,b;
		scanf("%d%d",&a,&b);
		for(int i=0;i<a;i++){
			scanf("%d",c+i);
		}
		std::sort(c,c+a);
		int ret=0;
		int rem=a;
		while(rem){
			ret++;
			for(int i=0;i<a;i++){
				if(~c[i]){
					
					rem--;
					for(int j=a-1;j>=0;j--){
						if(i!=j&&~c[j]&&c[i]+c[j]<=b){
							c[j]=-1;
							rem--;
							break;
						}
					}
					c[i]=-1;
					break;
				}
			}
		}
		printf("Case #%d: %d\n",t+1,ret);
	}
}