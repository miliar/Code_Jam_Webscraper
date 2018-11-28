#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<iostream>
#include<string.h>
#include<limits.h>
#include<functional>
#include<vector>
#include<utility>
#include<stdlib.h>
#include<time.h>
using namespace std;

#define mem(a) memset(a,0,sizeof(a))
int len;

string reduce(string s) {
	string a = s;
	int i=1;
	char prev = s[0];
	int in = 1;
	while(i<s.length()) {
		if(s[i] == prev) {
			i++;
			continue;
		}
		prev = s[i];
		a[in] = s[i];
		in++;
		i++;
	}
	len = in;
	return a;
}

int main() {
	// your code goes here
	long long tc;
	cin>>tc;
	for(int c=1;c<=tc;c++) {
		string s;
		cin>>s;
		len=0;
		s = reduce(s);
		if(len == 1) {
			if(s[0] == '+'){
				cout<<"Case #"<<c<<": "<<0<<endl;
			} else {
				cout<<"Case #"<<c<<": "<<1<<endl;
			}
			continue;
		}
		if(s[0] == '+'){
			if(len&1) {
				cout<<"Case #"<<c<<": "<<len-1<<endl;
			} else {
				cout<<"Case #"<<c<<": "<<len<<endl;
			}
		} else {
			if(len&1) {
				cout<<"Case #"<<c<<": "<<len<<endl;
			} else {
				cout<<"Case #"<<c<<": "<<len-1<<endl;
			}
		}
	}
	return 0;
}
