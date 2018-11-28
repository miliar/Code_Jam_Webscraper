#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	int x=1;
	while(x<=t){
		int smax;
		scanf("%d",&smax);
		char ip[smax+1];
		scanf("%s",ip);
		int noStanding = 0;
		int need = 0;
		for(int i=0;i<=smax;i++){
			int a = ip[i]-'0';
			if(noStanding>=i){
				noStanding += a;
			}else{
				int diff = i - noStanding;
				need += diff;
				noStanding +=a+diff;
			}
		}
		printf("Case #%d: %d\n",x,need);
		x++;
	}

	return 0;
}
