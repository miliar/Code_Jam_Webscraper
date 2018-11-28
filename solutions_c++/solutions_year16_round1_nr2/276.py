#include <bits/stdc++.h>
using namespace std;
const int N = 55;

int n;
void work() {
    scanf("%d" , &n);
    vector<int> V;
    for (int i = 0 ; i < n + n - 1 ; ++ i) {
        for (int j = 0 ; j < n ; ++ j) {
            int x;
            scanf("%d" , &x);
            V.push_back(x);
        }
    }
    sort(V.begin() , V.end());
    vector<int> res;
    for (int i = 0 ; i < V.size() ; ) {
        int j = i;
        while (j < V.size() && V[i] == V[j]) {
            ++ j;
        }
        if ((j - i) & 1) {
            res.push_back(V[i]);
        }
        i = j;
    }
    for (int i = 0 ; i < res.size() ; ++ i)
        printf("%d%c" , res[i] , " \n"[i + 1 == res.size()]);
}

int main() {
    int T , ca = 0;
    scanf("%d" , &T);
    while (T --) {
        printf("Case #%d: " , ++ ca);
        work();
    }
    return 0;
}
