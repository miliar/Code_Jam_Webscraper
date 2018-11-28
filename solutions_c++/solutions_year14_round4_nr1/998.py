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

#define INPUTFILE "test.in"
#define OUTPUTFILE "result.out"

using namespace std;

//#pragma warning(disable:4996)


int main()
{
	fstream infile(INPUTFILE, ios::in);
	fstream outfile(OUTPUTFILE, ios::out);
	int caseN, count, N,i,j;
	infile >> caseN;
	count = 1;
	int number[10001];
	int temp[1001];
	int capacity;
	
	while (count <= caseN){
		
		infile >> N >> capacity;
		vector<int> myVec(N);
		for (i = 0; i < N; i++){
			infile >>myVec[i];
		}
		sort(myVec.begin(), myVec.end());
		int left = 0;
		int right = N - 1;
		int ans = 0;
		while (left<right)
		{
			if (myVec[left] + myVec[right] <= capacity){
				left++;
				right--;
			}
			else
				right--;
			ans++;
		}
		if (left == right)
			ans++;

		outfile << "Case #" << count++ << ": " << ans << endl;
	}

	infile.close();
	outfile.close();
	return 0;
}

