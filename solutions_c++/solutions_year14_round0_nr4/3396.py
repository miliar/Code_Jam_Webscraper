#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 0; t<T; ++t) {
		int n;
		scanf("%d", &n);
		vector<double> v,w;
		for (int i = 0; i<n; ++i) {
			double x;
			scanf("%lf", &x);
			v.push_back(x);
		}
		for (int i = 0; i<n; ++i) {
			double x;
			scanf("%lf", &x);
			w.push_back(x);
		}
		sort(v.begin(),v.end());
		sort(w.begin(),w.end());
		int poc = 0;
		int i = n-1, j = n-1;
		while (i >= 0 && j >= 0) {
			while (v[i] < w[j] && j >= 0) j--;
			if (j >= 0 && v[i] > w[j]) poc++;
			i--;
			j--;
		}
		printf("Case #%d: %d ", t+1,poc);
		int vys = 0;
		set<double> s(w.begin(),w.end());
		for (int i = 0; i<n; ++i) {
			set<double>::iterator low;
			low = s.lower_bound(v[i]);
			if (low != s.end()) {
				s.erase(low);
			} else {
				s.erase(s.begin());	
				vys++;
			}
		}
		printf("%d\n", vys);
	}
	return 0;
}
