#include <bits/stdc++.h>
#define ff first
#define ss second
#define mp make_pair

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int a[11], k[11], p[11];
int n;

int swaps() {
    int r = 0;
    for(int i=0;i<n;i++) {
        int s = 0;
        for(int j=0;j<n-1;j++) {
            if(p[j] > p[j+1]) {
                swap(p[j],p[j+1]);
                r++;
                s++;
            }
        }
        if(s == 0) break;
    }
    return r;
}

int main() {
    int T;
    cin >> T;
    for(int t=1;t<=T;t++) {
        cin >> n;
        for(int i=0;i<n;i++) {
            cin >> a[i];
            k[i] = a[i];
        }
        sort(k,k+n);
        int m = 1e9;
        do {
            int ok=1, d=0;
            // checa se é crescente e depois decrescente
            for(d=0;d<n-1 && k[d]<k[d+1];d++) ;
            for(int i=d;i<n-1;i++) if(k[i] < k[i+1]) ok = 0;
            // se for calcula qntos movimentos
            if(ok) {
                for(int i=0;i<n;i++) for(int j=0;j<n;j++) {
                    if(a[i] == k[j]) p[i] = j;
                }
                m = min(m, swaps());
            }
        } while(next_permutation(k,k+n));
        printf("Case #%d: %d\n", t, m);
    }
    return 0;
}

