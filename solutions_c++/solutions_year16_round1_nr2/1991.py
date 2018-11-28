#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;

int main() {

    freopen("B-large.in", "r", stdin);
    freopen("output-largeB.txt", "w", stdout);
    int t, n, x;
    scanf("%d", &t);
    for(int j = 1; j <= t; j++) {
        scanf("%d", &n);
        int a[2501] = {0};
        for(int i = 0; i < 2*n*n-n; i++) {
            scanf("%d", &x);
            a[x]++;
        }
        std::vector<int> v;
        for(int i = 1; i < 2501; i++) {
            if(a[i] % 2 == 1)
                v.push_back(i);
        }
        sort(v.begin(), v.end());
        cout << "Case #" << j << ": ";
        for(int i = 0; i < v.size()-1; i++)
            cout << v[i] << " ";
        cout << v[v.size()-1] << "\n";
    }

    return 0;
}

//g++ rank.cpp -std=c++11 -o rank