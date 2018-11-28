#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
using namespace std;

bool a[1001];

bool check(int n) {
    vector<int> v;
    while (n) {
        v.push_back(n%10);
        n/=10;
    }
    for (int j=0; j<v.size()/2; j++) {
        if (v[j] != v[v.size()-1-j]) return false;
    }
    return true;
}

int main() {
    freopen("/Users/fengyelei/Desktop/A-small.in", "r", stdin);
    freopen("/Users/fengyelei/Desktop/out", "w", stdout);
    int T, t=1;
    int i, j, k, n, m;
    
    for (i=1; i<=1000; i++) {
        a[i] = check(i);
    }
    for (scanf("%d", &T); t<=T; t++) {
        scanf("%d %d", &n, &m);
        int c = 0;
        for (i=1; i*i<=m; i++) {
            if (i*i >= n && a[i] && a[i*i]) c++;
        }
        printf("Case #%d: %d\n", t, c);
    }
}
