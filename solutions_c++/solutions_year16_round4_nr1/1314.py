#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <numeric>
#include <array>
#include <map>
#include <set>
#include <stack>
#include <unordered_map>
#include <functional>
#include <iostream>
#include <thread>
#include <sstream>
#include <atomic>

using namespace std;


string St[13][3];


void GO() {
	St[0][0]="P";
	St[0][1]="R";
	St[0][2]="S";
	for (int n=1; n<13; n++){
		for (int i=0; i<3; i++) St[n][i] = (St[n-1][i]<St[n-1][(i+1)%3]) ? St[n-1][i] + St[n-1][(i+1)%3] : St[n-1][(i+1)%3] + St[n-1][i];
	}
}


int main () {
	GO();
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int N;
		int R, P, S;
		scanf("%d%d%d%d", &N, &R, &P, &S);
		bool ok=true;
		for (int i=0; i<N; i++) {
			int a=P+R-S;
			int b=R+S-P;
			int c=S+P-R;
			if (a<0 || b<0 || c<0) {
				ok=false;
				break;
			}
			P=a/2;
			R=b/2;
			S=c/2;
		}
		if (!ok) printf("Case #%d: %s\n", t, "IMPOSSIBLE");
		else if (P==1) printf("Case #%d: %s\n", t, St[N][0].c_str());
		else if (R==1) printf("Case #%d: %s\n", t, St[N][1].c_str());
		else if (S==1) printf("Case #%d: %s\n", t, St[N][2].c_str());
	}
	return 0;
}
