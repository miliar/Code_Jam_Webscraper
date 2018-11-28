#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

int V, X;
int n, R[100], C[100];

char buf[128];

int get_num() {
	scanf("%s", buf);
	int ret = 0;
	for(int i = 0;buf[i] != '\0';i ++) {
		if(buf[i] == '.') continue;
		ret = ret*10 + buf[i]-'0';
	}
	return ret;
}

void input() {
	scanf("%d", &n);
	V = get_num();
	X = get_num();
	for(int i = 0;i < n;i ++) {
		R[i] = get_num();
		C[i] = get_num();
	}
}

void solve() {
	int L = 0, S = 0, E = 0;
	double SX = 0, SY = 0;
	double LX = 0, LY = 0;
	double EX = 0;

	for(int i = 0;i < n;i ++) {
		if(C[i] > X) {
			L = 1;
			LX += R[i];
			LY += double(R[i])*double(C[i]);
		}
		else if(C[i] < X) {
			S = 1;
			SX += R[i];
			SY += double(R[i])*double(C[i]);
		}
		else {
			E = 1;
			EX += R[i];
		}
	}

	if(E == 0&&(L == 0||S == 0)) {
		printf("IMPOSSIBLE\n"); 
		return ;
	}

	double t1 = 0;
	if(L > 0&&S > 0) {
		double x = V*(SY - X*SX)/(LX*SY-LY*SX);
		double y = V*(LY - X*LX)/(SX*LY-LX*SY);
		t1 = x;
		if(y > t1) t1 = y;
	}

	double t2 = 0;
	if(E == 1) t2 = V/EX;

	double ret = 0;
	if(L > 0&&S > 0&&E > 0) ret = 1/(1/t1+1/t2);
	else if(E > 0) ret = t2;
	else ret = t1;
	
	printf("%.10lf\n", ret);
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Case;
	scanf("%d", &Case);
	for(int cas = 1;cas <= Case;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
}