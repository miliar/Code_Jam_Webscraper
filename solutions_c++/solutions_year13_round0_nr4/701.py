#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#define MAX(a,b) (a)>(b)?(a):(b)
#define MIN(a,b) (a)<(b)?(a):(b)

using namespace std;
int TESTS;
int K,N,tmp;
string num2str(int i) {stringstream ss; ss<<i; return ss.str();}

inline bool canVisit(int chest, int mask, vector<int> &T, vector<vector<int> > &Keys, vector<int> &initialKeys){
	int cant = 0;
	for(int bit = 0; bit<T.size(); bit++){
		if((mask & (1<<bit)) != 0){
			for(int i = 0; i<Keys[bit].size(); i++){
				if(Keys[bit][i] == T[chest]) cant++;
			}
			if(T[bit] == T[chest]) cant--;
		}
	}

	for(int i = 0; i<initialKeys.size(); i++)
		if(initialKeys[i] == T[chest]) cant++;
	return (cant>0);
}

pair<bool,string> cache[1<<21];

pair<bool,string> solve(int mask, vector<int> &T, vector<vector<int> > &Keys, vector<int> &initialKeys){
	if(mask == (1<<N)-1) return make_pair(true,"");
	if(cache[mask].second != "A") return cache[mask];
	pair<bool,string> ret;
	for(int i = 0; i<N; i++){
		if((mask & (1<<i)) == 0){
			if(canVisit(i,mask,T,Keys, initialKeys)){
				pair<bool,string> res = solve(mask | (1<<i), T, Keys, initialKeys);
				if(res.first){
					string t = num2str(i+1);
					ret = make_pair(true, t + " " + res.second);
					cache[mask] = ret;
					return ret;
				}
			}
		}
	}
	ret = make_pair(false,"");
	cache[mask] = ret;
	return ret;
}

 int main(){
	ifstream in("A.txt"); 
	ofstream out("resultado.txt");
	in >> TESTS;
	for(int test =1; test<=TESTS; test++){
		in >> K >> N;
		int mask = 0;
		vector<int> initialKeys;
		for(int i = 0; i<K; i++){
			in >> tmp; tmp--;
			initialKeys.push_back(tmp);
		}
		vector<int> T(N);
		vector< vector<int> > Keys(N);
		for(int i = 0; i<N; i++){
			int tmp1;
			in >> tmp1 >> tmp; tmp1--;
			T[i] = tmp1;
			Keys[i].resize(tmp);
			for(int j = 0; j<tmp; j++){
				in >> tmp1; tmp1--;
				Keys[i][j] = tmp1;
			}
		}

		for(int i = 0; i<(1<<T.size()); i++)
			cache[i] = make_pair(false,"A");

		pair<bool,string> ret = solve(0,T,Keys,initialKeys);

		out << "Case #" << test << ": ";
		cout << "Case #" << test << ": ";

		if(ret.first == false){
			out << "IMPOSSIBLE" << endl;
			cout << "IMPOSSIBLE" << endl;
		}
		else{
			out << ret.second << endl;
			cout << ret.second << endl;
		}

	}
	return 0;
 }
    