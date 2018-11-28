#include <iostream>
#include <cstdio>
#include <cstring>
#include <bits/stdc++.h>

using namespace std;

char ch[110];

int main(){
	int T;
	cin >> T;
	for (int ti=1;ti<=T;ti++){
		string s;
		cin >> s;
		int k=0;
		for (int i=1;i<s.length();i++){
			if (s[i]!=s[i-1]) k++;
		}
		if (s[0]=='+') k+=k%2;
			else k+=(k%2==0);
		cout << "Case #" <<ti <<": "<< k<<endl;
	}
	return 0;
}
