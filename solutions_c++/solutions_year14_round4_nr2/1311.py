#include <cstdio>
#include <vector>
#include <algorithm>
#define scanf(args...) (scanf(args) ? : 0)
const int MAXN = 1e3+5;
const int INF = 1e9;

int T[MAXN], n;
int perm[MAXN];
int mapped[MAXN];

int inversePref(int p) {
    int res = 0;
    std::vector<int> vec(T, T+p+1);
    for (int i=0; i<vec.size(); i++)
        for (int j=0; j+1<vec.size(); j++) {
            if (vec[j] > vec[j+1]) {
                res++;
                std::swap(vec[j], vec[j+1]);
            }
        }

    return res;
}

int inverseSuf(int p) {
    int res = 0;
    std::vector<int> vec(T+p, T+n);
    for (int i=0; i<vec.size(); i++)
        for (int j=0; j+1<vec.size(); j++) {
            if (vec[j] < vec[j+1]) {
                res++;
                std::swap(vec[j], vec[j+1]);
            }
        }
    return res;
}

void scale(int* T, int n) {
    std::vector<int*> array(n);
    for (int i=0; i<n; i++)
        array[i] = T+i;
    std::sort(array.begin(), array.end(), [](int* a, int* b) { return *a < *b; });
    for (int i=0; i<n; i++)
        *array[i] = i;
}


void solve(int test) {
    scanf("%d", &n);
    for (int i=0; i<n; i++)
        scanf("%d", &T[i]);
    scale(T, n);

    for (int i=0; i<n; i++)
        perm[i] = i;
    
    int best = INF;
    while (true) {
        int it = 0;
        while (it+1 < n && perm[it] < perm[it+1])
            it++;
        while (it+1 < n && perm[it] > perm[it+1])
            it++;

        if (it+1 == n) {
            for (int i=0; i<n; i++)
                mapped[perm[i]] = i;
            
            int current = 0;
            std::vector<int> table(T, T+n);
            for (int q=0; q<n; q++)
                for (int i=0; i+1<n; i++)
                    if (mapped[table[i]] > mapped[table[i+1]]) {
                        std::swap(table[i], table[i+1]);
                        current++;
                    }
            best = std::min(best, current);
        }

        if (!std::next_permutation(perm, perm+n))
            break;
    }

    printf("Case #%d: %d\n", test, best);

    /*int wrong = std::min(inversePref(n-1), inverseSuf(0));
    for (int i=1; i<n-1; i++) {
        int current = inversePref(i-1)+inverseSuf(i);
        wrong = std::min(wrong, current);
    }

    printf("Case #%d: %d\n", test, wrong);*/
}

int main() {
    int t;
    scanf("%d", &t);

    for (int i=1; i<=t; i++)
        solve(i);
}
