#include "stdafx.h"

#include <cstdio>
#include <iostream>
#include <fstream>
#include <iomanip>
#include<vector>
#include<stack>
#include<queue>
#include<cstring>
#include<string>
#include<map>

#define INPUTFILE "B-large (2).in"
#define OUTPUTFILE "result.out"

using namespace std;

//#pragma warning(disable:4996)

int minSwap(int *number,int N,int maxpos)
{
	int i, j, ans;
	ans = 0;
	for (i = maxpos - 1; i >= 0; i--){
		for (j = 0; j < i; j++){
			if (number[j] > number[j + 1]){
				number[j] = number[j] ^ number[j + 1];
				number[j + 1] = number[j] ^ number[j + 1];
				number[j] = number[j] ^ number[j + 1];
				ans++;
			}
		}
	}
	for (i = maxpos + 1; i < N; i++){
		for (j = N - 1; j > i; j--){
			if (number[j] > number[j - 1]){
				number[j] = number[j] ^ number[j - 1];
				number[j - 1] = number[j] ^ number[j - 1];
				number[j] = number[j] ^ number[j - 1];
				ans++;
			}
		}
	}
	return ans;
}

int main()
{
	fstream infile(INPUTFILE, ios::in);
	fstream outfile(OUTPUTFILE, ios::out);
	int caseN, count, N,i,j;
	infile >> caseN;
	count = 1;
	int number[1001];
	int temp[1001];
	
	while (count <= caseN){
		/*infile >> N;
		int maxpos = -1;
		int maxnum = 0;
		for (i = 0; i < N; i++){
			infile >> number[i];
			if (number[i]>maxnum){
				maxnum = number[i];
				maxpos = i;
			}
		}
		int ans = 0;
		int minans = -1;
		int pos = 0;
		for (pos = 0; pos <= maxpos; pos++){
			memcpy(temp, number, sizeof(int)*N);
			for (i = maxpos; i > pos; i--){
				temp[i] = temp[i] ^ temp[i - 1];
				temp[i - 1] = temp[i] ^ temp[i - 1];
				temp[i] = temp[i] ^ temp[i - 1];
			}
			ans = minSwap(temp, N, pos);
			if (minans == -1 || minans > (ans + (maxpos - pos)))
				minans = ans + (maxpos - pos);
		}
		for (pos = maxpos+1; pos < N; pos++){
			memcpy(temp, number, sizeof(int)*N);
			for (i = maxpos; i < pos; i++){
				temp[i] = temp[i] ^ temp[i + 1];
				temp[i + 1] = temp[i] ^ temp[i + 1];
				temp[i] = temp[i] ^ temp[i + 1];
			}
			ans = minSwap(temp, N, pos);
			if (minans == -1 || minans > (ans + (pos-maxpos)))
				minans = ans + (pos-maxpos);
		}*/

		infile >> N;
		map<int, int> myMap;
		map<int, int>::iterator itor;
		for (i = 0; i < N; i++){
			infile >> number[i];
			myMap.insert(make_pair(number[i], i));
		}
		int minans = 0;
		int step = 0;
		int large = 0;
		for (itor = myMap.begin(); itor != myMap.end(); ++itor){
			step++;
			large = 0;
			for (i = 0; i < itor->second; i++){
				if (number[i]>itor->first)
					large++;
			}
			minans += (large > (N - step - large)) ? (N - step - large) : large;
		}
		outfile << "Case #" << count++ << ": " << minans << endl;
	}

	infile.close();
	outfile.close();
	return 0;
}

