#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	int T;
	
	cin >> T;
	
	for (int i = 1; i <= T; i++){
		vector <int> RES;
		string NUMER;
		cin >> NUMER;
		int TAB[500];
		RES.clear();
		
		for (int j = 0; j < 500; j++) {
			TAB[j] = 0;
		}
		
		for (int j = 0; j < NUMER.length(); j++) {
			TAB[(int)NUMER[j]]++;
		}
		
		if(TAB[int('Z')] > 0) {
			for (int j = 0; j < TAB[int('Z')]; j++) {
				RES.push_back(0);
			}
			
			TAB[int('E')] -= TAB[(int)'Z'];
			TAB[int('R')] -= TAB[(int)'Z'];
			TAB[int('O')] -= TAB[(int)'Z'];
		   TAB[int('Z')] = 0;
			
		}
		
		if(TAB[int('W')] > 0) {
			for (int j = 0; j < TAB[int('W')]; j++) {
				RES.push_back(2);
			}
			
			TAB[int('T')] -= TAB[(int)'W'];
			TAB[int('O')] -= TAB[(int)'W'];
		   TAB[int('W')] = 0;
			
		}
		
		if(TAB[int('G')] > 0) {
			for (int j = 0; j < TAB[int('G')]; j++) {
				RES.push_back(8);
			}
			
			TAB[int('E')] -= TAB[(int)'G'];
			TAB[int('I')] -= TAB[(int)'G'];
			TAB[int('H')] -= TAB[(int)'G'];
			TAB[int('T')] -= TAB[(int)'G'];
		   TAB[int('G')] = 0;
			
		}
		
		if(TAB[int('T')] > 0) {
			for (int j = 0; j < TAB[int('T')]; j++) {
				RES.push_back(3);
			}
			
			TAB[int('H')] -= TAB[(int)'T'];
			TAB[int('R')] -= TAB[(int)'T'];
			TAB[int('E')] -= TAB[(int)'T'];
			TAB[int('E')] -= TAB[(int)'T'];
		   TAB[int('T')] = 0;
			
		}
		
		if(TAB[int('R')] > 0) {
			for (int j = 0; j < TAB[int('R')]; j++) {
				RES.push_back(4);
			}
			
			TAB[int('F')] -= TAB[(int)'R'];
			TAB[int('O')] -= TAB[(int)'R'];
			TAB[int('U')] -= TAB[(int)'R'];
		   TAB[int('R')] = 0;
		}
		
			if(TAB[int('F')] > 0) {
			for (int j = 0; j < TAB[int('F')]; j++) {
				RES.push_back(5);
			}
			
			TAB[int('I')] -= TAB[(int)'F'];
			TAB[int('V')] -= TAB[(int)'F'];
			TAB[int('E')] -= TAB[(int)'F'];
		   TAB[int('F')] = 0;
		}
		
			if(TAB[int('V')] > 0) {
			for (int j = 0; j < TAB[int('V')]; j++) {
				RES.push_back(7);
			}
			
			TAB[int('S')] -= TAB[(int)'V'];
			TAB[int('E')] -= TAB[(int)'V'];
			TAB[int('N')] -= TAB[(int)'V'];
			TAB[int('E')] -= TAB[(int)'V'];
		   TAB[int('V')] = 0;
		}
		
		if(TAB[int('S')] > 0) {
			for (int j = 0; j < TAB[int('S')]; j++) {
				RES.push_back(6);
			}
			
			TAB[int('I')] -= TAB[(int)'S'];
			TAB[int('X')] -= TAB[(int)'S'];
		   TAB[int('S')] = 0;
		}
		
		if(TAB[int('O')] > 0) {
			for (int j = 0; j < TAB[int('O')]; j++) {
				RES.push_back(1);
			}
			
			TAB[int('N')] -= TAB[(int)'O'];
			TAB[int('E')] -= TAB[(int)'O'];
		   TAB[int('O')] = 0;
		}
		
				if(TAB[int('I')] > 0) {
			for (int j = 0; j < TAB[int('I')]; j++) {
				RES.push_back(9);
			}
			
			TAB[int('N')] -= TAB[(int)'I'];
			TAB[int('N')] -= TAB[(int)'I'];
			TAB[int('E')] -= TAB[(int)'I'];
			TAB[int('I')] = 0;
		}
		
		cout << "Case #" << i << ": ";
		sort(RES.begin(), RES.end());
		for (int j = 0;  j < RES.size(); j++) {
			cout << RES[j];
		}
		

		
		cout << endl;
		
	}
	
	
	return 0;
}
