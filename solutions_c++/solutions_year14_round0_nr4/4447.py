#include <cstdio>
#include <iostream>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;


void solve(int c) {
	set<double> naomi;
	set<double> ken;
	
	int s_war = 0, s_d_war = 0;
	
	int N;
	cin >> N;
	s_war = N;
	s_d_war = N;
	
	for(int i = 0; i < N; ++i) {
		double tmp;
		scanf("%lf", &tmp);
		naomi.insert(tmp);
	}
	
	for(int i = 0; i < N; ++i) {
		double tmp;
		scanf("%lf", &tmp);
		ken.insert(tmp);
	}
	
	set<double>::iterator n_pt = naomi.begin();
	set<double>::iterator k_pt = ken.begin();
	
	while(n_pt != naomi.end() and
		  k_pt != ken.end()) {
		double n_val = *n_pt;
		double k_val = *k_pt;
		
		if(n_val > k_val) {
			k_pt++;
		}
		else {
			s_war--;
			n_pt++;
			k_pt++;
		}
	}
	
	n_pt = naomi.begin();
	k_pt = ken.begin();
	
	while(n_pt != naomi.end() and
		  k_pt != ken.end()) {
		double n_val = *n_pt;
		double k_val = *k_pt;
		
		if(k_val > n_val) {
			s_d_war--;
			n_pt++;
		} else {
			n_pt++;
			k_pt++;
		}
	}
	
	printf("Case #%d: %d %d\n", c+1, s_d_war, s_war);
}
int main() {
	int T;
	cin >> T;
	for(int c = 0; c < T; ++c)
		solve(c);
	return 0;
}