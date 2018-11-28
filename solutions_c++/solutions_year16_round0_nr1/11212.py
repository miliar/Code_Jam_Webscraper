#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iterator>
#include <string>
#include <sstream>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i, a, b) for (int i = (int)a; i <= (int)b; i++)
#define arrL(arr) (int)(sizeof(arr)/sizeof(*arr)) 
#define MAX 100000

string ins = "INSOMNIA";
string list[10] = {"0","1","2","3","4","5","6","7","8","9"};
vector<string> all;
string allC[10];
int pen = 0;

void vecToArr() {
    copy(all.begin(), all.end(), allC);
}

void inAllC() {
    for(int i=0;i<arrL(allC);i++) allC[i] = "-1";
}

bool in_array(string x) {
    const size_t nE = sizeof(allC) / sizeof(allC[0]);
    string* end = allC + nE;
    return find(allC, end, x) != end;
}

void operate(int x) {
    stringstream ss;ss << x;
    string s;ss >> s;
    for (int i = 0; i < (int)s.length(); i++) {
        stringstream sss;string si;
        sss << s[i];sss >> si;
        if (!in_array(si) && all.size() < 10) {
            all.push_back(si);
            allC[pen++] = si;
            vecToArr();
        }
    }
}

void solve(int i, int x) {
    string ans = "";
    if (x == 0) ans = ins;
    else {
        inAllC();
        pen = 0;
        int a=x,l=2;
        while (true) {
            operate(a);
            if (all.size() == 10) {
                stringstream ss;ss << a;ss >> ans;
                break;
            }
            a = l++*x;
        }
    }

    cout << "Case #" << (i+1) << ": " << ans << endl;
    all.clear();
}

int main(int argc, char *argv[]) {
    //cout.setf(ios::fixed);
    //cout.precision(0);
    int N, x;
    cin >> N;
    REP(i, N) {
        cin >> x;
        inAllC();
        solve(i, x);
    }
}
