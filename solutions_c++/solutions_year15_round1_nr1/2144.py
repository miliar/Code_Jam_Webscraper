// R1A_Q1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

void fun_ans(vector<int>& vec, long & r1, long & r2){
	int rate2=0;
	r1=0, r2=0;

	for(int i=0; i<vec.size()-1; i++){
		if(vec[i]>vec[i+1]){
			r1+=(vec[i]-vec[i+1]);
			if(vec[i]-vec[i+1]>rate2) rate2=vec[i]-vec[i+1];
		}
	}

	for(int i=0; i<vec.size()-1; i++){
		if(vec[i]<rate2) r2+=vec[i];
		else r2+=rate2;
	}
	return;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("D://Practice//A-large.in", "r", stdin);
    freopen("D://Practice//A-large.out", "w", stdout);

	int cases=0;
	cin>>cases;
	for(int i=0; i<cases; i++){
		int n, tmp;
		cin>>n;
		vector<int> vint(n);
		for(int j=0; j<n; j++){
			cin>>vint[j];
		}
		long r1, r2;
		fun_ans(vint, r1, r2);
		cout<<"Case #"<<i+1<<": "<<r1<<' '<<r2<<endl;
	}

	fclose(stdin);
	fclose(stdout);
	system("PAUSE");
	return 0;
}

