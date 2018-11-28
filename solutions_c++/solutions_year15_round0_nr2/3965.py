#include <cstdlib>
#include <vector>
#include <cstdio>
#include <iostream>
#include <stack>
#include <utility>
#include <algorithm>

using namespace std;

int max(vector<int> x) {
	int max=0;
	for (auto i:x) {
		if (i>max) max=i;
	}
	return max;
}

int main(int argc, char** argv) {
	int T;
	cin >> T;
	vector <int> res (T,0);
	vector<int> d (T,0);
	vector<vector<int> > p;//(n,vector<int>(d[n],0));
	for (int n=0;n<T;n++) {
		cin >> d[n];
		p.push_back(vector<int>(d[n],0));
		for (int i=0;i<d[n];i++) {
			cin >> p[n][i];
		}
	}
#pragma omp parallel for
	for (int n=0;n<T;n++) {
		stack<pair<int,vector<int> > > s;
		s.push(pair<int,vector<int> >(0,p[n]));
		int min = max(p[n])+0;
		while (!s.empty()) {
			auto x = s.top();
			s.pop();
			if (max(x.second)+x.first < min) {
				min = max(x.second)+x.first;
			}
			//auto xs = x.second;
			sort(x.second.begin(),x.second.end(),greater<int>());
			//x.second = xs;
			//cerr << "  "; for (auto i:x.second) cerr << i << " "; cerr <<"\n";
			//for (auto i:x.second) cerr << i << " "; cerr <<"\n";

			//auto x_ = x;
			//for (int i=0;i<x.second.size();i++) {
			//int i=0;
				for (int k=1;k<x.second[0]/2+1;k++) {
				auto xx = x;
				for (int i=0;i<x.second.size();i++) {
					xx.second[i]-=k;
					xx.second.push_back(k);
					xx.first++;
					//cerr << xx.first << " : "; for (auto i:xx.second) cerr << i << " "; cerr <<"\n";
					if (x.second[i]!=x.second[i+1]) break;
				}
				s.push(xx);
				}
			//}
		}
		//printf("Case #%d: %d\n",n+1,min);
		res[n]=min;
		//cerr << n+1 << "\n";
	}
	for (int n=0;n<T;n++) {
		printf("Case #%d: %d\n",n+1,res[n]);
	}

	return 0;
}

