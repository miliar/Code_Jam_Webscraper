#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

FILE *fin  = fopen("a.in",  "r");
FILE *fout = fopen("a.out", "w");

int main() {
    //ios_base::sync_with_stdio(0);
    //fin.tie(0); fout.tie(0); fout.precision(15);

    int n; fscanf(fin, "%d", &n);
    for(int t = 1; t <= n; t++) {
        ll a; fscanf(fin, "%d", &a);
        //cout << t << " " << a << endl;
        if(a == 0) {
            fprintf(fout, "Case #%d: INSOMNIA\n", t);
            continue;
        }
        set<int> seen;
        ll k, temp;
        for(k = 1; seen.size() != 10; k++) {
            temp = k * a;
            while(temp) {
                seen.insert(temp % 10);
                temp /= 10;
            }
        }
        fprintf(fout, "Case #%d: %lld\n", t, (k-1)*a);
    }

    return 0;
}
