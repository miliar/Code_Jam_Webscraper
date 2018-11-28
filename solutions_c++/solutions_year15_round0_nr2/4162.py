#include <stdio.h>
#include <vector>

using namespace std;

int main(){
	int T;
	scanf("%i",&T);
	for(int i = 1; i <= T; i++){
		int P,max = 0,best,ind,ops=0;
		scanf("%i",&P);
		vector<int> pan(P);
		for(int j = 0; j < P; j++){
			scanf("%i",&pan[j]);
			if(pan[j]>max){
				max = pan[j];
				ind = j;
			}
		}
		best = max;
		while(true){
			if(max==9){
				int c9=0,c5=0;
				for(int j = 0; j < (P+ops); j++){
					if(pan[j]==9)
						c9++;
					if(pan[j]==5)
						c5++;
				}
				if(c5==0 && c9==1){
					pan.push_back(3);
					pan[ind] = 6;
					ops++;
				}
				else{
					pan.push_back(pan[ind]-pan[ind]/2);
					pan[ind] = pan[ind]/2;
					ops++;
				}
			}
			else{
				pan.push_back(pan[ind]-pan[ind]/2);
				pan[ind] = pan[ind]/2;
				ops++;
			}
			max=0;
			for(int j = 0; j < (P+ops); j++){
				if(pan[j]>max){
					max = pan[j];
					ind = j;
				}
			}
			if((max+ops)<best){
				best = max+ops;
			}
			if(max==1){
				break;
			}
		}
		printf("Case #%i: %i\n",i,best);
	}
	return 0;
}