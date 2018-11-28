// David Wahler <dwahler@gmail.com>
// Google Code Jam submission: 

#include <algorithm>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define D(x) x

using namespace std;

typedef long long i64;

i64 best_place(i64 N, i64 rank) {
	i64 players = 1<<N;
	if (rank <= 0) {
		return 0;
	} else if (rank >= players-1) {
		return players-1;
	} else {
		return best_place(N-1, (rank+1)/2);
	}
}

i64 worst_place(i64 N, i64 rank) {
	i64 players = 1<<N;
	if (rank <= 0) {
		return 0;
	} else if (rank >= players-1) {
		return players-1;
	} else {
		int worse = (players-rank-1);
		int new_worse = (worse+1)/2;
		return players/2 + worst_place(N-1, players/2-new_worse-1);
	}
}

int main() {
    int T;
    cin >> T;
    

    for (int testCase = 1; testCase <= T; testCase++) {
    	i64 N, P;
    	cin >> N >> P;

    	i64 players = 1<<N;
    	i64 guaranteed_win = 0, guaranteed_lose = players;

    	for (i64 i = 0; i < players; i++) {
    		if (best_place(N, i) < P) {
    			guaranteed_win = max(guaranteed_win, i);
    		}
    		if (worst_place(N, i) >= P) {
    			guaranteed_lose = min(guaranteed_lose, i);
    		}
    	}
        cout << "Case #" << testCase << ": ";
        cout << (guaranteed_lose-1) << " " << (guaranteed_win);
        cout << endl;
    }
}
