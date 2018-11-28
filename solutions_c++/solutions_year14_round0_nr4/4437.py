// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 105;
const int INF = 0x3f3f3f3f;
const bool debug=true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

int get_war_score(vector<int> naomi, vector<int> ken) {

    sort(ALL(naomi));
    reverse(ALL(naomi));
    set<int> ken_set(ALL(ken));

    int score = 0;
    for(int i=0;i<SZ(naomi);++i) {
        set<int>::iterator up = ken_set.upper_bound(naomi[i]);
        if (up == ken_set.end()) {
            ++score;
            ken_set.erase(ken_set.begin());
        } else {
            ken_set.erase(up);
        }
    }

    return score;
}

bool check(deque<int> &naomi, deque<int> &ken) {
    for(int i=0;i<SZ(naomi);++i) {
        if(naomi[i] < ken[i]) return false;
    }
    return true;
}

int get_deceptive_war_score(vector<int> naomi, vector<int> ken) {
    sort(ALL(naomi));
    sort(ALL(ken));

    deque<int> naomi_q(ALL(naomi));
    deque<int> ken_q(ALL(ken));

    int score = SZ(naomi);

    do {
        if(check(naomi_q, ken_q)) return score;
        naomi_q.pop_front();
        ken_q.pop_back();
        --score;
    } while(SZ(naomi_q) > 0);

    return 0;
}

int get_num(char buf[20]) {
    int num = 0;
    int len = strlen(buf);
    for(int i=0;i<9;++i) {
        num *= 10;
        if(i+2 < len) {
            num += buf[i+2] - '0';
        }
    }
    return num;
}

int main() {
    int tc;
    scanf("%d",&tc);

    for(int t=1;t<=tc;++t) {
        int tot;
        scanf("%d", &tot);
        vector<int> naomi;
        vector<int> ken;

        for(int i=0;i<tot;++i) {
            char buf[20];
            scanf("%s",buf);
            naomi.push_back(get_num(buf));
        }

        for(int i=0;i<tot;++i) {
            char buf[20];
            scanf("%s",buf);
            ken.push_back(get_num(buf));
        }

        int war_score = get_war_score(naomi, ken);
        int deceptive_war_score = get_deceptive_war_score(naomi, ken);
        printf("Case #%d: %d %d\n", t, deceptive_war_score, war_score);
    }
    return 0;
}

