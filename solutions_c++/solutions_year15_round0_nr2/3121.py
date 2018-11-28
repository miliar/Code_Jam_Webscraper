#include <stdio.h>
#include <fstream>
#include <vector>
#include <iostream>
#include <cmath>
using namespace std;


int main() {
	int nTest;
	ifstream cin("input.txt");
	ofstream cout("out.txt");
	cin>>nTest;
	for(int k=1; k<=nTest; k++){
		int n, tmp, imax, answer =1<<30;
		cin>>n;
		vector<int> v;
		for(int i=0; i<n; i++){
			cin>>tmp;
			v.push_back(tmp);
			if(tmp > imax){
				imax = tmp;
			}
		}
		for(int i=1; i<=imax; i++){
			int total = i;
			for(int j=0; j<v.size(); j++){
				total +=(v[j] -1)/i;
			}
			if(total < answer){
				answer = total;
			}
		}
		cout<<"Case #"<<k<<": "<<answer<<endl;
	}
}
