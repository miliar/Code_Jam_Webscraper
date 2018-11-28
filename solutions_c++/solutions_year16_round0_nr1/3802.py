#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

ifstream fin("A-small-attempt1.in");
ofstream fout("out.txt");

void plusa(vector<int> &a, vector<int> &b) {
    a.push_back(0);
    for (int i = 0; i < a.size(); i++) {
        if (i < b.size())
            a[i] += b[i];
        a[i + 1] += a[i] / 10;
        a[i] %= 10;
    }
    if (a.back() == 0)
        a.resize(a.size() - 1);
}

void print(vector<int> &s) {
    for (int i = 0; i < s.size(); i++)
        fout << s[s.size() - i - 1];
}

void solve(int n) {
     vector<int> s;
    bool flag = false;
    vector<bool> used(10);
    while (n > 0) {
        s.push_back(n % 10);
        n /= 10;
    }
    vector<int> p = s;
    for (int i = 0; i < s.size(); i++) {
        used[s[i]] = true;
    }
    flag = true;
    for (int i = 0; i < used.size(); i++) {
        if (!used[i])
            flag = false;
    }
    for (int i = 0; i < 1e5 && !flag; i++) {
        plusa(s, p);
        for (int i = 0; i < s.size(); i++) {
            used[s[i]] = true;
        }
        flag = true;
        for (int i = 0; i < used.size(); i++) {
            if (!used[i])
                flag = false;
        }
        if (flag == true) {
            print(s);
            return;
        }
    }
    fout << "INSOMNIA";
}

int main()
{
    int t;
    fin >> t;
    vector<int> a(t);
    for (int i = 0; i < t; i++)
        fin >> a[i];
    for (int i = 0; i < t; i++) {
        if (a[i] == 0) {
            fout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
        }
        else {
            fout << "Case #" << i + 1 << ": ";
            solve(a[i]);
            fout << endl;
        }
    }
    return 0;
}
