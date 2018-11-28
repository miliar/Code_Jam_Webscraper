#include <iostream>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <string>

using namespace std;
typedef long long LL;

void flip(int p,string s){
	if(s[0] == '-'){
		for(int i=0;i<=p;i++)
			s[i] = '+';
	}
	else{
		for(int i=0;i<=p;i++)
			s[i] = '-';
	}
}

int main(){
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for(int t=1;t<=T;t++){
		string s;
		int count = 0;
		cin >> s;
		for(int i=0;i<s.size() - 1;i++){
			if(s[i] != s[i+1]){
				flip(i,s);
				count++;
			}
		}
		cout << "Case #" << t << ": ";
		if(s[s.size()-1] == '+')
			cout << count << endl;
		else
			cout << (count + 1) << endl;
	}
	return 0;
}