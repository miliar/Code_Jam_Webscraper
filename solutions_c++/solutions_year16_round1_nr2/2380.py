#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

vvi lists;
int bd[50][50];
int T;
int N;
bitset<100> used;

int il,isrowl;

bool add(bool isrow,int i,int j) {
	for (int c=0;c<N;c++) {
		int a=i,b=c;
		if (!isrow) swap(a,b);
		if (bd[a][b]!=-1 && bd[a][b]!=lists[j][c])
			return 0;
		bd[a][b]=lists[j][c];
	}
	return 1;
}

void rem(bool isrow,int i,int j) {
	for (int c=i;c<N;c++) {
		int a=i,b=c;
		if (!isrow) swap(a,b);
		bd[a][b]=-1;
	}
	if (il!=-1 && isrowl!=isrow) {
		int a=i,b=il;
		if (!isrow) swap(a,b);
		bd[a][b]=-1;
	}
}

bool solve(int i,bool canleave) {
	if (i==N) return 1;
	for (int c=0;c<2*N-1;c++) if (!used[c]) {
		for (int d=0;d<2*N-1;d++) if (!used[d] && c!=d) {
			used[c]=1;
			used[d]=1;
			if (add(0,i,c) && add(1,i,d)) {
				if (solve(i+1,canleave)) return 1;
			}
			rem(0,i,c);
			rem(1,i,d);
			used[c]=used[d]=0;
		}

		if (canleave) {
			used[c]=1;
			il=i;isrowl=1;
			if (add(0,i,c) && solve(i+1,0)) return 1;
			il=-1;
			rem(0,i,c);
			isrowl=0;il=i;
			if (add(1,i,c) && solve(i+1,0)) return 1;
			il=-1;
			rem(1,i,c);
			used[c]=0;
		}
	}
	return 0;
}



int main() {
	cin >> T;
	for (int cas=1;cas<=T;cas++) {
		cin >> N;
		lists.clear();
		lists.resize(2*N-1);
		used.reset();
		for (int c=0;c<2*N-1;c++) for (int d=0;d<N;d++) {
			int i;
			cin >> i;
			lists[c].push_back(i);
		}

		fill(bd[0],bd[50],-1);
		il=-1;
		assert(solve(0,1));
		printf("Case #%d:",cas);
		for (int c=0;c<N;c++) {
			int a=il,b=c;
			if (!isrowl) swap(a,b);
			cout << ' ' << bd[a][b];
		}
		cout << endl;
	}
}
