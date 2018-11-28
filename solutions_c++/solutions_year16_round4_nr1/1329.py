#include <bits/stdc++.h>

#define REP(i, n) for(int i = 0; i < n; i++)
#define mp make_pair

#define X first
#define Y second

using namespace std;

typedef pair<int, int> ii;
typedef long long ll;

string trz(int t, int n){
	if(n == 0){
		if(t == 0)return "PR"; // P
		if(t==1)return "PS"; // S
		if(t==2)return "RS"; // R
	} else{
		string a, b;
		switch(t){
			case 0: a = trz(0, n-1);
					b = trz(2, n-1);
					break;
			case 1: a = trz(0, n-1);
					b = trz(1, n-1);
					break;
			case 2: a = trz(1, n-1);
					b = trz(2, n-1);
					break;
		}
		if(a > b)swap(a, b);
		return a+b;
	}
	assert(false);
	return "";
}

bool ok(string st, int p, int r, int s){
	for(auto c : st){
		switch(c){
			case 'P': p--;break;
			case 'R': r--;break;
			case 'S': s--;break;
		}
	}
	return p == 0 && r == 0&&s == 0;
}

void testcase(int T){
	int n;
	int p, r, s;
	scanf("%d%d%d%d", &n, &r, &p, &s);

	string mn = "";
	REP(i, 3){
		string a = trz(i, n-1);
		if(ok(a, p, r, s)){
			if(mn.length() == 0 || mn > a)mn = a;
		}
	}

	if(mn.length() == 0)mn = "IMPOSSIBLE";
	cout << "Case #" << T << ": " << mn << endl;

}

int main(){
	int T;
	scanf("%d", &T);
	REP(i, T)testcase(i+1);


	return 0;
}
