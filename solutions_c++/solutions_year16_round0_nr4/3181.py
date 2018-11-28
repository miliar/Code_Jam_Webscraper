#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>
using namespace std;

ifstream fin("D-small-attempt0.in");
ofstream fout("out.txt");

void solve(int k, int c, int s) {
    for (int i = 0; i < k; i++)
        fout << i + 1 << " ";
}

struct q {
    int k, c, s;
};

int main()
{
    int T;
    fin >> T;
    vector<q> a(T);
    for (int i = 0; i < T; i++)
        fin >> a[i].k >> a[i].c >> a[i].s;
    for (int i = 0; i < T; i++) {
        fout << "Case #" << i + 1 << ": ";
        solve(a[i].k, a[i].c, a[i].s);
        fout << endl;
    }
    return 0;
}
