#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <queue>
using namespace std;

#define BARSUK_ALEXEY_PSKOV

int tests;
int mega_answer = 0;
vector<int> answers;

void fillAnswer() {
    answers.push_back(0);
    int len = 1;
    int s = 1;
    while (answers.size() < 1000000) {
        for (int i = 0; i < len; i++) {
            answers.push_back(s);
        }
        s++;
        for (int i = 0; i < len; i++) {
            answers.push_back(s);
        }
        s++;
        len++;
    }
}

bool isOk(vector<int> & p) {
    for (int i = 0; i < p.size(); i++)
        if (p[i] != 0) return false;
    return true;
}
vector<int> doDecrease(vector<int> p) {
    for (int i = 0; i < p.size(); i++) {
        if (p[i] > 0) p[i]--;
    }

    return p;
}
vector<int> doShift(vector<int> p, int a, int a_pos, int b, int b_pos)
{
    if (a_pos >= p.size()) p.push_back(a);
    else p[a_pos] += a;

    if (b_pos >= p.size()) p.push_back(b);
    else p[b_pos] += b;

    sort(p.begin(), p.end());
    reverse(p.begin(), p.end());

    return p;
}

void rec(int answer, vector<int> p) {
    if (isOk(p)) {
        mega_answer = min(answer, mega_answer);
        return;
    }
    if (answer >= mega_answer) return;

    rec(answer + 1, doDecrease(p));

    int can = answer;
    int mx = 0;
    for (int i = 0; i < p.size(); i++) {
        mx = max(mx, answers[p[i]]);
    }
    if (can + mx >= mega_answer) return;

    for (int i = 1; i <= p[0] - 1; i++) {
        for (int j = 1; j <= p.size(); j++) {
            int a = i;
            int b = p[0] - a;
            p[0] = 0;
            rec(answer + 1, doShift(p, a, j, b, 0));
            p[0] = a + b;
        }
    }
}

int main()
{
#ifdef BARSUK_ALEXEY_PSKOV
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

    fillAnswer();

    cin >> tests;
    for (int t = 1; t <= tests; t++) {
        int d; cin >> d;
        vector<int> p;
        int mx_answer = 0;
        for (int i = 0; i < d; i++) {
            int a; cin >> a;
            p.push_back(a);
            mx_answer = max(mx_answer, a);
        }
        p.push_back(0);
        sort(p.begin(), p.end());
        reverse(p.begin(), p.end());

        mega_answer = mx_answer;
        rec(0, p);

        cout << "Case #" << t << ": " << mega_answer << endl;
    }

    return 0;
}

