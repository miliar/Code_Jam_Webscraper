/*
 * main.cpp
 *
 *  Created on: 05/02/2014
 *      Author: sheidechammas
 */



#include <iostream>
#include <stdio.h>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <fstream>
#include <sstream>

using namespace std;


int main(int argc, char* argv[]) {
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("ouput.txt", "w", stdout);
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		int answer1, answer2;
		vector<vector<int> > arrangement1(4);
		vector<vector<int> > arrangement2(4);
		cin >> answer1;
		answer1--;
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				int card;
				cin >> card;
				arrangement1[i].push_back(card);
			}
		}
		cin >> answer2;
		answer2--;
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				int card;
				cin >> card;
				arrangement2[i].push_back(card);
			}
		}
		printf("Case #%d: ", t);
		int count=0, answer;
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				if(arrangement1[answer1][i] == arrangement2[answer2][j]) {
					answer = arrangement1[answer1][i];
					count++;
				}
			}
		}
		if(count==0) {
			printf("Volunteer cheated!\n");
		} else if(count > 1) {
			printf("Bad magician!\n");
		} else {
			printf("%d\n", answer);
		}
	}
}

