/**
* Change is impossible in this fog of ignorance.
*/
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <climits>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cassert>
#include <cmath>
using namespace std;

#define trace(x) {cerr << #x << "=" << x <<endl;}
#define trace2(x, y) {cerr << #x << "=" << x << " " << #y << "=" << y <<endl;}
#define track(x) {cerr << #x << ":" << endl; for (int q = 0; q < x.size(); q++) {cerr << x[q] << " ";} cerr << endl;}
#define trackarr(x, n) {cerr << #x << ":" << endl; for (int q = 0; q < n; q++) {cerr << x[q] << " ";} cerr << endl;}
#define trackvv(x) {cerr << #x << ":" << endl; for (int i = 0; i < x.size(); i++) { cerr << "i:" << i << endl; for (int j = 0; j < x[i].size(); j++){cerr << x[i][j] << " ";} cerr << endl;} cerr << endl;}
#define trackcr(x) {cerr << #x << ":" << endl; for (auto i = x.begin(); i != x.end(); i++) {cerr << *i << " ";} cerr << endl;}
template <typename Tk, typename Tv> ostream& operator<<(ostream& os, const pair<Tk, Tv> &p){os << "{" << p.first << ',' << p.second << "}";return os;}

typedef long long ll;
typedef pair<int,int> ii;

const int MAX = 100005;
const int MOD = 1000000000+7;
const int INF = 1000000000;

template <typename T>
string toString(T x){
    string s;
    while (x) {
        s.push_back(x % 10 + '0');
        x /= 10;
    }
    reverse(s.begin(), s.end());
    return s;
}

long long toValue(string &x){
    long long sum = 0;
    for (int i = 0; i < x.size(); i++) {
        sum *= 10;
        sum += (x[i]-'0');
    }
    return sum;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int tc;
    cin >> tc;
    for (int t = 1; t <= tc; t++){
        printf("Case #%d: ", t);
        string s;

        cin >> s;
        int n = s.size();
        int count=0, steps=0;
        for (int i = 0; i < n; i++) count+=(s[i]=='+');
        while (count<n) {
            int i = 0, pos = 0;
            for (; (i < n) && (s[i]=='+'); i++) pos++;
            for (int j = 0; j < pos; j++) s[j]='-';
            if (pos > 0) steps++;

            i = s.size()-1;
            for (; i >= 0; i--) if (s[i]=='-') break;
            reverse(s.begin(), s.begin() + i + 1);
            for (int j = 0; j <= i; j++) s[j] = ((s[j]=='+')? '-': '+');
            steps++;

            count = 0;
            for (int j = 0; j < n; j++) count+=(s[j]=='+');
        }
        cout << steps << endl;
    }
}
