#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <random>

using namespace std;


vector< vector<pair<int,int> > > l = {
    {make_pair(0, 1),  make_pair(1, 1),  make_pair(2, 1), make_pair(3, 1)},
    {make_pair(1, 1),  make_pair(0, -1), make_pair(3, 1), make_pair(2, -1)},
    {make_pair(2, 1),  make_pair(3, -1), make_pair(0, -1),make_pair(1, 1)},
    {make_pair(3, 1),  make_pair(2, 1),  make_pair(1, -1),make_pair(0, -1)}
};

auto getNext = [](const char& c) {
      if (c == 'i') return 1;
      if (c == 'j') return 2;
      return 3;
};

pair<int,int> multRight(pair<int,int>& val,const char& q) {
    return make_pair(l[val.first][getNext(q)].first, (l[val.first][getNext(q)].second*val.second));
}

pair<int,int> multLeft(pair<int,int>& val,const char& q) {
    return make_pair(l[getNext(q)][val.first].first, (l[getNext(q)][val.first].second*val.second));
}

string getc(const int& i) {
    if (i == 0) return "1";
    if (i == 1) return "i";
    if (i == 2) return "j";
    return "k";
}

string eval(const string& s,int l,int r) {
    pair<int,int> val = {0, 1};
    for (int i = l; i <= r; i++) {
        val = multRight(val, s[i]);
    }
    return (val.second == -1 ? "-" : "") + getc(val.first);
}

string solveSmall(int L,int X, const string& aux) {  
    pair<int,int> val = {0, 1};
    pair<int,int> tail = {0, 1};
    int fi = -1;
    int fk = -1;
    string s = "";
    for (int i = 0; i < X; i++) s += aux;
    L = L * X;
    if (L < 3) return "NO";
    for (int i = 0; i < L; i++) {
        val = multRight(val, s[i]);
        tail = multLeft(tail, s[L - i - 1]);
        if (fi == -1 && val.first == 1 && val.second == 1) fi = i;
        if (fk == -1 && tail.first == 3 && tail.second == 1) fk = L - i - 1;
    }
    if (fi != -1 && fk != -1 && fi < fk) {
        if (val.first == 0 && val.second == -1) return "YES";
    }
    return "NO";
}

string brute(int l,int x,const string& s) {
    if (x != 1) return "foo";
    for (int i = 0; i < l; i++) {
        for (int j = i + 1; j < l - 1; j++) {
            if (eval(s, 0, i) == "i" && eval(s,i + 1, j) == "j" && eval(s,j + 1, l -1) == "k") {
                return "YES";
            }
        }
    }

    return "NO";
}

void test() {
    std::random_device rd;
    std::mt19937 mt(time(0));
    std::uniform_int_distribution<int> dist(1, 10000);
    int t = 10;
    for (int i = 1; i <= t; i++) {
        int l = dist(mt) % 20;
        int x = 1;
        string s(l, '.');
        const char* q = "ijk";
        for (char& c : s) {
            c = q[dist(mt) % 3];
        }
        if (brute(l, x, s) != solveSmall(l, x, s)) {
             cout << l << " " << s << "\n";
        }
    }
}

int main() {
    ifstream cin("test.in");
    ofstream cout("test.out"); 
    int T;
    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        int L, X;
        string s;
        cin >> L >> X;
        cin.get();
        getline(cin, s); 
        cout << "Case #" << testCase << ": " << solveSmall(L, X, s) << "\n";
    }
    return 0;
}

