#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <limits>
#include <algorithm>
#include <ctime>
#include <cstring>

using namespace std;

const int MAXV = 10000;
int n, m;
int cnt, cs = 0;
vector<int> num;

bool check(vector<int> &div) {
    div.resize(11);
    for (int i = 2; i <= 10; ++i) {
        long long vv = 0;
        for (size_t j = 0; j < num.size(); ++j) {
            vv = vv * i + num[j];
        }
        bool prime = true;
        for (long long j = 2; j * j <= vv; ++j) {
            if (vv % j == 0) {
                prime = false;
                div[i] = j;
                break;
            }
        }
        if (prime == true) return false;
    }
    return true;
}

void dfs(int k) {
    if (cnt == m) return;
    if (k == n) {
        if (num[0] == 1 && num.back() == 1) {
            vector<int> div;
            if (check(div)) {
                ++cnt;
                for (size_t i = 0; i < num.size(); ++i)
                    cout<<num[i];
                for (size_t i = 2; i <= 10; ++i) {
                    cout<<" ";
                    cout<<div[i];
                }
                cout<<endl;
                if (cnt == m) {
                    return;
                }
            }
        }
        return;
    }
    num.push_back(0);
    dfs(k + 1);
    num.pop_back();

    num.push_back(1);
    dfs(k + 1);
    num.pop_back();

}

int main() {
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
    int t;
    cin>>t;
    while (t--) {
        cin>>n>>m;
        cnt = 0;
        printf("Case #%d:\n",++cs);
        dfs(0);
    }
    return 0;
}
