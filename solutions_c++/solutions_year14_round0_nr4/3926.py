#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <iomanip>
#define unsigned int uint
#define ff first
#define ss second
using namespace std;




int main() {
        int t,N;
	cin >> t;
	for (int n=0; n<t; n++) {
		cin >> N;
		vector<double> V1(N);
		vector<double> V2(N);
		for (int i=0; i<N; i++) cin >> V1[i]; 
		for (int i=0; i<N; i++) cin >> V2[i];
		sort(V1.begin(),V1.end());
		sort(V2.begin(),V2.end());
		vector<double> V3(V2);		
		

		int war=0;
		for (int i=0; i<N; i++) {
			 if (V1[i]>V2[V2.size()-1]) V2.erase(V2.begin()); 
				 else {
					for (uint j=0; j<V2.size(); j++) 
					if (V1[i]<V2[j]) {V2.erase(V2.begin()+j); war++; break;} }}
				
		int dwar=0,it1=N-1,it2=N-1; 
		for (int i=0; i<N; i++) {
			if (V1[it1]>V3[it2]) {dwar++; it1--; it2--;}
			else it2--;}			 		
		
		cout << " Case #" << n+1 << ": " << dwar << " " <<  N-war << endl;}
        return 0;}  
