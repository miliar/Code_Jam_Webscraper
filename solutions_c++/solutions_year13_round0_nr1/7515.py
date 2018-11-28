/*

* File Name : 1.cpp

* Creation Date : 13-04-2013

* Last Modified : Sat 13 Apr 2013 12:53:08 PM IST

* Created By : ShehbazJaffer <shehbazjaffer007@gmail.com> 

_._._._._._._._._._._._._._._._._._._._._.*/

#include<iostream>
#include<vector>
#include<sstream>
#include<queue>
#include<stack>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<map>
#include<deque>
#include<algorithm>
#include<bitset>
#include<iomanip>


#define ll long long
#define ld long double
#define modval 1000000007

using namespace std;

int 
main(int argc, char *argv[])
{
	int T,t,i,j;
	char A[4][4];
	int done,notcomplete;
	string str;
	cin >> T >> ws;
	for(t=1;t<=T;t++){
		done=-1;
		notcomplete=0;
		// take input
		
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%c",&A[i][j]);
				if(A[i][j] == '.'){ notcomplete=1; }  // check for incomplete
			}
			cin >> ws;
		}
	/*	
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				printf("%c ",A[i][j]);
			}
			printf("\n");
		}
*/
		// check for rows

		for(i=0;i<4;i++){
			char word= A[i][0];
			if(word == 'T') {word= A[i][1];}
			if(word == '.') {continue;}
			for(j=1;j<4;j++){
				if(A[i][j] == word || A[i][j] == 'T') {
					done = 1; 
					continue; 
				} else {
					done = -1;
					break;
				}
			}
			if(done == 1) {
				cout << "Case #" << t << ":" << " " << word << " won\n";break;
			}
		}
		if(done == 1) {continue;}

		// check for column
		
		for(i=0;i<4;i++){
			char word= A[0][i];
			if (word == 'T') { word = A[1][i];}
			if (word == '.') {continue;}
			for(j=1;j<4;j++){
				if(A[j][i] == word || A[j][i] == 'T') { done = 1; continue; } 
				else { done = -1; break;}
			}
			if(done == 1) {
				cout << "Case #" << t << ":" << " " << word << " won\n";break;
			}
		}
		if(done == 1) {continue;}

		// check for diaognals
		
		char word = A[0][0];
		if(word=='T') { word = A[1][1];}
		for(j=1;j<4;j++){
			if(word=='.') {break;}
			if(A[j][j] == word || A[j][j] == 'T') { done=1; continue;}
			else {done=-1;break;}
		}
		if(done==1) {
				cout << "Case #" << t << ":" << " " << word << " won\n"; continue;
		}

		word = A[0][3];
		if(word== 'T') {word = A[1][2];}
		for(j=2;j>=0;j--){
			if(word=='.') {break;}
			if(A[3-j][j] == word || A[3-j][j] == 'T') {done=1; continue;}
			else { done=-1; break;}
		}
		if(done==1) {
				cout << "Case #" << t << ":" << " " << word << " won\n"; continue;
		}
			
		if(notcomplete== 1) { cout << "Case #" << t << ":" << " Game has not completed\n"; continue;}

		cout << "Case #" << t << ":" << " Draw\n"; continue;
	
	}
	
	return 0;	
}
