#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <unordered_map>

using namespace std;

int n;
vector<int> s[20];
vector<string> t[20];
int f[20];
int ans;

unordered_map<int, int> english;
unordered_map<int, int> french;
unordered_map<string, int> wid;
unordered_map<int, int> wcnt;

int count()
{
    int ans = 0;
    for (unordered_map<int, int>::iterator it = english.begin();
            it != english.end(); ++it) {
        if (english[it->first] > 0 && french[it->first] > 0) {
            ++ans;
        //    cout << it->first << endl;
        }
    }
    return ans;
}

void updateEnglish(int p, int d)
{
    for (int i = 0; i < s[p].size(); ++i)
        english[s[p][i]] += d;
}

void updateFrench(int p, int d)
{
    for (int i = 0; i < s[p].size(); ++i)
        french[s[p][i]] += d;
}

int checkAll(int p)
{
    int e = 0;
    int f = 0;
    int m = s[p].size();
    for (int i = 0; i < m; ++i) {
        if (english[s[p][i]] > 1)
            ++e;
        if (french[s[p][i]] > 1)
            ++f;
    }
    if (e == m)
        return 0;
    if (f == m)
        return 1;
    return -1;
}

void search(int p) {
    if (count() > ans)
        return;
    if (p == n) {
        ans = min(ans, count());
    } else {
        int c = checkAll(p);
        if (c == 0 || c == -1) {
            f[p] = 0;
            updateEnglish(p, 1);
            search(p + 1);
            updateEnglish(p, -1);
        }
        if (c == 1 || c == -1) {
            f[p] = 1;
            updateFrench(p, 1);
            search(p + 1);
            updateFrench(p, -1);
        }
    }
}

void work(ifstream &fin, int caseno)
{
    fin >> n;
    string line;
    string word;
    getline(fin, line);
    wid.clear();
    wcnt.clear();
    english.clear();
    french.clear();
    int idx = 0;
    for (int i = 0; i < n; ++i) {
        getline(fin, line);
        istringstream sin(line);
        t[i].clear();
        while (sin >> word) {
            t[i].push_back(word);
            if (wid.find(word) == wid.end()) {
                wid[word] = idx++;
                wcnt[wid[word]] = 1;
            } else {
                wcnt[wid[word]]++;
            }
        }
       // cout << s[i].size() << endl;
    }

    unordered_map<int, int> exist;
    for (int i = 0; i < n; ++i) {
        s[i].clear();
        for (vector<string>::iterator it = t[i].begin();
                it != t[i].end(); ++it) {
            if (wcnt[wid[*it]] > 1) {
                s[i].push_back(wid[*it]);
                english[wid[*it]] = french[wid[*it]] = 0;
                exist[wid[*it]] = 0;
            }
        }
    }
  //  cout << n << " " << idx << " " << exist.size() << endl;

    f[0] = 0;
    updateEnglish(0, 1);
    f[1] = 1;
    updateFrench(1, 1);
    ans = 1000 * n;
    search(2); 
    cout << "Case #" << caseno << ": " << ans << endl;
}

int main()
{
    ifstream fin;
    fin.open("input");
    int t;
    fin >> t;
    for (int i = 0; i < t; ++i) {
        work(fin, i + 1);
    }
    fin.close();
    return 0;
}
