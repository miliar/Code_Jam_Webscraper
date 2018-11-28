#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <utility>
#include <stack>
#include <queue>
#include <complex>
#include <iomanip>
using namespace std;

#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector<vector<int> > graph;
const int INF = 1000000000;
const ll MOD = 1000000009;
#define FILEIN "B.in"
#define FILEOUT "B.out"

int A[1005];

int distl[1005];
int distr[1005];

pair<int,int> tmp[1005];
int N;

void precalc(){
	set<pair<int,int> > poses;
	bool used[1005];
	memset(used, 0, sizeof used);
	for(int i = 0; i <N; ++i){
		poses.insert(mp(A[i],i));
		
	}
	for(int i = 0; i < N; ++i){
		
		pair<int,int> pos = *(poses.begin());
		
		poses.erase(poses.begin());
		distl[i] = pos.second;
		distr[i] = N-1-i-pos.second;
		vector<pair<int,int> > curmas;
		for(std::set<pair<int,int> >::iterator it = poses.begin(); it!= poses.end(); ++it){
			
			pair<int,int> cur = *it;
			
			if(cur.second > pos.second){
				cur.second--;
			}
			curmas.pb(cur);
		}
		poses.clear();
		for(int j = 0; j < curmas.size(); ++j){
			poses.insert(curmas[j]);
		}
		
	}
	poses.clear();
}
int main(){
    freopen(FILEIN, "r", stdin);
    freopen(FILEOUT, "w", stdout);
    int tests;
    cin >> tests;
    for (int _ = 1; _ <= tests; ++_){
    	cin>>N;
    	
    	for(int i = 0; i < N; ++i)
    		cin>>A[i];
    	
    	precalc();
    	int res = 0;
    	for(int j = 0; j < N; ++j){
    		res += min(distl[j], distr[j]);
    	}

        cout << "Case #" << _ << ": ";
        cout<<res<<endl;
    }
    return 0;
}