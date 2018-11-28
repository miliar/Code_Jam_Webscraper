#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<iostream>
#include<math.h>


using namespace std;

int main(void){

	int T,N;
	scanf("%d",&T);

	for(int i=0; i<T; i++){
		scanf("%d",&N);
		int sheep=0;
		//do N have 1?
		if(N==0){
			printf("Case #%d: INSOMNIA\n",i+1);
			continue;
		}
		int sol= N;
		
		while(true){
			int bound = sol;
			int temp = sol;
			vector<int> number;

			number.push_back(temp%10);
			while((temp/=10)!=0){
				number.push_back(temp%10);
			}

			for(int j=0; j<number.size(); j++){
				sheep|=1<<number[j];
			}
			if(sheep==1023)
				break;

			sol+=N;
			number.clear();
		}
		printf("Case #%d: %d\n",i+1,sol);
	}

	return 0;
}
