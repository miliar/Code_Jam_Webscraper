#include <bits/stdc++.h>
using namespace std;
#define DB(v) cerr << #v << ' ' << v << endl
#define sz(v) int(v.size())

vector <int> divisors = {3, 4, 5, 6, 7, 8, 9, 10, 11};

string s;
int n,j;

int cur = 1;

void print() {
    cout << s << ' ';
    for(int to: divisors) cout << to << ' ';
    cout << '\n';
    cur++;
}

void go(int i) {
    if(cur > j) return;
    if(i == 0) {
        print();
        return;
    }
    s[i] = s[i-1] = '1';
    go(i - 2);
    s[i] = s[i-1] = '0';
    go(i - 2);
}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t; cin >> t;
    cin >> n >> j; s.resize(n);
    cout << "Case #1:" << endl;
    s[0] = s[n - 1] = '1';
    go(n - 2);
    return 0;
}
