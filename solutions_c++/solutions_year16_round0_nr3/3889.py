#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <fstream>
#include <stdio.h>
using namespace std;


vector<int> baseNum[501];
long long int roundNum[501];

FILE *fp = fopen("output.txt", "w");


//e가 카운드 i가 베이스
long long int mult(int i, int e){

	long long int temp = 1;
	for (int j = 0; j < e; j++){
		temp *= i;

	}

	return temp;
}

//Is this sosu
int isNotPrime(long long int num){

	for (int i = 2; i*i < 10000; i++){
		if ((num%i) == 0){
			return i;
		}
	}
	return -1;
}


long long int changeBase(long long int num, int base){

	long long int result = 0;
	long long int temp;
	int count = 0;

	while (num!=0){

		temp = num - ((num >> 1) << 1);
		if (temp == 1)
			result += mult(base, count);
		count++;

		num = num >> 1;
	}
	printf("return\n");
	return result;
}

long long int change(long long int num, int round){
	
	long long int temp = num;
	int result;

	//1~9진법으로 바꾸고 검사한다
	for (int i = 2; i <= 10; i++){
		temp = changeBase(num, i);
		result = isNotPrime(temp);
		if (result < 0)
			break;
		baseNum[round].push_back(result);
	}

	if (result == -1){
		baseNum[round].clear();
		return -1;
	}
		
	return temp;
}


void produceJam(int len, int ct){

	long long int first = (1 << (len-1)) +1 ;
	int round = 0;
	long long int result;
	int lent;
	long long int temp = first;
	while (ct--){
		result = change(temp,round);
		//printf("%lld\n", result);
		if (result < 0){
			ct++;
			temp += 2;
			//printf("%d\n",temp);
			continue;
		}
		else
			roundNum[round] = changeBase(result,2);
		round++;
		temp += 2;
	}
	

	//프린트
	printf("Case #1:\n");

	for (int i = 0; i < round; i++){
		printf("%lld ", roundNum[i]);
		fprintf(fp, "%lld ", roundNum[i]);
		lent = baseNum[i].size();
		for (int j = 0; j < lent; ++j){
			printf("%d ", baseNum[i][j]);
			fprintf(fp, "%d ", baseNum[i][j]);
		}
		fprintf(fp, "\n");
		printf("\n");
	}

}


int main(void){




	int Test_Case;
	int len, count;
	//freopen("input.txt", "r", stdin);
	scanf("%d", &Test_Case);
	for (int i = 1; i <= Test_Case; ++i){
		scanf("%d%d", &len, &count);
		produceJam(len, count);

		
	}

	//fclose(fp);
	

	return 0;
}