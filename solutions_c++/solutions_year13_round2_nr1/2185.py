///*
// * ProbA.cpp
// *
// *  Created on: 13-Apr-2013
// *      Author: nataraj
// */
//
//
//
#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <algorithm>
#include <limits.h>
using namespace std;

int T,prob;
int A;
int inp[101];
int N;

void solve(){
	sort(inp,inp+N);
	long long res=0;long long sum=A;
	for(int i=0;i<N;++i){
		if(sum>inp[i]){
			sum+=inp[i];
		}
		else{
			if(sum+sum-1 > inp[i]){
				res++;
				sum= (sum+sum-1+inp[i]);
			}else{
				long long tempSum = sum;
				long long tempres = 0;
				while(tempSum<=inp[i]){
					if(tempSum==1){
						tempres=LONG_LONG_MAX;
						break;
					}
					tempres++;
					tempSum += (tempSum-1);
				}
				if(tempres<(N-i)){
					res+=tempres;
					sum = tempSum;
					sum+=inp[i];
				}else{
					res+= (N-i);
					break;
				}
			}
		}
	}
	printf("Case #%d: %lld\n", prob++,res);
}
int main(int argc, char **argv) {
	scanf("%d",&T);
	prob=1;
	while(T--){
		scanf("%d%d",&A,&N);
		for(int i=0;i<N;++i){
			scanf("%d",&inp[i]);
		}
		solve();

	}
	return 0;
}

