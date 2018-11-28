/*
 * cjc.cpp
 *
 *  Created on: 2013/04/13
 *      Author: DO
 */

#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<deque>
#include<set>
#include<map>
#include<algorithm>
#include<functional>
#include<utility>
#include<cmath>
#include<complex>
#include<iomanip>

using namespace std;

#define REP(i,s,e) for(int i=int(s);i<=int(e);i++)
#define rep(i,n) for(int i=0;i<int(n);i++)
#define pi 3.14159265358979


bool f(unsigned long long int x){
	vector<int>v;
	for(int i=1;i<=15;i++){

		if(x/10!=0){
			v.push_back(x%10);
			x=x/10;
		}
		else{
			v.push_back(x%10);
			break;
		}
	}

	int s=v.size(); bool b=true;
	if(s%2==0){
		for(int i=0;i<=s/2-1;i++){
			if(v[i]!=v[s-1-i]){
			b=false; break;
			}
		}
	}

	else{

		if(s>=3){
		for(int i=0;i<=(s-3)/2;i++){
			if(v[i]!=v[s-1-i]){
			b=false; break;
			}
		}
	}
	}

	if(b) return true;
	else return false;

}

int main(void){

	int t;
	unsigned long long int b;
    double a;
    cin >> t;

	rep(i,t){

	cin >> a >> b;

	unsigned long long int p=ceil((sqrt(a)));

	unsigned long long int c=0;
	for(unsigned long long int j=p;j*j<=b;j++)
	if(f(j) && f(j*j)) c++;


	cout << "Case #" << i+1 << ": " << c << endl;

	}

	return 0;
}



