#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <stdio.h>
#include <map>
using namespace std;

string r = "RICHARD", g = "GABRIEL";

int main(){
	
	freopen ("D-small-attempt0.in","r",stdin);
	freopen ("def","w",stdout);
	
	int t, n, i, j;
	string s;
	int a, b, c;
	vector<int> v;
	cin>>j;
	bool bo[10001];
	string rez;
	
	vector<int> v1;
	
	
	for(int k = 0; k < j; k++){
		cin>>a>>b>>c;
		
		if(b<c)
			swap(b,c);
		
		if(b * c % a)
			rez = r;
		else{
			
			switch(a){
				
				case 1: rez = g; break;
				case 2: rez = g; break;
				case 3: if(c == 1) rez = r; else rez = g; break;
				case 4: if(c <= 2) rez = r; else rez = g; break;
				
				
			}
			
			
		}
		
		cout<<"Case #"<<k+1<<": ";
		cout<<rez<<endl;
	//	cout<<r<<" AAA"<<endl;
	}
	

	return 0;
}
