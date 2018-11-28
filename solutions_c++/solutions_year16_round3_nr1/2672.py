#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <bits/stdc++.h>
#include <stdio.h>
#include <string.h>
#include <sstream>
using namespace std;


ofstream fout("C:\\Users\\Harry\\Desktop\\temp");

#define cout fout
#define cin fin

bool allZeros(vector<int> P){
	for(int i=0; i<P.size(); i++){
		if(P[i]!= 0){
			return false;
		}
	}
	return true;
}

bool checkWith(vector<int> &P, vector<int> &D, int diff, int *total){
	stringstream ss;
//	cout<<"pSize= "<<P.size();
	vector<int> changes;
	int diffCopy = diff;
	*total -= diff;
//	cout<<"total = "<<*total<<endl;

	if(*total == 0){
		for(int i=0; i<P.size(); i++){
			while(P[i] > 0){
				cout<<(char)('A' + i);
				P[i] -- ;
			}
		}
		return true;
	}


	for(int i=0; i<P.size(); i++){
//		cout<<"p = "<<P[i]<<","<< P[i]/(float) *total <<"\t";
		if(P[i]/(float) *total > 0.5){
			if(diff > 0){
				diff--;
				changes.push_back(i);
				P[i]--;
				ss<< (char)(65 + i);
			}
			else{
				for(int j=0; j<changes.size(); j++){
					P[changes[j]]++;
				}
				*total += diffCopy;
				return false;
			}
		}
	}

	if(diff > 0){
		for(int i=0; i<P.size(); i++){
			while(P[i] > 0 && diff > 0){
				diff--;
				P[i] -- ;
				ss<< (char)(65 + i);
			}
		}
	}

	cout<< ss.str() << " ";
	return true;
}

int main() {
	//Enter your code here. Read input from STDIN. Print output to STDOUT
//	ofstream fout("C:\\Users\\Harry\\Desktop\\temp");
	ifstream fin("C:\\Users\\Harry\\Desktop\\A-large.in");
	int t;
	cin>>t;
	string buff;
	getline(cin, buff);



	for(int tc = 1; tc <=t; tc++){
		int N; cin>>N;
		vector<int> P(N), D(N);
		int total;
		for(int i=0; i<N; i++){
			cin>>P[i];
			total += P[i];
		}

		for(int i=0; i<N; i++)
			D[i] = total;

		cout<<"Case #"<<tc<<": ";

		while(total > 0){
			if(checkWith(P,D,1,&total)){
//				cout<<"in 1"<<endl;
					//do nothing
			}
			else{
				checkWith(P,D,2,&total);
//				cout<<"in 2"<<endl;
			}
		}

//		cout<<"Case #"<<tc<<": "<<C<<" "<<J;
		cout<<endl;
	}


	fout.close();
	return 0;
}
