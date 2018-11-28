#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <deque>
#include <cstring>
#include <string.h>
#include <cmath>

using namespace std;

const int MAXN = 11;

long long n, p;
int numbers[1 << MAXN];
int cntWins[1 << MAXN];

void simulateGame(vector < int > &game, int prizes) {
    if (prizes == 0) {
        return;
    }
    if ((int) game.size() == 1 && prizes > 0) {
        cntWins[game[0]]++;
        return;
    }
    vector < int > firstPart;
    vector < int > secondPart;

    int to = game.size();
    for (int i = 0; i < to; i += 2) {
        if (game[i] < game[i + 1]) {
            firstPart.push_back(game[i]);
            secondPart.push_back(game[i + 1]);
        } else {
            firstPart.push_back(game[i + 1]);
            secondPart.push_back(game[i]);
        }
    }

    if (prizes >= firstPart.size()) {
        to = firstPart.size();
        for (int i = 0; i < to; i++) {
            cntWins[firstPart[i]]++;
        }

        simulateGame(secondPart, prizes - to);
    } else {
        simulateGame(firstPart, prizes);
    }
}

void simulate_game(vector < int > &game) {
    if ((int) game.size() == 1) {
        cout << game[0] << " ";
        return;
    }

    vector < int > firstPart;
    vector < int > secondPart;

    int to = game.size();
    for (int i = 0; i < to; i += 2) {
        if (game[i] < game[i + 1]) {
            firstPart.push_back(game[i]);
            secondPart.push_back(game[i + 1]);
        } else {
            firstPart.push_back(game[i + 1]);
            secondPart.push_back(game[i]);
        }
    }

    simulate_game(firstPart);
    simulate_game(secondPart);
}

pair < int, int > solve() {
    memset(cntWins, 0, sizeof(cntWins));

    scanf("%d %d", &n, &p);

/*    if ((1 << n) == p) {
        return make_pair(p - 1, p - 1);
    }*/

    int players = 1 << n;
    for (int i = 0; i < players; i++) {
        numbers[i] = i;
    }

    int gamesCount = 1;
    for (int i = 1; i <= players; i++) {
        gamesCount *= i;
    }

    do {
        vector < int > game;
        for (int i = 0; i < players; i++) {
            game.push_back(numbers[i]);
        }

        simulateGame(game, p);

    } while (next_permutation(numbers, numbers + players));

    int maxWin = -1, maxWinAlways = -1;
    for (int i = 0; i < players; i++) {
            //cout << i << " " << cntWins[i] << endl;
        if (cntWins[i] > 0) {
            maxWin = i;
            if (cntWins[i] == gamesCount) {
                maxWinAlways = i;
            }
        }
    }

    return make_pair(maxWinAlways, maxWin);
}

pair <long long, long long> solve2() {
    cin >> n >> p;
    if (p == 1LL) {
        return make_pair(0, 0);
    }
    if (p == (1LL << n)) {
        return make_pair(p - 1, p - 1);
    }
    long long players, savedP = p, add;

    players = 1LL << n;
    p = savedP;
    add = 2;
    long long absoluteWin = 0;
    while (p > (players >> 1)) {
        absoluteWin += add;
        add += (add & (-add));
        p -= (players >> 1);
        players = players >> 1;
    }

    long long turns = savedP >> 1;
    add = (1LL << (n - 1));
    long long win = 0;
    while (turns) {
        win += add;
        add = add >> 1;
        turns = turns >> 1;
    }

    return make_pair(absoluteWin, win);
}

int main() {
    int tests;
    scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        pair <long long, long long> result = solve2();
        //printf("Case #%d: %d %d\n", test, result.first, result.second);
        cout << "Case #" << test << ": " << result.first << " " << result.second << endl;
        //result = solve2();
       // printf("Case #%d: %d %d\n", test, result.first, result.second);
    }

    return 0;
}
