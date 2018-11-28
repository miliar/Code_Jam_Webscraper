//============================================================================
// Name        : Google.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
using namespace std;
#define cin fin
ifstream fin("in.in");
#define cout fout
ofstream fout("out.out");

int main() {
	int T, N;
	cin >> T;
	for(int i = 1; i <= T; i++){
		cin >> N;
		vector<double> Na(N);
		vector<double> Ke(N);
		for(int j = 0; j < N; j ++) cin >> Na[j];
		for(int j = 0; j < N; j ++) cin >> Ke[j];
		sort(Na.begin(), Na.end());
		sort(Ke.begin(), Ke.end());
		int first = 0, second = 0;

		int na = 0;
		int ke = 0;
		while(na < N && ke < N){
			while(ke < N && Na[na] > Ke[ke])
				ke++;
			if(ke >= N)
				break;
			na++;ke++;
		}
		first = N-na;

		list<double> La;
		list<double> Le;
		for(int j = 0; j < N; j ++){
			La.push_back(Na[j]);
			Le.push_back(Ke[j]);
		}

		while(!La.empty()){
			if(La.front() < Le.front())
				Le.pop_back();
			else
			{
				Le.pop_front();
				second++;
			}
			La.pop_front();
		}

		cout<<"Case #"<<i<<": "<<second<<" "<<first<<endl;
	}
}
