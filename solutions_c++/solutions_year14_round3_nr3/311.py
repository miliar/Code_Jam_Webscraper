#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

// count number of bits:
 int nr(int i) {
  i = i - ((i >> 1) & 0x55555555);
  i = (i & 0x33333333) + ((i >> 2) & 0x33333333);
  return (((i + (i >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24;
 }

bool check(int st[20][20], int N, int M, int K) {
	// flood from each edge:
	bool trig = true;
	while (trig) {
		trig = false;
		for (int n=0; n<N; n++)
			for (int m=0; m<M; m++) {
				if (st[n][m]!=0) continue;
				if ((m==0 || m==M-1)/* && n!=0 && n!=N-1*/) // if edge
					if (st[n][m]==0) {
						st[n][m]=2;
						trig = true;
						continue;
					}
				if ((n==0 || n==N-1)/* && m!=0 && m!=M-1*/) // if edge
					if (st[n][m]==0) {
						st[n][m]=2;
						trig = true;
						continue;
					}
				if (st[max(0,min(N-1,n+1))][max(0,min(M-1,m))]==2 ||
					st[max(0,min(N-1,n-1))][max(0,min(M-1,m))]==2 ||
					st[max(0,min(N-1,n))][max(0,min(M-1,m+1))]==2 ||
					st[max(0,min(N-1,n))][max(0,min(M-1,m-1))]==2) {
						st[n][m]=2;
						trig = true;
						continue;
				}
			}
	}
	int ans=0, ans1=0;
	for (int n=0; n<N; n++)
		for (int m=0; m<M; m++) {
			if (st[n][m]!=2)
				ans++;
			if (st[n][m]==1)
				ans1++;
		}

	return (ans>=K);
}

int solve(int N, int M, int K) {
	int st[20][20];
	int mn=20;

	for (int i=0; i<(1<<N*M); i++) {
		for (int n=0; n<N; n++)
			for (int m=0; m<M; m++)
				if (i & 1 << n*M+m)
					st[n][m]=1;
				else
					st[n][m]=0;
		if (check(st,N,M,K))
			mn=min(nr(i),mn);
	}
    return mn;
}

int main() {
    freopen("C-small-attempt0.in", "rt", stdin);
    freopen("C-small.out", "wt", stdout);
//    freopen("C-large.in", "rt", stdin);
//    freopen("C-large.out", "wt", stdout);
//	freopen("test.in", "rt", stdin);
   
    int T;
    cin>>T;

    for (int i=1; i<=T; i++) {
        int N,M,K;
		cin >> N >> M >> K;
        cout << "Case #" << i << ": " << solve(N,M,K) << endl;
    }
}