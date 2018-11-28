/*
 * ProbC.cpp
 *
 *  Created on: 13-Apr-2013
 *      Author: nataraj
 */




#include <cmath>
#include <climits>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <iterator>
#include <sstream>
#include <algorithm>
using namespace std;

int T,prob;
int N,M;
int inp[100][100];
int rowMax[100];
int colMax[100];


bool solve(){
	for(int i=0;i<N;++i){
		int tempRowMax = INT_MIN;
		for(int j=0;j<M;++j){
			scanf("%d",&inp[i][j]);
			if(tempRowMax<inp[i][j])
				tempRowMax=inp[i][j];
		}
		rowMax[i]=tempRowMax;
	}
	for(int j=0;j<M;++j){
		int tempColMax=INT_MIN;
		for(int i=0;i<N;++i){
			if(tempColMax<inp[i][j])
				tempColMax=inp[i][j];
		}
		colMax[j]=tempColMax;
	}
	for(int i=0;i<N;++i){
		for(int j=0;j<M;++j){
			if(inp[i][j] <rowMax[i] && inp[i][j]<colMax[j])
				return false;
		}
	}
	return true;
}
int main(int argc, char **argv) {
	scanf("%d",&T);prob=1;
	while(T--){
		scanf("%d%d",&N,&M);int pos=0;
//		for(int i=0;i<N;++i){
//			for(int j=0;j<M;++j){
//				scanf("%d",&inp[i][j]);
//			}
//		}
		bool ret = solve();
		printf("Case #%d: %s\n",prob++,ret?"YES":"NO");
	}
	return 0;
}
