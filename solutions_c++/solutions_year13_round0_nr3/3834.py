/*
 *	Category: CodeJam
 *  Problem: C.FairAndSquare1.cpp
 *  Status: 
 * 	Date: Apr 13, 2013
 * 	Time: 4:21:43 AM
 * 	Author: Hossam Yousef
 */

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <cmath>
#include <deque>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <complex>
#include <sstream>
#include <utility>
#include <climits>
#include <cstring>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

inline bool isPalind(string S){
	for(int i = 0; i < (int)S.size(); i++){
		int sz = (int)S.size();
		if(S[i] != S[sz-i-1]) return false;
	}
	return true;
}

int main() {

	freopen("test.txt", "rt", stdin);
		freopen("o.txt", "wt", stdout);
	
	int tc; scanf("%d",&tc);
	int A, B;
	string S = "";
	for(int t = 0 ; t < tc; t++){
		scanf("%d%d",&A,&B);
		int count = 0;
		for(int i = (int)sqrt(A); i <= (int)sqrt(B); i++){
			int j = i;
			S = "";
			while(j > 0){
				S += '0'+j%10;
				j /= 10;
			}
			if(isPalind(S)){
				S = "";
				j = i*i;
				if(!(j >= A && j <= B)) continue;
				while(j > 0){
					S += '0'+j%10;
					j /= 10;
				}
				if(isPalind(S)){
					count++;
				}
			}
		}
		printf("Case #%d: %d\n",t+1,count);
	}
	return 0;
}
