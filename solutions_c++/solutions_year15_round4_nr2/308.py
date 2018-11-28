#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int T;

  cin >> T;

  for (int t=1;t<=T;t++) {
		int N;
		double V, X;
    cin >> N >> V >> X;

		double R = 0;
		vector<pair<double, double> > hot, cold;
    for (int i=0;i<N;i++) {
			pair<double, double> opt;
			cin >> opt.first >> opt.second;

			if (opt.second == X) R+=opt.first;
			else if (opt.second > X) hot.push_back(opt);
			else cold.push_back(opt);
    }

		sort(hot.begin(),hot.end());
		sort(cold.begin(),cold.end());
		reverse(cold.begin(),cold.end());

		if ((cold.empty() || hot.empty()) && R == 0) {printf("Case #%d: IMPOSSIBLE\n",t); continue;}

		int h = 0;
		double hv = 0, cv = 0;

		for (int c=0;c<cold.size() && h<hot.size();c++) {
			double p = cold[c].first * (X - cold[c].second);

			while (p > 0 && h < hot.size()) {
				double hp = (hot[h].first-hv) * (hot[h].second - X);
				if (hp > p) {
					hv += p/(hot[h].second - X);
					p = 0;
				}
				else {
					p -= hp;
					R += hot[h].first;
					hv = 0;
					h++;
				}
			}
			R += cold[c].first - p/(X-cold[c].second);
		}
		R += hv;

		printf("Case #%d: %.9lf\n",t,V/R);
		
  }

}
