//============================================================================
// Name        : A.cpp
// Author      : Loc Ngo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <math.h>
#include <fstream>
using namespace std;
ifstream fin("A-large.in");
#define MAX 1000000
struct node{
	char a;
	int c;
};
int n;
vector<node> A[1000];

int getMin(vector<int>& V){
	int maxV = 1;
	for(int i=0;i<V.size();i++)
		maxV = max(maxV,V[i]);
	int minSteps = MAX;
	for(int v=1;v<=maxV;v++){
		int steps = 0;
		for(int i=0;i<V.size();i++)
			steps += fabs(V[i] - v);
		minSteps = min(steps,minSteps);
	}
	return minSteps;
}

void process(int t){
	fin>>n;
	for(int i=0;i<n;i++)
		A[i].clear();
	for(int i=0;i<n;i++){
		string s;
		fin>>s;
		for(int j=0;j<s.length();j++){
			node tn;
			tn.a = s[j];
			tn.c = 1;
			while(j+1<s.length() && s[j+1]==s[j]){
				tn.c++;
				j++;
			}
			A[i].push_back(tn);
		}
	}

	bool found = true;
	int total = 0;
	for(int j=0;j<A[0].size();j++){
		bool ident = true;
		vector<int> V;
		V.push_back(A[0][j].c);
		for(int i=1;i<n;i++)
			if(A[i].size()!= A[0].size() || A[i][j].a!=A[0][j].a){
				ident = false;
				break;
			}
			else
				V.push_back(A[i][j].c);
		if(!ident){
			found = false;
			break;
		}
		else
			total += getMin(V);

	}
	cout<<"Case #"<<t<<": ";
	if(!found){
		cout<<"Fegla Won\n";
	}
	else
		cout<<total<<endl;
}

int main() {
	int T;
	fin>>T;
	for(int i=1;i<=T;i++)
		process(i);
	return 0;
}
