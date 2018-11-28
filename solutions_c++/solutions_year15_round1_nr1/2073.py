/*
 * MUSHROOM.cpp
 *
 *  Created on: Apr 17, 2015
 *      Author: ngoyal
 */

#include<iostream>

using namespace std;


int main(){
	int T;
	cin>>T;
	int case1=1;
	while(T--){
		int N;
		cin>>N;
		int M[N];
		for(int i=0;i<N;i++){
			cin>>M[i];
		}
		long long int res1=0;
		long long int largestDiff=0;
		for(int i=1;i<N;i++){
			long long int diff=M[i-1]-M[i];
			if(M[i]<M[i-1]){
				res1+=(M[i-1]-M[i]);
			}
			if(diff>0 && diff>largestDiff){
				largestDiff=diff;
			}
		}
		long long int res2=0;
		for(int i=0;i<N-1;i++){
			if(largestDiff>M[i])
				res2+=M[i];
			else
				res2+=largestDiff;
		}
		cout<<"Case #"<<case1<<": "<<res1<<" "<<res2<<"\n";
		case1++;
	}
}
