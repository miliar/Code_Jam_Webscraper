#include <bits/stdc++.h>
using namespace std ; 

const int MAXN = 1e6 + 100 ; 

int a[MAXN] ; 
bool res[MAXN] ; 


ifstream fin ("in.txt") ; 
ofstream fout ("out.txt") ; 
int32_t main(){

	ios_base::sync_with_stdio(0) ; 
	fin . tie(0) ; fout . tie(0) ;

	int t ; fin >> t ; 
	for(int _ = 0 ; _ < t ; _ ++){
		int sz = 0 , ptr = 0 ; 
		string s ; fin >> s ; 
		int n = s . size() , m ;  fin >> m ; 
		for(int i = 0 ; i < n ; i ++){
			bool temp = (s[i] == '+') ; 
			if(ptr != sz && a[ptr] == i - m) ptr ++ ;  
			if((sz - ptr + temp + 1) % 2 && i < n - m + 1)a[sz ++] = i ; 
			res[i] = ((sz - ptr + temp) & 1) ; 
		}
		bool final = true ;
		for(int i = 0 ; i < n ; i ++) final = final & res[i] ; 
		if(final)	fout << "Case #" << _ + 1 << ':' << ' ' << sz << '\n' ; 
		else 		fout << "Case #" << _ + 1 << ':' << ' ' << "IMPOSSIBLE\n" ; 
	}

}	