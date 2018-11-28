/*
 * A.cpp
 *
 *  Created on: May 2, 2015
 *      Author: ngoyal
 */

#include<iostream>
#include<cmath>
#define MAX 10000

using namespace std;
int solve(int R,int C,int W){
	int result=0;
	result=R*(floor(C/W)+ (W-1)+ (C%W!=0));
	return result;
}

int main(){

	int T;
	int caseNo=1;
	cin>>T;
	while(T--){
		long W,R,C;
		cin>>R;
		cin>>C;
		cin>>W;

		int result=solve(R,C,W);

		cout<<"Case #"<<caseNo<<": "<<result<<"\n";
		caseNo++;
	}
}

