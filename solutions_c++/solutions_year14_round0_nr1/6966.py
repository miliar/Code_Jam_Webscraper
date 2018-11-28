#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		int kt1,kt2,v1[4][4],v2[4][4],x;
		scanf("%d",&kt1); kt1--;
		int kolo=0,kt=-1;
		bool je[17]; for(int i=0;i<17;i++) je[i]=false;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&x);
				if(kt1==i)je[x]=true;
			}
		}
		scanf("%d",&kt2); kt2--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&x);
				if(kt2==i) if(je[x]){kolo++; kt=x;}
			}
		}

		printf("Case #%d: ",t+1);
		if(kolo==1) printf("%d\n",kt);
		if(kolo>1) printf("Bad magician!\n");
		if(kolo<1) printf("Volunteer cheated!\n");

	}
	return 0;
}
