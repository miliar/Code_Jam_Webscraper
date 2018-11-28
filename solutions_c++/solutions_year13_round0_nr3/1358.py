#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string>
#include<iostream>

using namespace std;

#define NAME "C-large-1"

int T, nm ;
long long A, B;
long long m[10000];


int fair(long long square){
	string s, ss;
	char tmp[25];
	tmp[0] = 0;
	sprintf (tmp, "%I64d", square);
	s = string(tmp);
	ss = s;
	reverse (ss.begin(), ss.end());
	if (s == ss){
		return 1;
	}
	else 
		return 0;
}

int main(){
	freopen(NAME".in", "r", stdin);
	freopen(NAME".out", "w", stdout);
	nm = 0;
	for(long long i = 1; i < (int)1e7; i++){
		long long square = i * i;
		if (fair(square) && fair(i)){
			m[nm++] = square;
		}
	}
	m[nm] = (long long)1e14;
	for (int i = 0; i < nm; i++){
		cout << m[i] << endl;
	}
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		cin >> A >> B;
		cout << "Case #" << t << ": " <<  lower_bound(m, m + nm, B+1) - lower_bound(m, m + nm, A) << endl;	
	}
	return 0;
}