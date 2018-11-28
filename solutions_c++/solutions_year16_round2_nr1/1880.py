#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>

#define pb push_back
#define ll long long
#define REP(a,b) for(int(a)=0;(a)<(b); (a)++)
using namespace std;

string s;
int cet[26];
void sniz(char c){
	cet[c-'A']--;
}
void ss(string g){
	REP(a,g.size()) cet[g[a]-'A']--;
}
void solve(int test){
	cin>>s;
	REP(a,26) cet[a] = 0;
	REP(a,s.size()) cet[s[a]-'A']++;
	vector<int> vys;
	while(cet['Z'-'A'] > 0){
		vys.pb(0);
		ss("ZERO");
	}
	while(cet['W'-'A'] > 0){
		vys.pb(2);
		sniz('T');
		sniz('W');
		sniz('O');
	}
	while(cet['X'-'A']> 0){
		vys.pb(6);
		sniz('S');
		sniz('I');
		sniz('X');
	}
	while(cet['G'-'A'] > 0){
		vys.pb(8);
		ss("EIGHT");
	}
	while(cet['T'-'A'] > 0){
		vys.pb(3);
		ss("THREE");
	}
	while(cet['U'-'A'] > 0){
		vys.pb(4);
		ss("FOUR");
	}
	while(cet['F'-'A'] > 0){
		vys.pb(5);
		ss("FIVE");
	}
	while(cet['S'-'A'] > 0){
		vys.pb(7);
		ss("SEVEN");
	}
	while(cet['I'-'A'] > 0){
		vys.pb(9);
		ss("NINE");
	}
	while(cet['O'-'A'] > 0){
		vys.pb(1);
		ss("ONE");
	}
	printf("Case #%i: ",test+1);
	sort(vys.begin(),vys.end());
	REP(a,vys.size()) printf("%i",vys[a]);
	printf("\n");
}

int main(){
	int t;
	scanf("%i",&t);
	REP(a,t) solve(a);
	return 0;
}
