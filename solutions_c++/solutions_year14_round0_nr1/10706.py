#include <iostream>
#include <cstdio>

using namespace std;

int main() {

	int T,r1,r2,k=1;
	scanf("%d",&T);
	while(T--){

		scanf("%d",&r1);
		int c1[16],c2[16];

		for (int i = 0; i < 16; ++i) {
			scanf("%d",&c1[i]);
		}

		scanf("%d",&r2);
		for (int i = 0; i < 16; ++i) {
			scanf("%d", &c2[i]);
		}

		int oc=0,pos=-1;

		for(int i=4*(r1-1);i < 4*r1;i++){
			for (int j = 4*(r2-1); j < 4*r2; ++j) {
				if(c1[i]==c2[j]){
					oc++;pos=i;
				}
			}
		}

		printf("Case #%d: ",k++);
		if(oc>1)
			printf("Bad magician!\n");
		else{
			if(oc==0)
				printf("Volunteer cheated!\n");
			else
				printf("%d\n",c1[pos]);
		}

	}

	return 0;
}
