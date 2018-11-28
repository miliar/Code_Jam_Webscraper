#include <bits/stdc++.h>

using namespace std;


vector< set<int> > lines;
int best;

void minans(int i, set<int> eng, set<int> fre, set<int> com) {
    if (com.size() >= best)
        return;
    
    if (i == lines.size()) {
        best = min(best, (int)com.size());
        return;
    }
    
    {
        set<int> c2 = com;
        set<int> e2 = eng, f2 = fre;
        for (auto &it : lines[i]) {
            if (e2.count(it)) {
                c2.insert(it);
                e2.erase(it); f2.erase(it);
            }
            else
                f2.insert(it);
        }
        minans(i+1, e2, f2, c2);
    }
    
    {
        set<int> c2 = com;
        set<int> e2 = eng, f2 = fre;
        for (auto &it : lines[i]) {
            if (f2.count(it)) {
                c2.insert(it);
                e2.erase(it); f2.erase(it);
            }
            else
                e2.insert(it);
        }
        minans(i+1, e2, f2, c2);
    }
}

int solve() {
    int n;
    map<string, int> wordmap;
    int nextid = 0;
    cin >> n >> ws;
    lines.clear();
    for (int i = 0; i < n; i++) {
        string s, w;
        getline(cin, s);
        istringstream ss(s);
        set<int> line;
        while (ss >> w) {
            if (!wordmap.count(w))
                wordmap[w] = nextid++;
            line.insert(wordmap[w]);
        }
        lines.push_back(line);
    }
    set<int> eng = lines[0], fre, com;
    for (auto &it : lines[1]) {
        if (eng.count(it)) {
            eng.erase(it);
            com.insert(it);
        }
        else
            fre.insert(it);
    }
    best = INT_MAX;
    minans(2, eng, fre, com);
    return best;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": " << solve() << endl;
        cerr << "Case " << i << " done" << endl;
    }
    return 0;
}
