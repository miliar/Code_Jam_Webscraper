#include <bits/stdc++.h>
#include <tr1/unordered_map>

using namespace std;
using namespace tr1;

string str;
int x, l, tam;
int grafo[8][8];
unordered_map < string, int > m;
int memo[3][10005][9];

int getNext( int at, int idx ){
	string aux = "";
	aux += str[idx];
	return grafo[at][m[aux]];
}

bool solve3( int at, int val ){
	if( at >= tam ) return memo[2][at][val] = (val == 3);
	if( memo[2][at][val] != -1 ) return memo[2][at][val];
	return memo[2][at][val] = solve3(at+1,getNext(val,at+1));
}

bool solve2( int at, int val ){
	bool ret = false;
	if( at >= tam-1 ) return memo[1][at][val] = false;
	if( memo[1][at][val] != -1 ) return memo[1][at][val];
	if( val == 2 ){
		string aux = "";
		aux += str[at+1];
		ret = solve3(at+1, m[aux]);
	}
	if( ret ) return memo[1][at][val] = true;
	return memo[1][at][val] = solve2(at+1,getNext(val,at+1));
}

bool solve1( int at, int val ){
	bool ret = false;
	if( at >= tam-2 ) return memo[0][at][val] = false;
	if( memo[0][at][val] != -1 ) return memo[0][at][val];
	if( val == 1 ){
		string aux = "";
		aux += str[at+1];
		ret = solve2(at+1, m[aux]);
	}
	if( ret ) return memo[0][at][val] = true;
	return memo[0][at][val] = solve1(at+1,getNext(val,at+1));
}

void buildGraph(){
	for( int i = 0; i < 8; i++ ) grafo[i][0] = grafo[0][i] = i;
	
	m["1"] = 0; m["i"] = 1; m["j"] = 2; m["k"] = 3; m["-1"] = 4; m["-i"] = 5; m["-j"] = 6; m["-k"] = 7;
	grafo[m["i"]][m["i"]] = m["-1"]; 
	grafo[m["i"]][m["j"]] = m["k"];
	grafo[m["i"]][m["k"]] = m["-j"];
	grafo[m["i"]][m["-1"]] = m["-i"];
	grafo[m["i"]][m["-i"]] = m["1"];
	grafo[m["i"]][m["-j"]] = m["-k"];
	grafo[m["i"]][m["-k"]] = m["j"];

	grafo[m["j"]][m["i"]] = m["-k"]; 
	grafo[m["j"]][m["j"]] = m["-1"];
	grafo[m["j"]][m["k"]] = m["i"];
	grafo[m["j"]][m["-1"]] = m["-j"];
	grafo[m["j"]][m["-i"]] = m["k"];
	grafo[m["j"]][m["-j"]] = m["1"];
	grafo[m["j"]][m["-k"]] = m["-i"];

	grafo[m["k"]][m["i"]] = m["j"]; 
	grafo[m["k"]][m["j"]] = m["-i"];
	grafo[m["k"]][m["k"]] = m["-1"];
	grafo[m["k"]][m["-1"]] = m["-k"];
	grafo[m["k"]][m["-i"]] = m["-j"];
	grafo[m["k"]][m["-j"]] = m["i"];
	grafo[m["k"]][m["-k"]] = m["1"];

	grafo[m["-1"]][m["i"]] = m["-i"]; 
	grafo[m["-1"]][m["j"]] = m["-j"];
	grafo[m["-1"]][m["k"]] = m["-k"];
	grafo[m["-1"]][m["-1"]] = m["1"];
	grafo[m["-1"]][m["-i"]] = m["i"];
	grafo[m["-1"]][m["-j"]] = m["j"];
	grafo[m["-1"]][m["-k"]] = m["k"];

	grafo[m["-i"]][m["i"]] = m["1"]; 
	grafo[m["-i"]][m["j"]] = m["-k"];
	grafo[m["-i"]][m["k"]] = m["j"];
	grafo[m["-i"]][m["-1"]] = m["i"];
	grafo[m["-i"]][m["-i"]] = m["-i"];
	grafo[m["-i"]][m["-j"]] = m["k"];
	grafo[m["-i"]][m["-k"]] = m["-j"];

	grafo[m["-j"]][m["i"]] = m["k"]; 
	grafo[m["-j"]][m["j"]] = m["1"];
	grafo[m["-j"]][m["k"]] = m["-i"];
	grafo[m["-j"]][m["-1"]] = m["j"];
	grafo[m["-j"]][m["-i"]] = m["-k"];
	grafo[m["-j"]][m["-j"]] = m["-1"];
	grafo[m["-j"]][m["-k"]] = m["i"];

	grafo[m["-k"]][m["i"]] = m["-j"]; 
	grafo[m["-k"]][m["j"]] = m["i"];
	grafo[m["-k"]][m["k"]] = m["1"];
	grafo[m["-k"]][m["-1"]] = m["k"];
	grafo[m["-k"]][m["-i"]] = m["j"];
	grafo[m["-k"]][m["-j"]] = m["-i"];
	grafo[m["-k"]][m["-k"]] = m["-1"];
}

int main(){
	ios::sync_with_stdio(false);
	int t, k = 1;
	string aux;
	cin >> t;
	buildGraph();
	string ans[] = {"NO","YES"};
	while( t-- ){
		cin >> x >> l;
		cin >> aux;
		str = "";
		for( int i = 0; i < l; i++ ) str += aux;
		tam = str.size();
		aux = "";
		aux += str[0];
		memset(memo,-1,sizeof(memo));
		cout <<  "Case #" << k++ << ": " << ans[solve1(0,m[aux])] << '\n';
	}
	return 0;
}