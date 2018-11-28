#include <bits/stdc++.h>

using namespace std;
ifstream fin("test.in");
ofstream fout("test.out");

string S;
int N,rs,j;
int main(){
	fin >> N;
	for(int i = 0;i<N;i++){
		fin >>S;
		rs = j = 0;
		while(S[j]=='-' && j < S.length()) j++;
		if(j) rs++;
		for(;j<S.length();j++){
			if(S[j] == '-'){
				while(S[j] == '-' && j < S.length()) j++;
				rs+=2;
			}
		}
		fout << "Case #" << i+1 << ": " << rs << '\n'; 
	}
}
