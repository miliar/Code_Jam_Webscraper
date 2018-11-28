#include <stdio.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <stdio.h>
#include <sstream>
#include <climits>
#include "limits.h"
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <math.h>
#include <map>


#define MaxLength 2147483647
#define INF 0x3f3f3f3f
#define NEG -1
#define MN 105
#define max(a, b) return a>b ? a : b
#define min(a, b) return a<b ? a : b
#define FOR(i, n) for(int i=0; i<n; i++)

using namespace std;

int mem[MN];
int N,A,B,C,D,M,Q,X,Y,T,R,K,L,U,S;


int main(){		
	int j,k,tt,a,b,c,s,t,n,d,x,y,r,u,v,p;
	long long res;
	long long current;
	scanf("%d\n",&T);
	for (tt = 1; tt <= T; tt++) {
	    res = 0;
	    memset(mem,0,sizeof(mem));
		scanf("%d\n",&N);
		if(N == 0) {
		    
		} else {
		    int i=1;
		    while(1) {
		        current = i * (long long)N;
		        while(current) {
		            mem[current%10] = 1;
		            current /= 10;
		        }
		        int tmp =0;
		        FOR(j,10) {
		            tmp += mem[j];
		        }
		        if(tmp == 10) {
		            res = i * N;
		            break;
		        }
		        i++;
		    }
		    
		}
		
		if(res) {
		    printf("Case #%d: %lld\n",tt,res);
		} else {
		    printf("Case #%d: INSOMNIA\n",tt);
		}
		
		/*
		FOR(i,N+1){
			char ch = getchar();
			mem[i] = ch;
			mem[i+1] = 0;
		}
		puts(mem);
		int standed = 0;
		res = 0;
		FOR(i,N+1){
			if(standed >= i){
				standed += mem[i];
			} else {
				res += i-standed;
				standed = i + mem[i];
			}
		}


		printf("Case #%d: %d\n",tt,res);
		*/
	}
	
	return 0;
}

