#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

struct cube{
	bool naomi;
	double w;
};

bool comp(cube a, cube b){
	return a.w < b.w;
}

int main(){
	int T, N;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cin >> N;
		vector<cube> cubes;
		for(int i = 0; i < N; i++){
			cube p; p.naomi = true; cin >> p.w;
			cubes.push_back(p);
		}
		for(int i = 0; i < N; i++){
			cube p; p.naomi = false; cin >> p.w;
			cubes.push_back(p);
		}
		sort(cubes.begin(),cubes.end(),comp);
		int pastK = 0, pastN = 0, score1 = 0, score2 = 0;
		for(int i = 0; i < cubes.size(); i++){
			if(cubes[i].naomi) pastN++;
			else pastK++;

			if(cubes[i].naomi && pastK){
				score1++; pastK--;
			}
			if(!cubes[i].naomi && pastN){
				score2++; pastN--;
			}
		}
		cout << "Case #" << t << ": " << score1 << " " << N - score2 << endl;
	}
	return 0;
}