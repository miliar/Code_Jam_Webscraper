#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
using namespace std;

int N;
int words[200][1000];
int wordsSize[200];
int dictSize;
int bestSol;


void test(char *eng, char *fra, int index);

void test(char *eng, char *fra, int index) {
	//end case
	int sol;
	if (index == N) {
		sol = 0;
		for (int i=0; i<dictSize; i++) sol += (eng[i]&fra[i]);
		if (sol < bestSol) {
		//	printf("sol %d\n", sol);
		//	for (int i=0; i<dictSize; i++) printf("i %d, eng %d, fra %d\n", i, eng[i], fra[i]);
			bestSol = sol;
		}
		return;
	}
	
	//try eng
	char *neweng = new char [dictSize];
	memcpy(neweng, eng, dictSize);
	for (int i=0; i<wordsSize[index]; i++) neweng[words[index][i]] = 1;	//add to dictionary
	int soleng = 0;
	for (int i=0; i<dictSize; i++) soleng += (neweng[i]&fra[i]);
	
	//try fra
	char *newfra = new char [dictSize];
	memcpy(newfra, fra, dictSize);
	for (int i=0; i<wordsSize[index]; i++) newfra[words[index][i]] = 1;	//add to dictionary
	int solfra = 0;
	for (int i=0; i<dictSize; i++) solfra += (eng[i]&newfra[i]);
	
	//try the smaller solution first -- should get better pruning
	if (soleng < solfra) {
		if (soleng < bestSol) test(neweng, fra, index+1);
		if (solfra < bestSol) test(eng, newfra, index+1);
	}
	else {
		if (solfra < bestSol) test(eng, newfra, index+1);
		if (soleng < bestSol) test(neweng, fra, index+1);
	}
	
	delete[] neweng;
	delete[] newfra;
}





int main(void) {
	int T;
	string s;
	
	int i;
	
	
	fscanf(stdin, "%d\n", &T);
	
	map<string,int> dict;
	map<string,int>::iterator it;
	
	char *eng;
	char *fra;
	char entireline[100000];
	
	
	for (int t=1; t<=T; t++) {
		dict.clear();
		dictSize = 0;
		fscanf(stdin, "%d\n", &N);
	//	printf("t %d, N %d\n", t, N);
		for (i=0; i<N; i++) {
			fgets(entireline, sizeof(entireline), stdin);
			stringstream ss(entireline);
			wordsSize[i] = 0;
			while (1) {
				ss >> s;
				if (!ss.good()) break;
				it = dict.find(s);
				if (it == dict.end()) {
					dict.insert( pair<string,int>(s, dictSize) );
					dictSize++;
				}
				words[i][wordsSize[i]] = dict[s];
				wordsSize[i]++;
			//	printf("%s.", s.c_str());
			}
		//	printf("\n");
		}
	//	if (t==4) {
		/*
		for (it=dict.begin(); it!=dict.end(); it++) {
			printf("%d %s\n", it->second, it->first.c_str());
		}
	//	*/
		/*
		for (i=0; i<N; i++) {
			for (int j=0; j<wordsSize[i]; j++) printf("%d ", words[i][j]);
			printf("\n");
		}
	//	*/
	//	}
		
		eng = new char [dictSize];
		fra = new char [dictSize];
		memset(eng, 0, dictSize);
		memset(fra, 0, dictSize);
		for (i=0; i<wordsSize[0]; i++) eng[ words[0][i] ] = 1;
		for (i=0; i<wordsSize[1]; i++) fra[ words[1][i] ] = 1;
		bestSol = dictSize;
	//	if (t==4) {
		/*
		printf("dictSize %d, wordsSize %d %d\n", dictSize, wordsSize[0], wordsSize[1]);
		for (i=0; i<dictSize; i++) printf("%d%d ", eng[i], fra[i]);
		int k=0;
		for (i=0; i<dictSize; i++) k += (eng[i]&fra[i]);
		printf("\nk %d\n", k);
	//	*/
	//	}
		
		test(eng, fra, 0);
		
		delete[] eng;
		delete[] fra;
		
		
		
		printf("Case #%d: ", t);
		
		
		printf("%d", bestSol);
	//	printf("%s", str);
	//	printf("%s", str.c_str());
		printf("\n");
	}
	return 0;
}