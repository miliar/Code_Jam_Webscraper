#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>

using namespace std;


bool nums[10];


void adddig(int n){
	
	nums[n%10] = 1;
	while (n /= 10){
		nums[n%10] = 1;
	}
	
}


int main(){
	int c;
	scanf("%d",&c);
	int N,j;
	int sol;
	bool listo;
	for (int i = 1; i <= c; i++){
		memset(nums,0,sizeof(nums));
		scanf("%d",&N);

		if (N == 0){
			printf("Case #%d: INSOMNIA\n",i);
			continue;
		}

		listo = false;
		j = 1;
		sol  = N;
		while (j < 1000000000 and !listo){
			sol = N *j;
//			cout << sol << endl;
			adddig(sol);
			listo = true;
			for (int k = 0; k < 10; k++){
				if (nums[k] == 0){
					listo = false;
				}
			}


			j++;
		}

		printf("Case #%d: %d\n",i,sol);
	}

}