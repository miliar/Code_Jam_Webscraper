#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <cassert>
#include <vector>
#include <set>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

#define ll long long
#define point pair<double, double>
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define uint unsigned int
#define merge botva
#define M_PI 3.14159265358979323846
#define left b1
#define right b2

#define plus botva12


const int INF = 1200000000, mod = 1000002013, maxn = 1006;

int dx[] = {-1, 0, 1,  0};
int dy[] = { 0, 1, 0, -1};

int hm[maxn], hmm[maxn];

int n, b, zB;
long double best;

double zac() {
        long double now = b - zB;
        long long vnow = 0;
        int minf = 1000000;
        int vz = 0;
        for (int k = 0; k < n; ++k) minf = min(minf, hmm[k] + hm[k]);
        for (int k = 0; k < n; ++k) {
                if (hmm[k] + hm[k] == minf) {
                        vnow += hmm[k] * 36;
                        ++vz;
                }
        }
        now += (vnow + 0.0l) / vz;
        best = max(best, now);
}

int main() {
        int t, af;
        cin >> t;
        for (int zi = 0; zi < t; ++zi) {
                cin >> b >> n;
                memset(hm, 0, sizeof hm);
                memset(hmm, 0, sizeof hmm);
                for (int i = 0; i < n; ++i)
                        scanf("%d", &hm[i]);
                zB = b;
                n = 37;
                best = 0;
                while (b) {
                        pair<int, int> minf = make_pair(1000000, 1000);
                        for (int i = 0; i < n; ++i)
                                minf = min(minf, mp(hm[i] + hmm[i], hmm[i]));
                        for (int i = 0; i < n; ++i)
                                if (minf == mp(hm[i] + hmm[i], hmm[i])) {
                                        ++hmm[i];
                                        --b;
                                        zac();
                                        break;
                                }
                }
                
                printf("Case #%d: ", zi + 1);
                cout.precision(20);
                cout << best << endl;
        }
}
