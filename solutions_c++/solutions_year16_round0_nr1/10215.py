//printf("Case #%d: ",i+1);
#include <stdio.h>
#include <iostream>
#include <fstream>
//#include "problem_a.h"
#include <string.h>
using namespace std;

int ccnt(int arr[]){
	int result = 1;
	for (int i = 0; i < 10; i++){
		result *= arr[i];
		if (result == 0) return 0;
	}
	return 1;
}

int main(void){
	fstream fs;
	fs.open("result_aa.txt", ios::out | ios::binary);
	int t; cin >> t;
	int	N, num, r=2, rec=1;
	int store =0;
	int arr[10], output[105]={0,};
	char number[10];

	int cnt = 0;
	for (int i = 1; i <= t; i++){
		int digit[10] = {0,};
		num = cnt =0; r= 2;
		cin >> N; num = N;
		

		if(N == 0) {
			output[rec++] = -1;
			fs << "Case #"<< i << ": " << "INSOMNIA" << endl;
			continue;
		}
		do{
			while (num != 0){ // ÀÚ¸®¼ö
				++cnt;digit[num%10]=1;
				num /= 10;
				if(cnt == 7 && num == 1) {output[rec++] = -1; continue;}
			}
			if(ccnt(digit) == 1){	
				output[rec++] = store;
				break;
			}
			store = num = N*r; r++;
			cnt = 0;
		}while(1);

		if(output[i] != -1)
			fs << "Case #"<< i << ": " << output[i] << endl;
		else
			fs << "Case #"<< i << ": " << "INSOMNIA" << endl;
			
	}
}