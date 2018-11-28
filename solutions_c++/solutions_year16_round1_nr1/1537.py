//Naman Agarwal
//IIT Mandi
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <string>

using namespace std;

#define lli long long int

int main() {
	ios::sync_with_stdio(false);
	int t,tc=1;
	cin>>t;
	while(t--){
		string s;
		cin>>s;
		string a="";
		a=a+s[0];
		for(int i=1;i<=s.length();i++){
			if(s[i]>=a[0])
				a=s[i]+a;
			else
				a=a+s[i];
		}
		cout<<"Case #"<<tc<<": "<<a<<"\n";
		tc++;
	}
	return 0;
}