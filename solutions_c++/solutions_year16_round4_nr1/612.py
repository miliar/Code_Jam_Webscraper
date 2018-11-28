#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;

int P, R, S;

string ans;
string x[3];

void Do(int n,int p,int r,int s){
	if(n == 0){
		if(p)printf("%s\n", x[0].c_str());
		if(r)printf("%s\n", x[1].c_str());
		if(s)printf("%s\n", x[2].c_str());
		return;
	}
	
	string t[3];
	if(x[0] > x[1])t[0] = x[1] + x[0];
	else t[0] = x[0] + x[1];
	if(x[1] > x[2])t[1] = x[2] + x[1];
	else t[1] = x[1] + x[2];
	if(x[2] > x[0])t[2] = x[0] + x[2];
	else t[2] = x[2] + x[0];
	for(int i=0;i<3;i++)x[i] = t[i];
	int tp = (r+p-s)/2;
	int ts = (s+p-r)/2;
	int tr = (r+s-p)/2;
	Do(n-1, tp, tr, ts);
}

void solve(int tc){
	printf("Case #%d: ", tc);
	int n, r, p, s;
	scanf("%d%d%d%d", &n, &r, &p, &s);
	P = p; R = r; S = s;
	for(int i=1;i<=n;i++){
		int tp = (r+p-s)/2;
		int ts = (s+p-r)/2;
		int tr = (r+s-p)/2;
		if(tp < 0 || ts < 0 || tr < 0){
			printf("IMPOSSIBLE\n");
			return;
		}
		p = tp, r = tr, s = ts;
	}
	x[0] = "P";
	x[1] = "R";
	x[2] = "S";
	Do(n, P, R, S);
}

int main() {
	int Tc; scanf("%d", &Tc);
	for(int tc=1;tc<=Tc;tc++){
		solve(tc);
	}
	return 0;
}