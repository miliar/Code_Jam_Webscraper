#include <bits/stdc++.h>

using namespace std;

struct BARBER {
    int id, m;
    long long finish;
} barber[1005];

class cmp {
    public:
        bool operator() (const BARBER& lhs, const BARBER& rhs) const {
            if (lhs.finish > rhs.finish) return true;
            if (lhs.finish < rhs.finish) return false;
            return lhs.id > rhs.id;
        }
};

long long gcd(long long a, long long b) {
    if (a < b) return gcd(b, a);
    if (b == 0) return a;
    return gcd(b, a%b);
}

long long lcm(long long a, long long b) {
    long long mygcd = gcd(a, b);
    return a/mygcd*b;
}

int solve(int b, long long person) {
    if (person <= b) return person;
    long long ourlcm = barber[0].m;
    for (int i = 1; i < b; ++i) {
        ourlcm = lcm(ourlcm, barber[i].m);
    }
    int base = 0;
    for (int i = 0; i < b; ++i) {
        base += (ourlcm/barber[i].m);
    }

    //cout << "base: " << base << endl;
    person %= base;
    //cout << "ourlcm: " << ourlcm << " person: " << person << endl;
    if (person == 0) {
        int ans_id = 1, ans_m = barber[0].m;
        for (int i = 1; i < b; ++i) {
            if (ans_m > barber[i].m) {
                ans_m = barber[i].m;
                ans_id = i+1;
            }
            if (ans_m == barber[i].m) ans_id = i+1;
        }
        return ans_id;
    }
    if (person <= b) return person;
    person -= b;

    priority_queue<BARBER, vector<BARBER>, cmp> pq;
    for (int i = 0; i < b; ++i) {
        pq.push(barber[i]);
    }
    //cout << pq.top().id << endl;
    while (person > 1) {
        BARBER now = pq.top();
        pq.pop();
        now.finish += now.m;
        pq.push(now);
        --person;
        //cout << person << endl;
    }

    return pq.top().id+1;
}

int main () {
    int tcase;
    scanf("%d", &tcase);
    for (int i = 1; i <= tcase; ++i) {
        int b;
        long long person;
        scanf("%d", &b);
        cin >> person;
        for (int j = 0; j < b; ++j) {
            barber[j].id = j;
            scanf("%d", &barber[j].m);
            barber[j].finish = barber[j].m;
        }
        int ans = solve(b, person);
        printf("Case #%d: %d\n", i, ans);
    }
    return 0;
}
