#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <vector>

using namespace std;

int getMinMinutesAux(priority_queue<int> diners) {
    int curr = diners.top();

    if (curr == 1)
        return curr;

    priority_queue<int> next = diners;
    next.pop();
    next.push(curr / 2);
    next.push(curr - (curr / 2));

    return min(curr, 1 + getMinMinutesAux(next));
}

int getMinMinutes(vector<int> diners) {
    priority_queue<int> pq;
    int N = diners.size();

    for (int i = 0; i < N; i++)
        pq.push(diners[i]);

    return getMinMinutesAux(pq);
}

map<vector<int>, int> minutes;

int getMinMinutesSimpleAux(vector<int> diners) {
    sort(diners.begin(), diners.end());
    if (diners.size() == 0)
        return 0;
    if (minutes[diners] != 0)
        return minutes[diners];
    int N = diners.size();
    int large = diners[0];
    for (int i = 1; i < N; i++)
        if (diners[i] > large)
            large = diners[i];

    vector<int> eat;
    for (int i = 0; i < N; i++)
        if (diners[i] - 1 > 0)
            eat.push_back(diners[i] - 1);
    int best = 1 + getMinMinutesSimpleAux(eat);

    for (int i = 0; i < N; i++) {
        for (int j = 1; j < diners[i]; j++) {
            vector<int> next;
            for (int k = 0; k < N; k++) {
                if (k != i)
                    next.push_back(diners[k]);
                else {
                    next.push_back(diners[i] - j);
                    next.push_back(j);
                }
            }
            best = min(best, 1 + getMinMinutesSimpleAux(next));
        }
    }

    minutes[diners] = best;
    return minutes[diners];
}

int getMinMinutesSimple(vector<int> diners) {
    return getMinMinutesSimpleAux(diners);
}

#define MAXP 1001
int dp[MAXP][MAXP];

int getMinMinutesDp(vector<int> diners) {
    int best = 0;
    int N = diners.size();

    for (int i = 0; i < N; i++)
        if (diners[i] > best)
            best = diners[i];

    int l = best;
    for (int j = l; j >= 1; j--) {
        int curr = 0;
        for (int i = 0; i < N; i++)
            curr += dp[diners[i]][j];
        best = min(best, curr + j);
    }

    return best;
}

int main() {
    for (int i = 0; i < MAXP; i++) {
        dp[i][i] = 0;
        for (int j = 1; j < i; j++) {
            if (j >= i - j)
                dp[i][j] = 1;
            else
                dp[i][j] = 1 + dp[i - j][j];
        }
    }

    int T;
    cin >> T;

    for (int i = 1; i <= T; i++) {
        int D;
        cin >> D;

        vector<int> diners;
        diners.assign(D, 0);
        for (int j = 0; j < D; j++)
            cin >> diners[j];

        cout << "Case #" << i << ": " << getMinMinutesDp(diners) << endl;
    }

    return 0;
}
