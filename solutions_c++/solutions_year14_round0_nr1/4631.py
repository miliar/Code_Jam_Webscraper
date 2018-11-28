#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main() {
	fstream f;
	fstream x;
	f.open("A-small-attempt0.in",ios::in);
	x.open("output.txt",ios::out);
	int t;
	f>>t;
	for(int i=1;i<=t;i++) {
		int n;
		f>>n;
		vector<int> abc;
		for(int j=1;j<=4;j++) {
			for(int k=1;k<=4;k++) {
				int y;
				f>>y;
				if(j==n) {
					abc.push_back(y);
				}			
			}
		}	
		f>>n;
		for(int j=1;j<=4;j++) {
			for(int k=1;k<=4;k++) {
				int y;
				f>>y;
				if(j==n) {
					abc.push_back(y);
				}			
			}
		}	
		sort(abc.begin(),abc.end());
		int dis =0;
		int sol =0;
		for(int j =0;j<abc.size()-1;j++) {
			if(abc[j]==abc[j+1]) {
				dis++;
				sol = abc[j];
			}
		}
		if(dis == 1) {
			x<<"Case #"<<i<<": "<<sol<<"\n";
		} else if( dis >1) {
			x<<"Case #"<<i<<": Bad magician!\n";
		} else {
		    x<<"Case #"<<i<<": Volunteer cheated!\n";
		}
	}
	f.close();
	x.close();
	return 0;
}
