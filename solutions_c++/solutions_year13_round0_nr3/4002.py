//============================================================================
// Name        : Tiny3.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <sstream>
#include <algorithm>
#define rep(i,n) for(int i = 0;i<n;i++)
typedef unsigned long long ull;
using namespace std;

ull table[] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
int tsize = sizeof(table)/sizeof(ull);
int main() {
	int T;
	cin >> T;
	for(int Case = 1;Case<=T;Case++){
		ull a,b;
		cin >> a >> b;
		bool ea,eb;
		ull ta = lower_bound(table,table+tsize,a) - table;
		ull tb = lower_bound(table,table+tsize,b) - table;
		ea = (a == table[ta]);
		eb = (b == table[tb]);
		if(ea && eb){
			cout << "Case #" << Case << ": " << tb - ta + 1 << endl;
		}else if(ea && !eb){
			cout << "Case #" << Case << ": " << tb - ta<< endl;
		}else if(!ea && eb){
			cout << "Case #" << Case << ": " << tb - ta + 1 << endl;
		}else{
			cout << "Case #" << Case << ": " << tb - ta<< endl;
		}
	}
	return 0;
}
