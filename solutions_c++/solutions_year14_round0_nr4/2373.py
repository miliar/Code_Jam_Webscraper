/*
    Greedy EVERYTHING!
*/

#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main () {
    int T, n, deceit, normal, pointken, pointnaomi;
    scanf("%d", &T);
    vector <double> ken, naomi;
    for (int cases = 1; cases <= T; cases ++) {
        deceit = 0;
        normal = 0;
        scanf("%d", &n);
        ken.resize(n);
        naomi.resize(n);
        for (int i = 0; i < n; i++) {
            scanf("%lf", &naomi[i]);
        }
        for (int i = 0; i < n; i++) {
            scanf("%lf", &ken[i]);
        }
        sort (naomi.begin(), naomi.end());
        sort (ken.begin(), ken.end());
        ken.push_back(3000.0);
        naomi.push_back(3000.0);
        pointken = 0;
        for (int i = 0; i < n; i++) {
            while (ken [pointken] < naomi [i]) pointken ++;
            if (pointken == n) normal ++;
            else pointken ++;
        }
        pointnaomi = 0;
        for (int i = 0; i < n; i++) {
            while (naomi [pointnaomi] < ken [i]) pointnaomi ++;
            if (pointnaomi == n) deceit ++;
            else pointnaomi ++;
        }
        deceit = n - deceit;
        printf("Case #%d: %d %d\n", cases, deceit, normal);
    }
}
