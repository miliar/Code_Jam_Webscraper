#include <iostream>
#include <cstdio>
using namespace std;

int P[1005];

int bruteForceSearch(int max){
	//Assuming same splits for same values:
	int bestSplitSolution = max;
	for (int i = max; i >0; --i){
		if(P[i]==0) continue;
		bestSplitSolution = i;
		//Find the best Split for this i.
		for (int j = 1; j <= i/2; ++j){
			//This split is j,(i-j)
			P[j]=P[i]+P[j];
			P[i-j]=P[i]+P[i-j];
			int temp = bruteForceSearch(i-1);
			if(temp+P[i]<bestSplitSolution) bestSplitSolution=temp+P[i];
			P[j]=P[j]-P[i];
			P[i-j]=P[i-j]-P[i];
		}
		return bestSplitSolution;
	}
	return 0;
}

int main(){
	int T,D,casenumber=0,temp,max;

	scanf("%d",&T);
	while(T--){
		casenumber++;
		scanf("%d",&D);
		memset(P,0,sizeof(P));
		max=0;		//Max P value.
		for (int i = 0; i < D; ++i){
			scanf("%d",&temp);
			P[temp]++;
			if(temp>max) max = temp;
		}
		int answer = bruteForceSearch(max);
		printf("Case #%d: %d\n",casenumber,answer);
	}
}