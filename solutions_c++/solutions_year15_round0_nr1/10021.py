#include<stdio.h>


using namespace std;

int main(){
	int T, Sm, i, j, shy[1002], total, fri;
	char S[1002];

	scanf("%d", &T);
	for(i=0;i<T;i++){
		total = 0;
		fri = 0;

		scanf("%d%s", &Sm, &S);
		for(j=0;j<Sm+1;j++){
			shy[j] = (int)S[j] - 48;	//shy_level = j の人数
		}

		for(j=0;j<Sm+1;j++){
			if(total < j){
				fri += j - total;
				total += j - total;
			}
			total += shy[j];
		}

		printf("Case #%d: %d\n", i+1, fri);
	}

	return 0;
}
