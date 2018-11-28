/*
 * fairsquare.cpp
 *
 *  Created on: 13-Apr-2013
 *      Author: saurav
 */
#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
#define limit 100000000000000
//#define limit 1000

int checkpalindrome(long long int N){
	long long int rev=0,temp=N;
	while(N>0){
		rev=rev*10+N%10;
		N/=10;
	}
	return temp==rev;
}

int main(){
	int T,count;
	unsigned long long int A,B,i;
	vector<long long int> square;
	scanf("%d",&T);
	for(i=1;i*i<=limit;i++) {
		if(checkpalindrome(i*i)){
			if(checkpalindrome(i)){
				square.push_back(i*i);
			}
		}
	}
	/*for(i=0;i<square.size();i++)
		printf("%lld\n",square.at(i));*/
	for(int t=0;t<T;t++){
		scanf("%lld %lld",&A,&B);
		count=0;
		for(i=0;i<square.size();i++) {
			if(square.at(i)>=A&&square.at(i)<=B) {
				count++;
				//printf("%lld\n",square.at(i));
			}
		}
		printf("Case #%d: %d\n",t+1,count);
	}
}
