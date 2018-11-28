/*
LANG: C++
ID: fox05711
PROG: c-large1.cpp
*/
//==========================================
#include <iostream>
#include <cctype>
#include <map>
#include <set>
#include <sstream>
#include <cstring>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <list>
#include <cmath>
#include <algorithm>
#include <set>
#include <fstream>

using namespace std;
int isPal(long long n){
	int m[16];
	int i;
	for (i=0;n!=0;i++){
		m[i]=n%10;
		n/=10;
	}
	int j=0;
	for (i--;j<i;j++,i--)
		if (m[j]!=m[i]) return 0;
	return 1;
}
int main (){
	ifstream fin("c-large1.in");
	ofstream fout("c-large1.out");
	long long n,a,b;
	int t;
	list<long long> pal;
	for (long long i=1;i<=10000000;i++){
		long long ti=i*i;
		if (isPal(i) && isPal(ti)) pal.push_back(ti); 
	}
	fin>>t;
	for (int i=0;i<t;i++){
		fin>>a>>b;
		int ans=0;
		list<long long>::iterator ite;
		for (ite=pal.begin();ite!=pal.end();++ite){
			if ((*ite)>=a && (*ite)<=b){
				ans++;
			}
		}
		fout<<"Case #"<<(i+1)<<": "<<ans<<endl;
	}
	return 0;
}
	

