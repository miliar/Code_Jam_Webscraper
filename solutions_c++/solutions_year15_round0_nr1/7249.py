#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
using namespace std;

int main(){
	int t,smax;scanf("%d",&t);
	char c;
	for(int i=0;i<t;i++){
		scanf("%d",&smax);
		c=getchar();
		vector<int> vec(smax+1),sumvec(smax+1);
		for(int j=0;j<smax+1;j++){
			c=getchar();
			vec[j]=(c-'0');
		}
		sumvec[0]=vec[0];sumvec[1]=vec[0];
		for(int j=2;j<smax+1;j++){
			sumvec[j]=vec[j-1]+sumvec[j-1];
		}
		int maxdiff=0;
		for(int j=1;j<smax+1;j++){
			if(vec[j]!=0){
				maxdiff=max(maxdiff,j-sumvec[j]);
			}
		}
		printf("Case #%d: %d\n", i+1, maxdiff);
	}
}
