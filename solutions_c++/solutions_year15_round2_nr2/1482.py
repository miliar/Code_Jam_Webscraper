#include <fstream>
#include <cassert>
#include <climits>
using namespace std;

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

int calcUnhappiness(const bool a[], int R, int C, int n) {
	int cur_count=0;
	for (int i=0; i<R; i++) {
		for (int j=0; j<C; j++) {
			if (a[i*C+j]) {
				for (int k=0; k<4; k++) {
					int x = i+dx[k];
					int y = j+dy[k];
					if (x>=0 && x<R && y>=0 && y<C && a[x*C+y]) 
						cur_count++;
				}
			}
		}
	}
	return cur_count/2;
}

int getans(int R, int C, int n) {
	int m = R*C;
	bool a[m];
	fill_n(a, m, false);
	fill_n(a, n, true);
	int ans = INT_MAX;
	do {
		int cur_ans = calcUnhappiness(a, R, C, n);
		ans = min(ans, cur_ans);
		int k=m-1;
		while (k>=0 && a[k]) k--;
		int j = m-1-k;
		if (j == n) break;
		fill(a+(k+1), a+m, false);
		while (k>=0 && !a[k]) k--;
		a[k]=false;
		fill_n(a+(k+1), j+1, true);
	} while(true);
	return ans;
}

int main(){
	ifstream fin("B-small-attempt0.in");
	ofstream fout("pb-small.out");
	assert(fin && fout);
	int test;
	fin >> test;
	for (int count=1; count<=test; count++) {
		int R, C;
		int n;
		fin >> R >> C >> n;
		fout << "Case #" << count << ": " << getans(R, C, n) << endl;
	}
	fin.close();
	fout.close();
	return 0;
}