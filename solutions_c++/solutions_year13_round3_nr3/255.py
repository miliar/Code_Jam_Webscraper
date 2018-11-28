#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <string.h>
#include <memory.h>

using namespace std;

const int MAXWALLSIZE = 600;
long long wall[MAXWALLSIZE];
long long wallInterval[MAXWALLSIZE];
int tribesCount;

struct Tribe {
    int firstDay;
    int numberOfAttacks;
    int east, west;
    long long firstAttack;
    int deltaDay;
    int deltaDist;
    int deltaAttack;

    Tribe(int _firstDay, int _numberOfAttacks, int _east, int _west, long long _firstAttack,
          int _deltaDay, int _deltaDist, int _deltaAttack) {
        firstDay = _firstDay;
        numberOfAttacks = _numberOfAttacks;
        east = _east;
        west = _west;
        firstAttack = _firstAttack;
        deltaDay = _deltaDay;
        deltaDist = _deltaDist;
        deltaAttack = _deltaAttack;
    }
};

struct Event {
    int tribeId;
    int round;
    int day;
    Event(int _day, int _tribeId, int _round) {
        tribeId = _tribeId;
        round = _round;
        day = _day;
    }

    bool operator < (const Event& other) const {
        return day > other.day;
    }
};

struct Repair {
    int east;
    int west;
    long long height;
    Repair(int _west, int _east, long long _height) {
        east = _east;
        west = _west;
        height = _height;
    }
};

vector < Tribe > tribes;
vector < Repair > repairs;

void doRepairs() {
    for (int i = 0; i < (int) repairs.size(); i++) {
        for (int j = repairs[i].west; j < repairs[i].east; j++) {
            wallInterval[j] = max(wallInterval[j], repairs[i].height);
        }
        for (int j = repairs[i].west; j <= repairs[i].east; j++) {
            wall[j] = max(wall[j], repairs[i].height);
        }
    }

    repairs = vector < Repair >();
}

bool isSuccesfull(int west, int east, long long height) {
    for (int i = west; i < east; i++) {
        if (wallInterval[i] < height) {
            return true;
        }
    }

    for (int i = west; i <= east; i++) {
        if (wall[i] < height) {
            return true;
        }
    }

    return false;
}

int solve() {
    memset(wall, 0, sizeof(wall));
    memset(wallInterval, 0, sizeof(wallInterval));

    priority_queue < Event > events;
    tribes = vector < Tribe >();
    repairs = vector < Repair >();

    scanf("%d", &tribesCount);
    for (int i = 0; i < tribesCount; i++) {
        int firstDay;
        int numberOfAttacks;
        int east, west;
        long long firstAttack;
        int deltaDay;
        int deltaDist;
        int deltaAttack;

        cin >> firstDay >> numberOfAttacks >> west >> east >> firstAttack >> deltaDay >> deltaDist >> deltaAttack;
 /*       //scanf("%d %d %d %d %d %d %d %d", &firstDay, &numberOfAttacks, &west, &east, &firstAttack, &deltaDay, &deltaDist, &deltaAttack);
        cout << firstDay << endl;
        cout << numberOfAttacks << endl;
        cout << west << endl;
        cout << east << endl;
        cout << firstAttack << endl;
        cout << deltaDay << endl;
        cout << deltaDist << endl;
        cout << deltaAttack << endl;*/
        tribes.push_back(Tribe(firstDay, numberOfAttacks, east + 250, west + 250, (long long) firstAttack, deltaDay, deltaDist, deltaAttack));
        events.push(Event(firstDay, i, 1));
    }

    int res = 0;
    int prevDay = -1;
    while (!events.empty()) {
        Event temp = events.top();
        events.pop();
        if (prevDay != temp.day) {
            doRepairs();
        }

        prevDay = temp.day;
        int west = tribes[temp.tribeId].west + (temp.round - 1) * tribes[temp.tribeId].deltaDist;
        int east = tribes[temp.tribeId].east + (temp.round - 1) * tribes[temp.tribeId].deltaDist;
        long long height = tribes[temp.tribeId].firstAttack + (temp.round - 1) * tribes[temp.tribeId].deltaAttack;

        if (isSuccesfull(west, east, height)) {
            res++;
            repairs.push_back(Repair(west, east, height));
        }

        if (temp.round < tribes[temp.tribeId].numberOfAttacks) {
            events.push(Event(temp.day + tribes[temp.tribeId].deltaDay, temp.tribeId, temp.round + 1));
        }
    }

    return res;
}

int main() {
    int tests;
    scanf("%d", &tests);

    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": " << solve() << endl;
    }

    return 0;
}
