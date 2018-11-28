//
// a.cpp -- A
//
// Siwakorn Sriakaokul - ping128
// Written on Saturday, 13 April 2013.
//

#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <algorithm>
#include <map>
#include <ctype.h>

using namespace std;

typedef long long LL;

#define MAXN 21

map<int, int> startkey;
map<int, int> chestkey[MAXN];
int keytoopen[MAXN];
int K, N;

int dp[1<<MAXN];
int next[1<<MAXN];

bool search(int state){
	int res = 0;
	if(state == ((1<<N) - 1))
		return 1;
	if(dp[state] != -1) return dp[state];
	for(int i = 0; i < N; i++ ){
		if(!((1<<i) & state) && startkey[keytoopen[i]]){
			startkey[keytoopen[i]]--;
			for(map<int, int>::iterator it = chestkey[i].begin(); it != chestkey[i].end(); it++ ){
				startkey[it->first] += it->second;
			}
			res = search(state | (1<<i));
			startkey[keytoopen[i]]++;
			for(map<int, int>::iterator it = chestkey[i].begin(); it != chestkey[i].end(); it++ ){
				startkey[it->first] -= it->second;
			}
			if(res){
				next[state] = (state | (1<<i));
				return dp[state] = 1;
			}
		}
	}
	return dp[state] = 0;
}


void solve(){

	cin >> K >> N;
	startkey.clear();
	for(int i = 0; i < K; i++ ){
		int key;
		cin >> key;
		startkey[key]++;
	}
	for(int i = 0; i < N; i++ )
		chestkey[i].clear();

	for(int i = 0; i < N; i++ ){
		cin >> keytoopen[i];
		int num;
		cin >> num;
		for(int j = 0; j < num; j++ ){
			int key;
			cin >> key;
			chestkey[i][key]++;
		}
	}

	for(int j = 0; j < 1<<MAXN; j++ ){
		dp[j] = next[j] = -1;
	}

	if(search(0)){
		int c;
		int state;
		for(int i = 0; i < N; i++ ){
			if((next[0] & (1<<i))){
				c = i;
				state = (1<<i);
				break;
			}
		}
		cout << c + 1;
		for(int i = 0; i < N - 1; i++ ){
			int nextstate = next[state];
			for(int j = 0; j < N; j++ ){
				if(((1<<j) & nextstate) && !((1<<j) & state)){
					cout << " " << j + 1;
					state = nextstate;	
					break;
				}
			}
		}
		cout << endl;
	} else {
		cout << "IMPOSSIBLE" << endl;
	}
}


int main()
{
	int test;
	cin >> test;
	for(int tt = 0; tt < test; tt++ ){
		printf("Case #%d: ", tt + 1);
		solve();
	}
	return 0;
}
