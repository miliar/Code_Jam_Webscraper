// A.cpp : Defines the entry point for the console application.
//

#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>

using namespace std;
#define ll long long

int isPal(int n){
	stringstream ss;
	ss<<n;
	string s;
	ss>>s;
	for(int i=0;i<s.length()/2;++i){
		if(s[i]!=s[s.length()-i-1])return false;
	}
	return true;

}
int main()
{

	int T;
	cin>>T;
	for(int _t=1;_t<=T;++_t){
		int a,b;
		cin>>a>>b;

		int result=0;
		for(int i=a;i<=b;++i){
			bool good=false;
			for(int j=1;j*j<=i;++j){
				if(j*j==i){
					good=isPal(j);
					break;
				}
			}
			if(good&&isPal(i)){
				++result;
			}
		}
		cout<<"Case #"<<_t<<": "<<result<<endl;

	}

}



