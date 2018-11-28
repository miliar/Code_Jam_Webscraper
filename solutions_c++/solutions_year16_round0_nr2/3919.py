#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <string>
#include <algorithm>
#include <iostream>
#include <math.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main(){
	int T;
	string S;
	cin >> T;
	for(int c = 1; c <= T; c++){
		cin >> S;
		int steps = 0;
		vi v;
		for(int i = 0; i < S.size(); i++){
			if(S[i] == '+') v.push_back(1);
			else v.push_back(0);
		}

		while(v.size() > 0 && v[v.size() - 1] == 1) v.pop_back();

		while(v.size() > 0){
			if(v[0] == 1){
				steps++;
				for(int i = 0; i < v.size(); i++){
					if(v[i] == 0) break;
					v[i] = 1 - v[i];
				}
			}

			steps++;
			reverse(v.begin(), v.end());
			for(int i = 0; i < v.size(); i++){
				v[i] = 1 - v[i];
			}
			while(v.size() > 0 && v[v.size() - 1] == 1) v.pop_back();
		}

		cout << "Case #" << c << ": " << steps << endl;
	}
}
