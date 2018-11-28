#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int R, C;
int cnt;
char grid[10][10];

inline bool val(int i, int j) {
	char c = 0;
	char n = grid[i][j];
	if (i>0&&grid[i-1][j] == n) c++;
	if (i+1<R&&grid[i+1][j] == n) c++;
	if (j+1==C) {
		if (grid[i][0] == n) c++;
	}
	else {
//printf("gridij+1:%d %d %d\n",i,j+1,grid[i][j+1]);
		if (grid[i][j+1] == n) c++;
	}
	if (j==0) {
		if (grid[i][C-1] == n) c++;
	}
	else {
		if (grid[i][j-1] == n) c++;
	}
	return (c==n);
}
inline bool valid (int i, int j, bool inte=true) {
	if (j<0) return true;
	if (i<0) return true;
	char c = 0;
	char n = grid[i][j];
	if (i>0&&grid[i-1][j] == n) c++;
	if (i+1<R&&grid[i+1][j] == n) c++;
	if (inte && grid[i][j+1] == n) c++;
	if (j==0) {
		return (c <= n);
	}
	else {
		if (grid[i][j-1] == n) c++;
	}
	if (inte) return (n==c);
	else return (c <= n);
}
set<long long> done;
//long long hash;
long long p3[40];

unsigned long long hsh(int k) {
	long long h = 0;
	int n = 0;
	for (int i=0;i<R;i++) {
		for (int j=k;j<C+k;j++) {
			h += p3[n++]*(grid[i][j%C]-1);
		}
	}
	return h;
}
long long hash() {
	unsigned long long h = -1;
	for (int k=0;k<C;k++) h = min(h,hsh(k));
	return h;
}

void g(int i, int j) {
	//long long hsh = hash;
	for (int x=1;x<=3;x++) {
		//long long h = p3[i*6+j];
		//hash = hsh + h*(x-1);
		grid[i][j] = x;
		if (!valid(i,j-1)) continue;
		if (!valid(i-1,j,false)) continue;
		if (i==R-1) {
			if (j==C-1) {
				bool bad = false;
				for (int k=0;k<R;k++) {
					if (!val(k,C-1)) {bad=true;break;}
					if (!val(k,0)) {bad=true;break;}
				}
				if (bad) continue;
//printf("val:\n");
//val(0,0);
//for (int i=0;i<R;i++) {
//	for (int j=0;j<C;j++) {
//		cout << (int)grid[i][j];
//	}
//	cout << endl;
//}
//	cout << endl;
				int h = hash();
				if (done.count(h)) return;
				done.insert(h);
				cnt++;

				//hash = hsh;
				return;
			}
			else g(0,j+1);
		}
		else g(i+1,j);
	}
	//hash = hsh;
}

int main() {
	p3[0] = 1;
	for (int i=1;i<38;i++) {
		p3[i] = p3[i-1]*3;
	}
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
		done.clear();
    cin >> R >> C;
		cnt = 0;
		//hash = 0;
		g(0,0);

		printf("Case #%d: %d\n",t,cnt);
		
  }

}
