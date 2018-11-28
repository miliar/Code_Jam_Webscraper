#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<cstring>
#include<map>
#include<algorithm>
#include<vector>
#include<stdlib.h>

using namespace std;

#define MEM(v,i) memset(v,i,sizeof(v))

typedef long long int LL;
int count_a = 0, array[10000];

bool is_pal(int square){
	int temp = 0;
	int x = square;
	while(x!= 0){
		temp = temp *10 + x%10;
		x = x/10;
	}
	if(temp == square)
		return true;
	else return false;

}

void preprocess(){
	int n = 1;
	int i = 0;
	MEM(array,0);
	for( i = 1; i<=1000000; i++){
		if(is_pal(i)){
			int square = i*i;
			if(is_pal(square)){
				array[count_a++] = square;
			}
		}
	}
/*
	for(i = 0; i< count_a; i++){
		cout<<array[i]<<endl<<flush;
	}
*/
}

int main(){
	int test = 0, N = 0;
	int A = 0, B = 0;
	scanf("%d",&N);
	preprocess();	
	
	for(test = 1; test<=N; test++){
		scanf("%d %d\n",&A,&B);
		int count_A = 0, count_B = 0;
		int i = 0;
		//int low = 0, high = count_a-1, mid = (high+low)/2;
		for(i = 0; i<count_a && array[i]<=A-1; i++);
		count_A = i-1;
		
		for(i = 0; i<count_a && array[i]<=B; i++);
		count_B = i-1;
		//cout<<count_A<<endl<<count_B<<endl<<flush;
		
		printf("Case #%d: %d\n",test, count_B - count_A);
	}

	return(0);
}
