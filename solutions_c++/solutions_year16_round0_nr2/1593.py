#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
#define MAXS 101
#define INF 1<<30

void printv(vector<bool> pcs) {
    cout << "* ";
    for (auto pc : pcs) {
        cout << pc;
    }
    cout << endl;
}

bool allhappy(vector<bool> pcs) {
    for (auto pc : pcs) {
        if (!pc) return false;
    }
    return true;
}

vector<bool> flipall(vector<bool> pcs) {
    for (auto pc : pcs) {
        pc = !pc;
    }
    reverse(pcs.begin(), pcs.end());
    return pcs;
}

vector<bool> inverse(vector<bool> pcs) {
    for (auto pc : pcs) {
        pc = !pc;
    }
    return pcs;
}

vector<bool> gettopi(vector<bool> pcs, int I) {
    pcs.erase(pcs.begin() + I, pcs.end());
    return pcs;
}

vector<bool> getbottomnoti(vector<bool> pcs, int I) {
    pcs.erase(pcs.begin(), pcs.begin() + I);
    return pcs;
}

vector<bool> trimbottom(vector<bool> pcs) {
    while (pcs.back() == true) {
        pcs.pop_back();
    }
    return pcs;
}

int dfs(vector<bool> pcs) {
    pcs = trimbottom(pcs);
    if (allhappy(pcs)) {
        return 0;
    }
    if (pcs.size() == 1) {
        return 1;
    }

    int i;
    for (i = pcs.size()-1; i >= 0; i--) {
        if (pcs[i]) break;
    }
    i++;

    int best = dfs(inverse(gettopi(pcs, i))) + dfs(flipall(getbottomnoti(pcs, i))) + 1;

    return best;
}


int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        char input[MAXS];
        cin >> input;
        vector<bool> pancakes;
        for (int i = 0; input[i] != '\0'; i++) {
            pancakes.push_back((input[i] == '+') ? true : false);
        }

        int res = dfs(pancakes);
        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
