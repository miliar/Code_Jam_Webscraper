#include <iostream>
#include <string>
using namespace std;

int primo[20];
int secondo[20];
int terzo[20];

string rps[20];
string rsp[20];
string psr[20];
string prs[20];
string spr[20];
string srp[20];

void init(){
	primo[0] = 1; secondo[0] = 0; terzo[0] = 0;
	for(int i=1; i<13; i++){
		primo[i] = primo[i-1] + terzo[i-1];
		secondo[i] = secondo[i-1] + primo[i-1];
		terzo[i] = terzo[i-1] + secondo[i-1];
	}
	
	rps[0] = "R"; rsp[0] = "R";
	psr[0] = "P"; prs[0] = "P";
	spr[0] = "S"; srp[0] = "S";
	for(int i=1; i<13; i++){
		rps[i] = min(rps[i-1] + psr[i-1], psr[i-1] + rps[i-1]);
		rsp[i] = min(rsp[i-1] + spr[i-1], spr[i-1] + rsp[i-1]);
		
		psr[i] = min(psr[i-1] + srp[i-1], srp[i-1] + psr[i-1]);
		prs[i] = min(prs[i-1] + rsp[i-1], rsp[i-1] + prs[i-1]);
		
		spr[i] = min(spr[i-1] + prs[i-1], prs[i-1] + spr[i-1]);
		srp[i] = min(srp[i-1] + rps[i-1], rps[i-1] + srp[i-1]);
	}
}

struct test_case{
	int n, r, p, s;
	
	
	void solve(){
		cin >> n >> r >> p >> s;
		//~ cout << r << ' ' << p << ' ' << s << "     " << primo[n] << ' ' << secondo[n] << ' ' << terzo[n] << '\t';
		string ans = "Z";
		if(primo[n] == r && secondo[n] == p && terzo[n] == s) ans = min(ans, rps[n]);
		if(primo[n] == r && secondo[n] == s && terzo[n] == p) ans = min(ans, rsp[n]);
		if(primo[n] == s && secondo[n] == p && terzo[n] == r) ans = min(ans, spr[n]);
		if(primo[n] == s && secondo[n] == r && terzo[n] == p) ans = min(ans, srp[n]);
		if(primo[n] == p && secondo[n] == r && terzo[n] == s) ans = min(ans, prs[n]);
		if(primo[n] == p && secondo[n] == s && terzo[n] == r) ans = min(ans, psr[n]);
		if(ans == "Z") ans = "IMPOSSIBLE";
		cout << ans;
	}
};

int main(){
	init();
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		cout << "Case #" << i << ": ";
		test_case s = {};
		s.solve();
		cout << endl;
	}
	return 0;
}
