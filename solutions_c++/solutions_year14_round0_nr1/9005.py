//
//  main.cpp
//  ex1
//
//  Created by Martin Skrovina on 4/12/14.
//  Copyright (c) 2014 Martin Skrovina. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

#define ROW_NUM 4

using namespace std;



int main(int argc, const char * argv[])
{
	ifstream in("input.txt");
	
	int testNo = 0;
	in >> testNo;
	
	for (int test = 0; test < testNo; test++) {
		int row1 = 0;
		in >> row1;
		--row1;
		
		vector< vector<int> > mat1(ROW_NUM);
		
		for (int i = 0; i < ROW_NUM; i++) {
			mat1[i].resize(ROW_NUM);
		}
		
		for (int j = 0; j < ROW_NUM; j++) {
			for (int k = 0; k < ROW_NUM; k++) {
				in >> mat1[j][k];
			}
		}
		
		vector<int> vec1 = mat1[row1];
		
		int row2 = 0;
		in >> row2;
		--row2;
		
		vector< vector<int> > mat2(ROW_NUM);
		
		for (int i = 0; i < ROW_NUM; i++) {
			mat2[i].resize(ROW_NUM);
		}
		
		for (int j = 0; j < ROW_NUM; j++) {
			for (int k = 0; k < ROW_NUM; k++) {
				in >> mat2[j][k];
			}
		}
		
		vector<int> vec2 = mat2[row2];
	
		int sims = 0;
		int num = 0;
		for (int i = 0; i < ROW_NUM; i++) {
			for (int j = 0; j < ROW_NUM; j++) {
				if (vec2[j] == vec1[i]) {
					sims++;
					num = vec2[j];
				}
			}
		}
		
		cout << "Case " << "#" << (test + 1) << ":" << " ";
		switch (sims) {
			case 1:
				cout << num;
				break;
			case 0:
				cout << "Volunteer cheated!";
				break;
			default:
				cout << "Bad magician!";
				break;
		}
		cout << endl;
	}
	
    return 0;
}

