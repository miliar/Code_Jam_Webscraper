//
//  main.cpp
//  MaginTrick
//
//  Created by 김민규 on 4/12/14.
//  Copyright (c) 2014 Micky. All rights reserved.
//
#include <iostream>

#define MAX_CASE 100
#define CARD_ROW 4

#define TEST_PER_ASK 2

using namespace std;

int main(int argc, const char * argv[])
{
	char result[MAX_CASE][30];
	int card[CARD_ROW][CARD_ROW];
	int t_cnt;
	
	
	cin >> t_cnt;
	
	for (int i=1; i<=t_cnt; i++) {
		int answer[2];
		int sel_row[CARD_ROW];
		int a_cnt = 0;
		
		int chose = 0;
		
		cin >> answer[0];
		for (int j=0; j<CARD_ROW; j++) {
			for (int k=0; k<CARD_ROW; k++) {
				cin >> card[j][k];
			}
		}
		
		for (int j=0; j<CARD_ROW; j++) {
			sel_row[j] = card[answer[0]-1][j];
		}
		
		cin >> answer[1];
		for (int j=0; j<CARD_ROW; j++) {
			for (int k=0; k<CARD_ROW; k++) {
				cin >> card[j][k];
			}
		}
		
		for (int j=0; j<CARD_ROW; j++) {
			for (int k=0; k<CARD_ROW; k++) {
				if(sel_row[j] == card[answer[1]-1][k]) {
					chose = sel_row[j];
					a_cnt++;
				}
			}
		}
		
		if (a_cnt == 1) {
			sprintf(result[i-1], "Case #%d: %d\n", i, chose);
		}
		else if(a_cnt == 0) {
			sprintf(result[i-1], "Case #%d: Volunteer cheated!\n", i);
		}
		else {
			sprintf(result[i-1], "Case #%d: Bad magician!\n", i);
		}
		
		
	}
	for (int i = 0; i<t_cnt; i++) {
		cout << result[i];
	}
//	cout << "Hello, World!\n";
    return 0;
}

