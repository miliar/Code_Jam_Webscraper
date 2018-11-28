#include <iostream>
#include <cstdio>
#include <cstdio>

using namespace std;

int pancake[1200];

int calculate(int now){
	int time=0;
	time+=now;
	int ss[1200];
	for(int q=0;q<=1000;q++) ss[q] = pancake[q];
	for(int z=1000;z>now;z--){
		if(ss[z]>0){
			ss[z-now] += ss[z];
			ss[now] +=ss[z];
			time += ss[z];
			ss[z]=0;
		}
	}
	return time;
}





int main(int argc, char** argv) {
	freopen("zzz.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas=1;;
	scanf("%d",&t);
	while(t--){
		int number;	
		scanf("%d",&number);	
		int z;
		for(int s=0;s<1100;s++)  pancake[s] = 0;
			
		for(int s=0;s<number;s++){
				scanf("%d",&z);
				pancake[z]++;
		}
		
		int min = 50000;
		int k;
		for(int q=1;q<=1000;q++){
			if(min>calculate(q)) {
			min = calculate(q);
			k = q;
			}
		}
		
		
		printf("Case #%d: %d\n",cas,min);
		cas++;
		
	}
}
