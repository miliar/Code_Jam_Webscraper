#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

const int maxn = 10000;

int Tree[maxn];
int Size = 0;

void add(int x) {
    int v = x + Size;
    while (v != 0) {
        Tree[v] += 1;
        v /= 2;
    }
}

int Sum(int v, int vl, int vr, int l, int r) {
    if (l <= vl && vr <= r) {
        return Tree[v];
    } else if (r <= vl || vr <= l) {
        return 0;
    } else {
        int vm = (vl + vr) / 2;
        return Sum(2 * v, vl, vm, l, r) + Sum(2 * v + 1, vm, vr, l, r);
    }   
}

bool comp(pair <int, int> A, pair <int, int> B)  {
    return A.second < B.second;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; ++test) {
        int N;
        scanf("%d", &N);
        vector <pair <int, int> > A(N);
        for (int i = 0; i < N; ++i) {
            scanf("%d", &A[i].first);
            A[i].second = i;
        }
        sort(A.begin(), A.end());
        for (int i = 0; i < N; ++i) {
            A[i].first = i;
        }
        sort(A.begin(), A.end(), comp);
        vector <int> cnt1(N, 0), cnt2(N, 0);
        Size = 1;
        while (Size <= N) Size *= 2;
        for (int i = 0; i <= Size * 2; ++i) {
            Tree[i] = 0; 
        }
        for (int i = 0; i < N; ++i) {
            cnt1[i] = Sum(1, 0, Size, A[i].first, Size);
            add(A[i].first);
        }
        for (int i = 0; i <= Size * 2; ++i) {
            Tree[i] = 0; 
        }
        for (int i = N - 1; i >= 0; --i) {
            cnt2[i] = Sum(1, 0, Size, A[i].first, Size);
            add(A[i].first);
        }
        int Min = 0;
        for (int i = 0; i < N; ++i) {
            Min += min(cnt1[i], cnt2[i]);
        }
        printf("Case #%d: %d\n", test + 1, Min);
    } 

}