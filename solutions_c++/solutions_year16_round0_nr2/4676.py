#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
using namespace std;

vector<char> str;

void countFilp(int round){
	int count = 0;
	bool check = false;
	for (int i = str.size()-1; i >=0; --i){
		if (str[i] == '-'){
			check = true;
			continue;
		}
		else{
			if (check) count += 2;
			check = false;
		}
			

	}
	if (str[0] == '-')
		count++;

	printf("Case #%d: %d\n", round, count);
	
}


int main(void){

	int Test_Case;
	int count;
	int k = 0;
	char temp[103];
	//freopen("input.txt", "r", stdin);
	scanf("%d", &Test_Case);
	for (int i = 1; i <= Test_Case; ++i){
		k = 0;
		str.clear();
		for (int j = 0; j < 103; j++)
			temp[j] = '0';

		count = 0;
		scanf("%s", &temp);
		while (temp[k] != '\0'){
			str.push_back(temp[k]);
			k++;
		}
		

		countFilp(i);

	}

	return 0;
}