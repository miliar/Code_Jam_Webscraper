#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstring>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VII;
typedef vector<VS> VSS;

#define PB push_back
	
int sqrt(int n) {
	int left=1, right=n/2+1;
	while(left<right) {
		int mid=left+(right-left)/2;
		if(n/mid==mid) return mid;
		else if(n/mid<mid) right=mid-1;
	      	else left=mid+1;
	}
	if(n/left>=left) return left;
	else return left-1; 
}

bool ispalindrome(int n) {
	int dcount=(int)log10(n);
	if(dcount==0) return true;
	int power=pow(10, dcount);
	while(n>0) {
		int high=n/power;
		int low=n%10;
		if(high!=low) return false;
		n=n%power/10;
		power/=100;
	}
	return true;
}


int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	
	int caseno;
	fin >> caseno;
	for(int i=0; i<caseno; i++) {
		int lim1, lim2;
		fin >> lim1 >> lim2;
		int lim3=sqrt(lim1);
		int lim4=sqrt(lim2);
		if(lim3*lim3<lim1) lim3++;
	    	int count=0;
		for(int j=lim3; j<=lim4; j++) {
			int square=j*j;
			if(ispalindrome(square) && ispalindrome(j)) {
				count++;
			}
		}	
		fout<<"Case #" << i+1 <<": "<<count<<endl;
	}
		
	fin.close();
	fout.close();
	return 0;
}













