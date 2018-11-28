// Include Header and Libraries
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <iomanip>

#define FOR(i,n) for(int i=0;i<n;i++)

using namespace std;

int a[5][9] = { 0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0, 3,-4,1,-2,0,2,-1,4,-3, -2,1,4,-3,0,3,-4,-1,2, 1,2,-3,-4,0,4,3,-2,-1};
//i=2,j=3,k=4

string s;

// Main Program Starts
int main() {

	
	// Input file handling
	string line;
  	ifstream ifh ("R-small-practice.in");
  	if (!ifh.is_open()) {
  		cout << "Can't open input file";
		return 1;
	}

	int mul(char,int);
	
	//bool fun(int,char,int);
	bool fun(int,char);
	
	int T=0,X=0,L=0;

	getline(ifh,line);
	stringstream(line) >> T;

	FOR(t,T){
		
		size_t oldParsePos=0;
		size_t newParsePos=0;
		
		getline(ifh,line);
		
		newParsePos=line.find(' ',oldParsePos);
		stringstream(line.substr(oldParsePos,newParsePos-oldParsePos)) >> X;
		oldParsePos=newParsePos+1;

		newParsePos=line.find(' ',oldParsePos);
		stringstream(line.substr(oldParsePos,newParsePos-oldParsePos)) >> L;
		oldParsePos=newParsePos+1;

		getline(ifh,line);

		s.clear();

		FOR(i,L)
			s+=line;

		//cout << X << " " << L << " " << s << endl;

		//if(fun(s.size()-1,'k',L))
		if(fun(s.size()-1,'k'))
			cout << "Case #" << t+1 << ": " << "YES" << endl;
		else
			cout << "Case #" << t+1 <<": " << "NO" << endl;
	}
	return 0;
}


	int mul(char x,int y) {
		return a[x-'i'+2][y+4];
	}

	//bool fun(int pos,char c,int L){
	bool fun(int pos,char c){
		int m=1;		
		
	if(c=='k'){
		for(int i=pos;i>=0;i--)
		{
			m=mul(s[i],m);
			if(m==4){
				//cout << "Matched k at pos=" << i <<  endl; 
				if(fun(i-1,'j')) return true;
			}
		}
	}

	else if (c=='j') {
		for(int i=pos;i>=0;i--)
		{
			m=mul(s[i],m);
			
			if(m==3){
				//cout << "Matched j at pos=" << i << endl; 
				if(fun(i-1,'i')) return true;
			}
		}
	}

	else if (c=='i') {
		for(int i=pos;i>=0;i--)
		{
			m=mul(s[i],m);
			
			if(m==2){
				//if(c=='i' && i==0 && j==1) { cout << "Matched i at pos=" << i<< endl;
				if(i==0) {//cout << "Matched i at pos=" << i<< endl;
					return true;
				}
			}
		}
	}

	return false;
}















			
