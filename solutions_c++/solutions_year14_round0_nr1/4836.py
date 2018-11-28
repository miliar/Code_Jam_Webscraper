// 1.MagicTrick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[]){
	int t;
	cin>>t;
	int cards1[4][4];
	int cards2[4][4];
	bool check[16];
	int row1, row2, found;
	for(int i = 0; i < t; ++i){
		//input
		cin>>row1;
		--row1;
		for(int j = 0; j < 4; ++j)
			for(int k = 0; k < 4; ++k)
				cin>>cards1[j][k];
		cin>>row2;
		--row2;
		for(int j = 0; j < 4; ++j)
			for(int k = 0; k < 4; ++k)
				cin>>cards2[j][k];
		//solving
		found = 0;
		for(int j = 0; j < 16; ++j)
			check[j] = false;
		for(int j = 0; j < 4; ++j)
			check[cards1[row1][j] - 1] = true;
		for(int j = 0; j < 4; ++j)
			if(check[cards2[row2][j] - 1]){
				if(found == 0)
					found = cards2[row2][j];
				else if(found != 0){
					found = -1;
					break;
				}
			}
		//output
		switch (found){
			case 0:
				cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
				break;
			case -1:
				cout << "Case #" << i+1 << ": Bad magician!" << endl;
				break;
			default:
				cout << "Case #" << i+1 << ": " << found << endl;
		}
	}
}

