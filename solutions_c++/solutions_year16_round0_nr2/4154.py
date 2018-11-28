#include<stdio.h>
#include<vector>
#include<string>
#include<stdlib.h>
#include<queue>
using namespace std;

int cal(vector<int> arr){

	int flag = 0;
	int rate = 1;
	for (int i = 0; i < arr.size(); i++){
		if (arr[i] == 1){
			flag += rate;
		}
		rate *= 2;
	}	

	return flag;
}


int main(){


	FILE *pFile = fopen("B-large.txt", "r");
	FILE *oFile = fopen("B-large-output.txt", "w");
	int testcase;
	fscanf(pFile, "%d", &testcase);

	for (int temp = 1; temp <= testcase; temp++){

		char input_str[101];
		fscanf(pFile, "%s", input_str);

		string input = input_str;
		
		vector<int> arr;
		arr.resize(input.size(), 0);

		for (int i = 0; i < input.size(); i++){ 
			if (input[i] == '+'){
				arr[i] = 1;
			}
		}


		int start = arr[0];
		int count = 0;
		
		for (int i = 0; i < arr.size(); i++){
			if (arr[i] != start){
				start = 1 - start;
				count++;
			}
		}
		if (start == 0){
			count++;
		}
		fprintf(oFile, "Case #%d: %d\n", temp, count);
	}
}
