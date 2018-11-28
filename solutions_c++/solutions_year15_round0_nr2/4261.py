#include <iostream>
#include <vector>
#include <queue>
#include <limits.h>

using namespace std;

int max_pancakes(vector<int>& P, int &i_max){
	int max = -1;
	for(int i = 0; i < P.size(); ++i){
		if(P[i] > max){
			max = P[i];
			i_max = i;
		}
	}
	return max;
}

int not_so_fast_fliping(vector<int>& p){
	int global_i_max, max_P,t,best_so_far;
	max_P = best_so_far = max_pancakes(p, global_i_max);
	for(int r = 1; r < max_P; ++r){
		int t = 0, best_t = max_P, max = max_P, i_max = global_i_max;
		vector<int> P(p.size());
		copy(p.begin(), p.end(), P.begin());
		for(int i = 0; i < best_t; ++i){
			if(r >= max){
				best_t = t + max;
				break;
			}
			t++;
			P.push_back(r);
			if(P[i_max] < r){
				P[i_max] = 0;
			}else{
				P[i_max] -= r;
			}
			max = max_pancakes(P, i_max);
			if(max + t < best_t){
				best_t = max + t;
			}
		}
		if(best_t < best_so_far){
			//cout << "best r: " << r << endl;
			best_so_far = best_t;
		}
	}
	return best_so_far;
}

int fast_fliping(vector<int>& p){
	int global_i_max, max_P,t,best_so_far;
	max_P = best_so_far = max_pancakes(p, global_i_max);
	for(int r = 1; r < max_P ; ++r){
		int t = 0, best_t = max_P, max = max_P, i_max = global_i_max;
		priority_queue<int> P(p.begin(), p.end());
		//copy(p.begin(), p.end(), P.begin());
		for(int i = 0; i < best_t; ++i){
			max = P.top();
			P.pop();
			if(r >= max){
				best_t = t + max;
				break;
			}
			t++;
			P.push(r);
			P.push(max - r);
			if(max + t < best_t){
				best_t = max + t;
			}
		}
		if(best_t < best_so_far){
			best_so_far = best_t;
		}
	}
	return best_so_far;
}


int main(){
	int T, D;
	cin >> T;
	for(int c = 1; c <= T; ++c){
		cin >> D;
		vector<int> P;
		for(int j = 0; j < D; ++j){
			int p;
			cin >> p;
			P.push_back(p);
		}

		//cout << "Case #" << c << ": " << not_so_fast_fliping(P) << endl;
		cout << "Case #" << c << ": " << fast_fliping(P) << endl;
	}
	return 0;
}
