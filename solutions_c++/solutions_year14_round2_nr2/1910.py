//Author : wiragotama@gmail.com
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <utility>
#include <stack>
#include <queue>
using namespace std ;
typedef long long int LL ;

//for sorting
bool asc (int i,int j) { 
	return (i<j);
}

bool dsc (int i,int j) { 
	return (i>j);
}
//main program
int main () {
	int t;
	scanf("%d",&t);
	for (int i=1; i<=t; i++) {
		int a, b, k;
		scanf("%d%d%d",&a,&b,&k);
		long result = 0;
		
		for (int j=0; j<a; j++) {
			for (int x=0; x<b; x++) {
				int tmp = j&x;
				if (tmp < k) {
					result++;
				}
			}
		}
		printf("Case #%d: %ld\n",i,result);
	}
	return 0;
}
