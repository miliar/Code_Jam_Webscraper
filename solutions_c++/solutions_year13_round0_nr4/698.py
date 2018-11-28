// PD.cpp : main project file.

#include "stdafx.h"
#include <string>
#include <iostream>
#include <conio.h>

using namespace System;
using namespace std;

#define KEYS_LEN 201

bool allClosedAccessible(int* availKeys, int chestsLen, bool* openedChests, int* chestsTypes, int* chestsKeysLen, int** chestsKeys)
{
	for(int i = 0; i < chestsLen; i++) {
		if(!openedChests[i] && availKeys[chestsTypes[i]] == 0) {
			bool flag = false;

			for(int j = 0; !flag && j < chestsLen; j++) {
				if(i != j && !openedChests[j]) {
					for(int k = 0; !flag && k < chestsKeysLen[j]; k++) {
						if(chestsKeys[j][k] == chestsTypes[i]) {
							flag = true;
						}
					}
				}
			}

			if(!flag) {
				return false;
			}
		}
	}
	return true;
}

bool solve(int* availKeys, int chestsLen, bool* openedChests, int* chestsTypes, int* chestsKeysLen, int** chestsKeys, int depth, int* solution)
{
	if(depth == chestsLen) {
		return true;
	}
	
	if(!allClosedAccessible(availKeys, chestsLen, openedChests, chestsTypes, chestsKeysLen, chestsKeys)) {
		return false;
	}

	for(int i = 0; i < chestsLen; i++) {
		if(!openedChests[i] && availKeys[chestsTypes[i]] > 0) {
			openedChests[i] = true;
			availKeys[chestsTypes[i]]--;

			for(int j = 0; j < chestsKeysLen[i]; j++) {
				availKeys[chestsKeys[i][j]]++;
			}
			
			solution[depth] = i;
			if(solve(availKeys, chestsLen, openedChests, chestsTypes, chestsKeysLen, chestsKeys, depth + 1, solution)) {
				return true;
			}

			for(int j = 0; j < chestsKeysLen[i]; j++) {
				availKeys[chestsKeys[i][j]]--;
			}
			
			availKeys[chestsTypes[i]]++;
			openedChests[i] = false;
		}
	}

	return false;
}

bool precheck(int* precheckKeys, int chestsLen, int* chestsTypes)
{
	for(int i = 0; i < chestsLen; i++) {
		precheckKeys[chestsTypes[i]]--;
	}

	for(int i = 0; i < KEYS_LEN; i++) {
		if(precheckKeys[i] < 0) {
			return false;
		}
	}

	return true;
}

int main(array<System::String ^> ^args)
{
	freopen("C:\\Users\\Shay\\Documents\\Visual Studio 2010\\CodeJam2013\\QualificationRound\\PD\\io\\input.txt", "r", stdin);
	freopen("C:\\Users\\Shay\\Documents\\Visual Studio 2010\\CodeJam2013\\QualificationRound\\PD\\io\\output.txt", "w", stdout);

	int T;
	
	cin >> T;

	for(int c = 1; c <= T; c++) {
		int K, N;
		
		cin >> K;
		cin >> N;

		int* availKeys = new int[KEYS_LEN];
		bool* openedChests = new bool[N];
		int* chestsTypes = new int[N];
		int* chestsKeysLen = new int[N];
		int** chestsKeys = new int*[N];
		
		int* precheckKeys = new int[KEYS_LEN];
		
		for(int i = 0; i < 201; i++) {
			availKeys[i] = 0;
			precheckKeys[i] = 0;
		}
		for(int i = 0; i < K; i++) {
			int t;
			cin >> t;
			availKeys[t]++;
			precheckKeys[t]++;
		}

		for(int i = 0; i < N; i++) {
			openedChests[i] = false;
			cin >> chestsTypes[i];
			cin >> chestsKeysLen[i];
			chestsKeys[i] = new int[chestsKeysLen[i]];

			for(int j = 0; j < chestsKeysLen[i]; j++) {
				int t;
				cin >> t;
				chestsKeys[i][j] = t;
				precheckKeys[t]++;
			}
		}

		int* solution = new int[N];
		
		cout << "Case #" << c << ": ";
		if(precheck(precheckKeys, N, chestsTypes) && solve(availKeys, N, openedChests, chestsTypes, chestsKeysLen, chestsKeys, 0, solution)) {
			for(int i = 0; i < N; i++) {
				cout << (solution[i] + 1) << " ";
			}
		}
		else {
			cout << "IMPOSSIBLE";
		}
		cout << "\n";
		
		delete [] availKeys;
		delete [] openedChests;
		delete [] chestsTypes;
		delete [] chestsKeysLen;
		for(int i = 0; i < N; i++) {
			delete [] chestsKeys[i];
		}
		delete [] chestsKeys;
	}

	return 0;
}