#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <fstream>
using namespace std;

string r = "RPS";
string mem[3][15];
string solve(string w, int L){
	int id = r.find(w[0]);
	if(L == 0)return w;
	if(mem[id][L] != "")return mem[id][L];
	string A = "" , B = "";
	if(w == "S"){
		A = solve("P", L-1);
		B = solve("S", L-1);
	} else if(w == "P"){
		A = solve("P", L-1);
		B = solve("R", L-1);
	} else if(w == "R"){
		A = solve("S", L-1);
		B = solve("R", L-1);
	}
	return mem[id][L] = min(A+B, B+A);
}

int check(string s, int R, int P, int S){
	for(int i = 0; i < s.size(); ++i){
		if(s[i] == 'R')R--;
		if(s[i] == 'S')S--;
		if(s[i] == 'P')P--;
	}
	return R == 0 && P == 0 && S == 0;
}
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt","w",stdout);
	int TC;
	cin >> TC;
	for(int tc = 1 ; tc<=TC; ++tc){
		int N, R, P, S;
		cin >> N >> R >> P >> S;
		
		string M = "Z";
		string P1 = solve("R", N);
		if(check(P1,R,P,S)) M = min(M, P1);
		string P2 = solve("P", N);
		if(check(P2,R,P,S)) M = min(M, P2);
		string P3 = solve("S", N);
		if(check(P3,R,P,S)) M = min(M, P3);
		if(M == "Z"){
			M = "IMPOSSIBLE";
		}
		cout << "Case #" << tc << ": " << M << endl;
	}
	
}

/*

P
PR

R
RS
RSPS

PSRS
SR
R

 
*/
