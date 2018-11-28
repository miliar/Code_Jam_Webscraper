#include <iostream>
#include <vector>
#include <map>

using namespace std;

int process(vector< vector<int> > runs) {
	
	int ret;
	while(1) {
		
		int k = 0;
   		while(k < runs.size()){
   			if (runs[k].empty()){
   				runs.erase(runs.begin() + k);
   				continue;
   			}
   			k++;
   		}
   		if(runs.empty())
   			break;
		
		
		//get the min, minr, minc
		int min = 99999999, minr, minc;
		int r_runs = 0, c_runs = 0;
		bool rrun = true, crun = true;
		for(int i=0; i < runs.size(); i++){
			for(int j=0; j < runs[0].size(); j++){
				if(min > runs[i][j]) {
					min = runs[i][j];
					minr = i;
					minc = j;
				}
			}
		}
		//mow the rows
		for(int i=0; i < runs[minr].size(); i++) {
			if(runs[minr][i] == min) {
				r_runs++;
			}
		}
		if(r_runs != runs[minr].size()){
			rrun = false;
		}

		//mow the columns
		for(int i=0; i < runs.size(); i++) {
			if(runs[i][minc] == min){
				c_runs++;
			}
		}

		if(c_runs != runs.size()) {
			crun = false;
		}

		if(!crun && !rrun) {
			return -1;
		}

		if(crun) {
			for(int i=0; i < runs.size(); i++) {
				runs[i].erase(runs[i].begin() + minc);
			}
			continue;
		} else if(rrun) {
			runs.erase(runs.begin() + minr);
			continue;
		}
		if(runs.size() != 0) continue;
		ret = runs.size();
	}
	return ret;
}

int main() {
	int T, N, M, cases = 0;
	scanf("%d", &T);
	vector< vector<int> > runs;
	vector<int> rows;
	while(T--) {
		cases++;
		runs.clear();
		scanf("%d %d", &N, &M);
		for(int i=0; i < N; i++) {
			int a;
			rows.clear();
			for(int j=0; j < M; j++) {
				scanf("%d", &a);
				rows.push_back(a);
			}
			runs.push_back(rows);
		}
		int ret = process(runs);
		printf("Case #%d: ", cases);
		if(ret == -1) {
			printf("NO\n");
		} else {
			printf("YES\n");
		}
		
	}
	return 0;
}