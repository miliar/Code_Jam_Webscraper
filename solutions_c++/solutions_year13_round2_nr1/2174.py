//============================================================================
// Name        : Prob1.cpp
// Author      : Loc Ngo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
ifstream fin("A-small-attempt1.in");
ofstream fout("out.txt");
int A[11];
int S,N;

int transform(int s,int index,int n) {
	if (index > n)
		return 0;
	if(s>A[index])
		return transform(s+A[index],index+1,n);
	else {
		if(s==1)
			return transform(s,index,n-1) + 1;
		else
			return min(transform(2*s-1,index,n) + 1,transform(s,index,n-1) + 1);
	}
}

void process(int t){
	fin>>S>>N;
	for(int i=1;i<=N;i++)
		fin>>A[i];
	sort(A+1,A+N+1);

	fout<<"Case #"<<t<<": "<<transform(S,1,N)<<endl;
}

int main() {
	int T;
	fin>>T;

	for(int i=1;i<=T;i++)
		process(i);
	return 0;
}
