#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;

#define FOR(i,a,b)  for (int i = int(a); i < int(b); +i)

int T;

bool next_round(int* lists, int num){
    if (num == 0) return true;
    for (int i = 0; i < num; i+=2){
        if (lists[i] == lists[i+1]) return false;
        else if (lists[i] + lists[i+1] == 4) lists[i/2] = 3;
        else if (lists[i] + lists[i+1] == 5) lists[i/2] = 2;
        else lists[i/2] = 1;
    }
    return next_round(lists, num/2);
}

void make_order(int* lists, int start, int ends){
    if (start == ends) return;
    for (int i = 0; i < ends; i+=2*start){
        for (int a = i, b = i+start ; a < i+start; ++a, ++b){
            if (!((lists[a] == 1 && lists[b] != 1) || (lists[a] == 2 && lists[b] == 3)||(lists[a]==lists[b]))){
                for (int j = i, k = i+start ; j < i+start; ++j, ++k) swap(lists[j], lists[k]);
                break;
            }
        }
    }
    return make_order(lists, 2*start, ends);
}

int main() {

    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);

    scanf("%d", &T);
    for (int t = 1; t <= T; ++t){
        printf("Case #%d: ", t);
        int N, R, P, S;
        cin >> N >> R >> P >> S;
        vector <int> comps;
        for (int i = 0; i < R; ++i) comps.push_back(2);
        for (int i = 0; i < P; ++i) comps.push_back(1);
        for (int i = 0; i < S; ++i) comps.push_back(3);
        sort(comps.begin(), comps.end());
        bool flag = false;
        do {
            int* men = new int [R+P+S];
            for (int i = 0; i < R+P+S; ++i) men[i] = comps[i];
            if (next_round(men, R+P+S)){
                make_order(men, 1, R+P+S);
                for (int i = 0; i < R+P+S; ++i){
                    if (men[i] == 2) cout << "R";
                    else if (men[i] == 1) cout << "P";
                    else cout << "S";
                }
                flag = true;
                break;
            }
            delete [] men;

        } while (next_permutation(comps.begin(), comps.end()));
        if (!flag) printf("IMPOSSIBLE");

        printf("\n");
    }
    return 0;
}
