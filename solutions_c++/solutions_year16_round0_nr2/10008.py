#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
using namespace std;

void countFilp(int sum, int count, int round){
	int temp;
	unsigned int temp2;
	int num = 0;
	while (sum !=1){
		temp = sum - ((sum >> 1) << 1);
		//count--;
		//sum = sum >> 1;
		if (temp == 1){
			temp2 = sum - ((sum >> count) << count);
			temp2 = ~temp2 & ((1 << count)-1);
			sum = ((sum >> count) << count) + temp2;
			num++;
		}
		sum = sum >> 1;
		count--;
	}

	printf("Case #%d: %d\n", round, num);
	return;
}


int main(void){

	int Test_Case;
	char str[103];
	int sum;
	int count;
	int k = 0;
	//freopen("input.txt", "r", stdin);
	scanf("%d", &Test_Case);
	for (int i = 1; i <= Test_Case; ++i){
		k = 0;
		sum = 1;
		count = 0;
		scanf("%s", &str);
		while (str[k] != '\0'){
			sum = sum << 1;
			if (str[k] == '-')
				sum |= 1;
			k++;
		}

		countFilp(sum, k, i);

	}

	return 0;
}