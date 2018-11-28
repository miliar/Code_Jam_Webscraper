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
        cin.sync_with_stdio(0);
	int t;
	cin >> t;
	double i,c,f,x,d,cas;
	for (int n=0; n<t; n++) {
		d=2; cas=0;
		cin >> c >> f >> x;
		while (1)  {
			if ((x-c)/d>x/(d+f)) {cas+=c/d; d+=f;}
			else {cas+=x/d; break;}}		
		cout.setf(ios::fixed,ios::floatfield);
		cout.precision(7);	
		cout << "Case #" << n+1 << ": " << cas << endl;}  
 			 
		 
        return 0;}  
