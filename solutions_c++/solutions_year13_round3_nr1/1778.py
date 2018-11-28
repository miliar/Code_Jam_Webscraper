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
long long L;
bool dp[101][101];
//long long ans[101][101];
long long res=0;
char inp[101];
int n;
void solve(){
	L=strlen(inp);
	res=0;
	for(int i=0;i<=L;++i){
		dp[0][i]=false;
		dp[i][0]=false;
//		ans[0][i]=0;
//		ans[i][0]=0;
	}

	for(int i=0;i<=L;++i){
		for(int j=0;j<=L;++j){
			if(i>j){
				dp[i][j]=false;
			}

		}
	}

	for(int i=1;i<=L;++i){
		for(int j=i;j<=L;++j){
			if(j-i+1 <n){
				dp[i][j]=false;
//				ans[i][j]=0;
			}else{
				if(dp[i][j-1]==true){
					dp[i][j]=true;
//					ans[i][j]=ans[i][j-1]+1;
					++res;
				}else{
					int consCons=0;int maxconsCons=0;
					for(int k=i;k<=j;++k){
						if(inp[k-1]=='a' || inp[k-1]=='e' || inp[k-1]=='i' || inp[k-1]=='o' || inp[k-1]=='u'){
							if(maxconsCons<consCons)
								maxconsCons= consCons;
							consCons=0;
						}else{
							++consCons;
						}
					}
					if(maxconsCons < consCons)
						maxconsCons = consCons;

					if(maxconsCons>=n){
						dp[i][j]=true;
//						ans[i][j]=1;
						++res;
					}else{
						dp[i][j]=false;
//						ans[i][j]=0;
					}
				}
			}
		}
	}
	printf("Case #%d: %lld\n",prob++,res);

}
int main(int argc, char **argv) {
	scanf("%d",&T);
	prob=1;
	while(T--){
		scanf("%s%d",inp,&n);
		solve();

	}
	return 0;
}

