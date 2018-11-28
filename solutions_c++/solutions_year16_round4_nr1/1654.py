#include <stdio.h>
#include <map>
#include <algorithm>
#include <iostream>
using namespace std;

struct Node {
    long long a, b, c, d;
};

map< long long, string > used;

long long V(Node t) {
    long long base = 10000;
    long long ans = t.a * base * base + t.b * base + t.c;
    ans *= (long long)3;
    ans += t.d;
    return ans;
}
long long V(long long a, long long b, long long c, long long d) {
    long long base = 10000;
    long long ans = a * base * base + b * base + c;
    ans *= (long long)3;
    ans += d;
    return ans;
}

void Work(int lev, long long v, Node temp) {
    long long n = (1 << lev);
    int a_min = max((long long)0, n / 2 - temp.b - temp.c), a_max = min(n / 2, temp.a);
    for (int i = a_min; i <= a_max; i++) {
        int b_min = max((long long)0, n / 2 - i - temp.c), b_max = min(temp.b, (n - 2 * i) / 2);
        for (int j = b_min; j <= b_max; j++) {
            Node t1, t2;
            t1.a = i; t2.a = temp.a - i;
            t1.b = j; t2.b = temp.b - j;
            t1.c = n / 2 - i - j; t2.c = temp.c - t1.c;
            if (temp.d == 0) {
                t1.d = 0; t2.d = 1;
                long long v1 = V(t1), v2 = V(t2);
                if (used.find(v1) == used.end()) {
                    Work(lev - 1, V(t1), t1);
                }
                if (used.find(v2) == used.end()) {
                    Work(lev - 1, V(t2), t2);
                }
                if ((used.find(v1) != used.end()) && (used.find(v2) != used.end())) {
                    string t = min(used[v1] + used[v2], used[v2] + used[v1]);
                    map< long long, string >::iterator iter = used.find(v);
                    if (iter == used.end()) {
                        used.insert(pair<long long, string>(v, t));
                    } else {
                        if (iter->second > t) {
                            iter->second = t;
                        }
                    }
                }
                t1.d = 1; t2.d = 0;
                v1 = V(t1), v2 = V(t2);
                if (used.find(v1) == used.end()) {
                    Work(lev - 1, V(t1), t1);
                }
                if (used.find(v2) == used.end()) {
                    Work(lev - 1, V(t2), t2);
                }
                if ((used.find(v1) != used.end()) && (used.find(v2) != used.end())) {
                    string t = min(used[v1] + used[v2], used[v2] + used[v1]);
                    map< long long, string >::iterator iter = used.find(v);
                    if (iter == used.end()) {
                        used.insert(pair<long long, string>(v, t));
                    } else {
                        if (iter->second > t) {
                            iter->second = t;
                        }
                    }
                }
            }
            if (temp.d == 1) {
                t1.d = 2; t2.d = 1;
                long long v1 = V(t1), v2 = V(t2);
                if (used.find(v1) == used.end()) {
                    Work(lev - 1, V(t1), t1);
                }
                if (used.find(v2) == used.end()) {
                    Work(lev - 1, V(t2), t2);
                }
                if ((used.find(v1) != used.end()) && (used.find(v2) != used.end())) {
                    string t = min(used[v1] + used[v2], used[v2] + used[v1]);
                    map< long long, string >::iterator iter = used.find(v);
                    if (iter == used.end()) {
                        used.insert(pair<long long, string>(v, t));
                    } else {
                        if (iter->second > t) {
                            iter->second = t;
                        }
                    }
                }
                t1.d = 1; t2.d = 2;
                v1 = V(t1), v2 = V(t2);
                if (used.find(v1) == used.end()) {
                    Work(lev - 1, V(t1), t1);
                }
                if (used.find(v2) == used.end()) {
                    Work(lev - 1, V(t2), t2);
                }
                if ((used.find(v1) != used.end()) && (used.find(v2) != used.end())) {
                    string t = min(used[v1] + used[v2], used[v2] + used[v1]);
                    map< long long, string >::iterator iter = used.find(v);
                    if (iter == used.end()) {
                        used.insert(pair<long long, string>(v, t));
                    } else {
                        if (iter->second > t) {
                            iter->second = t;
                        }
                    }
                }
            }
            if (temp.d == 2) {
                t1.d = 0; t2.d = 2;
                long long v1 = V(t1), v2 = V(t2);
                if (used.find(v1) == used.end()) {
                    Work(lev - 1, V(t1), t1);
                }
                if (used.find(v2) == used.end()) {
                    Work(lev - 1, V(t2), t2);
                }
                if ((used.find(v1) != used.end()) && (used.find(v2) != used.end())) {
                    string t = min(used[v1] + used[v2], used[v2] + used[v1]);
                    map< long long, string >::iterator iter = used.find(v);
                    if (iter == used.end()) {
                        used.insert(pair<long long, string>(v, t));
                    } else {
                        if (iter->second > t) {
                            iter->second = t;
                        }
                    }
                }
                t1.d = 2; t2.d = 0;
                v1 = V(t1), v2 = V(t2);
                if (used.find(v1) == used.end()) {
                    Work(lev - 1, V(t1), t1);
                }
                if (used.find(v2) == used.end()) {
                    Work(lev - 1, V(t2), t2);
                }
                if ((used.find(v1) != used.end()) && (used.find(v2) != used.end())) {
                    string t = min(used[v1] + used[v2], used[v2] + used[v1]);
                    map< long long, string >::iterator iter = used.find(v);
                    if (iter == used.end()) {
                        used.insert(pair<long long, string>(v, t));
                    } else {
                        if (iter->second > t) {
                            iter->second = t;
                        }
                    }
                }
            }
        }
    }
}

int main() {
    Node temp; temp.d = -1;
    used.insert(pair< long long, string > (V(1, 0, 0, 0), "R"));
    used.insert(pair< long long, string > (V(0, 1, 0, 1), "S"));
    used.insert(pair< long long, string > (V(0, 0, 1, 2), "P"));
    /*
    for (int i = 1; i <= 12; i++) {
        printf("%d\n", i);
        for (int j = 1; j <= (1 << i) + 1; j++)
            for (int k = j + 1; k <= (1 << i) + 2; k++) {
                for (int l = 0; l < 3; l++) {
                    Node temp;
                    temp.a = j - 1;
                    temp.b = k - j - 1;
                    temp.c = (1 << i) + 2 - k;
                    temp.d = l;
                    long long v = V(temp);
                    Check(i, v, temp);
                }
            }
    }*/

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++) {
        int a, b, c, lev;
        scanf("%d%d%d%d", &lev, &a, &c, &b);
        printf("Case #%d: ", t);
        string ans = "";
        for (int i = 0; i < 3; i++) {
            long long v = V(a, b, c, i);
            Node temp;
            temp.a = a;
            temp.b = b;
            temp.c = c;
            temp.d = i;
            Work(lev, v, temp);
            map< long long, string >::iterator iter = used.find(v);
            if ((iter != used.end()) && ((ans.length() == 0) || (ans > iter->second))) {
                ans = iter->second;
            }
        }
        if (ans.length() == 0) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%s\n", ans.c_str());
        }
    }
    return 0;
}
