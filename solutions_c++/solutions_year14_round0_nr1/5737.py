#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <vector>
#include <list>
#include <set>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cmath>
#include <cassert>
#include <climits>

using namespace std;

#define isOn(S, j) (S & (1 << j))
#define setBit(S, j) (S |= (1 << j))
#define clearBit(S, j) (S &= ~(1 << j))
#define toggleBit(S, j) (S ^= (1 << j))
#define lowBit(S) (S & (-S))
#define setAll(S, n) (S = (1 << n) - 1)
// returns S % N, where N is a power of 2
#define modulo(S, N) ((S) & (N - 1))
#define isPowerOfTwo(S) (!(S & (S - 1)))
#define nearestPowerOfTwo(S) \
    ((int)pow(2.0, (int)((log((double)S) / log(2.0)) + 0.5)))
#define turnOffLastBit(S) ((S) & (S - 1))
#define turnOnLastZero(S) ((S) | (S + 1))
#define turnOffLastConsecutiveBits(S) ((S) & (S + 1))
#define turnOnLastConsecutiveZeroes(S) ((S) | (S - 1))

#define all(x) x.begin(), x.end()
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define MP make_pair

typedef long long int ll;
typedef vector<int> vi;
typedef map<int, int> mii;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int main(int argc, char *argv[]) {
    int T;
    int board[5][5];
    int ini, end;
    int temp;
    vi guess, fguess;
    scanf("%d", &T);
FOR(num,1,T+1) {
    guess.clear();
    fguess.clear();
    scanf("%d", &ini);
    FOR(i,1,5) {
        FOR(j,1,5) {
            scanf("%d", &board[i][j]);
        }
    }
    for(int i = 1; i <= 4; i++)
        guess.PB(board[ini][i]);
    scanf("%d", &end);
    FOR(i,1,5) {
        FOR(j,1,5) {
            scanf("%d", &board[i][j]);
        }
    }
    int found = 0;
    int magic;
    for(int i = 1; i <= 4; i++) {
        for(int j = 0; j < (int)guess.size(); j++) {
            if(guess[j] == board[end][i]) {
                found++;
                magic = guess[j];
            }
        }}
    if(found == 1)
        printf("Case #%d: %d\n", num, magic);
    else if(found == 0)
        printf("Case #%d: Volunteer cheated!\n", num);
    else if(found > 1)
        printf("Case #%d: Bad magician!\n", num);
}
    return 0;
}
