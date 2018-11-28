/*
LANG: C++
ID: fox05711
PROG: a.cpp
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
int main(){
	int T;
	cin>>T;
	long long r,t;
	long long total;
	for (int i=0;i<T;i++){
		cin>>r>>t;
		long long k=0;
		total=0;
		for (k=0;;k++){
			total+=(2*r+(1+4*k));
			if (total>t) break;
		}
		cout<<"Case #"<<(i+1)<<": "<<k<<endl;
	}
	return 0;
}
