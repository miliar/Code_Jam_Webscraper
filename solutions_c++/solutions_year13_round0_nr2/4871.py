// next.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "tclass.h"
#include <vector>
#include <string>
#include "Windows.h"

using namespace std;

void printYes(int t) {
	cout << "Case #" << t +1 << ": YES" << std::endl;
}

void printNo(int t) {
	cout << "Case #" << t +1 << ": NO" << std::endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T = 0;
	std::cin >> T;
	for (int t = 0; t < T; ++t) {
		int N = 0;
		int M = 0;
		cin >> N;
		cin >> M;
		int arr[100][100];
		for (int i = 0; i < N; ++i) for (int j = 0; j < M; ++j)
			cin >> arr[i][j];
		
		bool valid = true;

		for (int i = 0; i < N; ++i) {
			int big = arr[i][0];

			for (int j = 0; j < M; ++j) {
				if (arr[i][j] > big)
					big = arr[i][j];
			}

			for (int j = 0; j < M; ++j) {
				if (arr[i][j] < big) {					
					for (int x = 0; x < N; ++x) 
						if (arr[x][j] > arr[i][j]) 
							valid = false;
				}					
			}	

		}

		if (true == valid) {
			for (int i = 0; i < M; ++i) {
				int big = arr[0][i];

				for (int j = 0; j < N; ++j) {
					if (arr[j][i] > big)
						big = arr[j][i];
				}

				for (int j = 0; j < N; ++j) {
					if (arr[j][i] < big) {					
						for (int x = 0; x < M; ++x) 
							if (arr[j][x] > arr[j][i]) 
								valid = false;
					}					
				}	

			}
		}

		if (true == valid)
			printYes(t);
		else
			printNo(t);

	}

}

