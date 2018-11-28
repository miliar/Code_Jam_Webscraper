//============================================================================
// Name        : standing_Ovation.cpp
// Author      : Rakesh Sharma
// Version     :
// Copyright   : MIT
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <istream>
#include <ostream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int count_zeros(string s);
int peopleStanding(int index, string s);

int main() {
	//Read and write input files
	freopen("A-small-attempt4.in","r",stdin);
	freopen("A-small-attempt4.out","w",stdout);

	int totalCases(0);
	cin >> totalCases;
	for(int caseNum=0;caseNum<totalCases;caseNum++){
		int maxShy(0);
		string totalAudience = "";
		cin >> maxShy;
		cin >> totalAudience;
		printf("Case #%d: %d\n",(caseNum+1),count_zeros(totalAudience));
	}

	return 0;
}

int count_zeros(string s) {
	int count = 0;
	for(int i = 0; i < s.size(); i++){
		if(s[i] == '0'){
			if((peopleStanding(i+1,s)+count)<i+1){
				count++;
			}
		}
	}
	return count;
}

int peopleStanding(int index, string s){
	int totalStanding(0);
	for(int i = 0; i < index; i++){
		char s2[1];
		s2[0] = s[i];
		char * sz;
		totalStanding += strtol(s2,&sz,10);
	}
	return totalStanding;
}
