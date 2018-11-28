#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("out.txt");

void solve(string s) {
    vector<int> a;
    a.push_back(s[0]);
    for (int i = 1; i < s.size(); i++) {
        if (s[i] != s[i - 1])
            a.push_back(s[i]);
    }
    int ans = a.size();
    if (a.back() == '+')
        ans--;
    fout << ans;
}

int main()
{
    int t;
    fin >> t;
    vector<string> a(t);
    for (int i = 0; i < t; i++)
        fin >> a[i];
    for (int i = 0; i < t; i++) {
        fout << "Case #" << i + 1 << ": ";
        solve(a[i]);
        fout << endl;
    }
    return 0;
}
