#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> in[2];

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++){
		int n;
		scanf("%d", &n);
		for (int i = 0; i < 2; i++){
			for (int j = 0; j < n; j++){
				double t1; scanf("%lf", &t1);
				in[i].push_back((int)(t1 * 10000000));
			}
			sort(in[i].begin(), in[i].end());
		}
		
		int a = 0, b = 0;
		int ii = -1, jj = n - 1, kk = n - 1;
		while (ii < jj && jj>-1 && kk>-1){
			if (in[0][jj]>in[1][kk]) {
				a++; jj--; kk--;
			}
			else{
				ii++; kk--;
			}
		}

		for (int i = 0; i < n; i++){
			vector<int>::iterator it = lower_bound(in[1].begin(), in[1].end(), in[0][i]);
			if (it != in[1].end()) {
				b++;
				in[1].erase(it);
			}
			else break;
		}
		b = n - b;

		printf("Case #%d: %d %d\n",tt,a,b);
		
		in[0].clear();
		in[1].clear();
	}
}