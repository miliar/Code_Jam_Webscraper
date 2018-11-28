#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <queue>
#include <cmath>
#include <list>
#include <cstring>
#include <cstdlib>
#include <limits>
#include <stack>
#include <iomanip>

using namespace std;

ofstream fout ("D-large.out");
ifstream fin ("D-large.in");

int main() {
    int T, N;
    fin >> T;
    for (int t = 1; t <= T; t++) {
        fin >> N;
        vector<double> naomi(N), ken(N);
        for (int i = 0; i < N; i++) fin >> naomi[i];
        for (int i = 0; i < N; i++) fin >> ken[i];
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        int nao = 0;
        int ke = 0;
        int ans1, ans2;
        ans1 = ans2 = 0;
        for (int i = 0; i < N; i++) {
            if (naomi[i] > ken[ke]) {
                ans1++;
                ke++;
            }
        }
        ke = 0;
        for (int i = 0; i < N; i++) {
            while (ke < N && ken[ke] < naomi[i]) ke++;
            if (ke == N) break;
            ke++;
            ans2++;
        }
        ans2 = N - ans2;
        fout <<  "Case #" << t << ": " << ans1 << " " << ans2 << endl;
    }
}
