#include <stdio.h>
#include <vector>
#include <algorithm>


int saiki(int j, std::vector<bool>& b, std::vector<std::vector<int> >& r)
{
	int res = 0;
	for (int i=0; i<(int)r[j].size(); i++) {
		if (b[r[j][i]]) {
			continue;
		}
		res = std::max(res, saiki(r[j][i], b, r));
	}
	return res + 1;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int n;
		scanf("%d", &n);
		std::vector<int> v;
		std::vector<bool> b;
		std::vector<std::vector<int> > r;
		for (int i=0; i<n; i++) {
			r.push_back(std::vector<int>());
		}
		for (int i=0; i<n; i++) {
			int a;
			scanf("%d", &a);
			v.push_back(a-1);
			b.push_back(false);
			r[a-1].push_back(i);
		}
		std::vector<std::vector<int> > p;
		//int res = 0;
		for (int i=0; i<n; i++) {
			if (b[i]) {
				continue;
			}
			std::vector<int> seq;
			int num = 0;
			int cur = i;
			while (true) {
				b[cur] = true;
				seq.push_back(cur);
				int next = v[cur];
				if (b[next]) {
					int nth = 0;
					int j = 0;
					for (; j<(int)seq.size(); j++) {
						if (seq[j] == next) {
							break;
						}
					}
					if (j < seq.size()) {
						//res = std::max(res, (int)(seq.size() - j));
						std::vector<int> cir;
						for (int k=j; k<seq.size(); k++) {
							cir.push_back(seq[k]);
						}
						p.push_back(cir);
						/*
						if ((int) seq.size() - j == 2) {
							std::vector<int> pair;
							pair.push_back(cur);
							pair.push_back(next);
							p.push_back(pair);
						}*/
					}
					break;
				}
				cur = next;
			}
		}
		int cir = 0;
		std::vector<int> pr;
		for (int i=0; i<(int)p.size(); i++) {
			cir = std::max(cir, (int)p[i].size());
			if (p[i].size() != 2) {
				continue;
			} 
			for (int k=0; k<(int)b.size(); k++) {
				b[k] = false;
			}
			for (int j=0; j<(int)p[i].size(); j++) {
				b[p[i][j]] = true;			
			}
			int rres = 0;
			for (int j=0; j<(int)p[i].size(); j++) {
				int l = saiki(p[i][j], b, r);
				rres += l;
				//rres = std::max(rres, l + (int)p[i].size() - 1);
			}
			pr.push_back(rres);
		}
		int rres = 0;
		for (int i=0; i<(int)pr.size(); i++) {
			rres += pr[i];
		}
		int res = 0;
		res = std::max(rres, cir);
		/*
		if (pr.size() == 1) {
			rres = pr[0];
		} else if (pr.size() >= 2) {
			std::sort(pr.begin(), pr.end());
			rres = pr[pr.size()-1] + pr[pr.size()-2];
		}*/
		//res = std::max(rres, res);
		/*
		if (pr2.size() > 0) {
			std::sort(pr2.begin(), pr2.end());
			res = std::max(res, pr2[0]);
		}*/
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}