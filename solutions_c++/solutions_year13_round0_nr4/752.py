
// Language: C++
// Problem: D. Treasure
// User: samuel.gruetter

#include <vector>
#include <stack>
#include <cstdio>

using namespace std;

#define MAXO 0xFFFFF
#define MAXKT 200

int K, N;

// key type needed to open
vector<int> nto(21);

// keys in chest, inch[i] = (keyType=>howMany) vector
vector< vector< int > > inch(21);

// M[op] = list containing all (keyType=>howMany) vectors with given open chests op
vector< vector< vector< int > > > M(MAXO+1);

vector<int> path; // chest ids

bool found;

int needed1s;

#define BYTETOBINARYPATTERN "%d%d%d%d%d%d%d%d"
#define BYTETOBINARY(byte)  \
  (byte & 0x80 ? 1 : 0), \
  (byte & 0x40 ? 1 : 0), \
  (byte & 0x20 ? 1 : 0), \
  (byte & 0x10 ? 1 : 0), \
  (byte & 0x08 ? 1 : 0), \
  (byte & 0x04 ? 1 : 0), \
  (byte & 0x02 ? 1 : 0), \
  (byte & 0x01 ? 1 : 0) 

// returns true if ks1 is strictly better than ks2
bool keySet1Better(vector<int>& ks1, vector<int>& ks2) {
	bool strictly = false;
	for (int kt=1; kt<=MAXKT; ++kt) if (ks1[kt] < ks2[kt]) {
		return false;
	} else if (ks1[kt] > ks2[kt]) {
		strictly = true;
	}
	return strictly;
} 

// search from M[op][index]
void find(int op, int index) {
	/*printf("[");
	for (int j=0; j<path.size(); ++j) printf("%d ", path[j]);
	printf("]--[" BYTETOBINARYPATTERN "]\n", BYTETOBINARY(op));*/
	
	if (op == needed1s) {
		found = true;
		return;
	}
		
	int mask = 1;
	for (int chest=1; chest<=N; ++chest) {
		bool isOpen = ((mask & op) != 0);
		bool hasKey = (M[op][index][nto[chest]] > 0);
		//printf("(%d %c%c)", chest, !isOpen?'y':'n', hasKey?'y':'n');
		if (hasKey && !isOpen) {
			int newOp = (op | mask);

			//printf("(" BYTETOBINARYPATTERN ")", BYTETOBINARY(newOp));
			
			vector<int> newKeySet(MAXKT+1);
			for (int kt=1; kt<=MAXKT; ++kt) newKeySet[kt] = M[op][index][kt] + inch[chest][kt];
			newKeySet[nto[chest]]--;
			bool wroteIt = false;
			int newIndex = -1;
			for (int i=0; i<M[newOp].size(); ++i) {
				if (keySet1Better(M[newOp][i], newKeySet)) {
					break; // newKeySet is bad
				} else if (keySet1Better(newKeySet, M[newOp][i])) {
					if (!wroteIt) {
						// overwrite this bad keySet with newKeySet
						for (int kt=1; kt<=MAXKT; ++kt) M[newOp][i][kt] = newKeySet[kt];
						wroteIt = true;
						newIndex = i;
					} else {
						// another bad keySet, set it to 0 so that all others will be better
						// and can occupy its memory
						for (int kt=1; kt<=MAXKT; ++kt) M[newOp][i][kt] = 0;
					}
				}
			}
			if (M[newOp].size() == 0) {
				M[newOp].push_back(newKeySet);
				newIndex = 0;
			}
			if (newIndex != -1) {
				path.push_back(chest);
				find(newOp, newIndex);
				if (found) return; // without popping path
				path.pop_back();
			}			
		}
		mask *= 2;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i=1; i<=T; ++i) {
		scanf("%d %d", &K, &N);
		for (int j=0; j < (1 << N); ++j) M[j].clear();
		//for (int j=0; j <= N; ++j) inch[j].clear();
		M[0].push_back(vector<int>(MAXKT+1, 0));
		for (int j=0; j<K; ++j) {
			int kt;
			scanf("%d", &kt);
			M[0][0][kt]++;
		}
		needed1s = (1 << N) - 1;
		for (int j=1; j<=N; ++j) {
			int Ti, Ki;
			scanf("%d %d", &Ti, &Ki);
			nto[j] = Ti;
			inch[j] = vector<int>(MAXKT+1, 0);
			for (int l=0; l<Ki; ++l) {
				int kt;
				scanf("%d", &kt);
				inch[j][kt]++;
			}
		}

		path.clear();
		found = false;
		find(0, 0);
		printf("Case #%d:", i);
		if (found) {
			if (path.size() != N) printf("weird\n");
			for (int j=0; j<path.size(); ++j) printf(" %d", path[j]);
			printf("\n");
		} else {
			printf(" IMPOSSIBLE\n");
		}
	}
}

