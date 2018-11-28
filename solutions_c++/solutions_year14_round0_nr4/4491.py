#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main() {
	fstream f;
	fstream x;
	f.open("D-large.in",ios::in);
	x.open("output.txt",ios::out);
	int t;
	f>>t;
	for(int i=1;i<=t;i++) {
		int n;
		f>>n;
		vector<double> naomi;
		vector<double> kim;
		for(int j=0;j<n;j++) {
			double y;
			f>>y;
			naomi.push_back(y);
		}
		for(int j=0;j<n;j++) {
			double y;
			f>>y;
			kim.push_back(y);
		}
		sort(naomi.begin(),naomi.end());
		sort(kim.begin(),kim.end());
		int tr =0;
		int stp =0;
		for(int j=0;j<n;j++) {
			while((stp!=n)&&(naomi[j]>kim[stp])){
				stp++;
			}	
			if(stp<=n-1) {
				tr++;
				stp++;
			} else if(stp>=n) {
				j=n;
			}
		}
		int nama= n-tr;
		int namb=0;
		int fp =0;
		int lp =n-1;
		for(int j=0;j<n;j++) {
			if(naomi[j]>kim[fp]) {
				namb++;
				fp++;
			} else {
				if(naomi[j]>kim[lp]) {
					namb++;
					lp--;
				} else {
					lp--;
				} 	
			}
		}

		x<<"Case #"<<i<<": "<<namb<<" "<<nama<<"\n";
	}
	f.close();
	x.close();
	return 0;
}
