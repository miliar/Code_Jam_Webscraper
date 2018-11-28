#include <bits/stdc++.h>
#define ull unsigned long long

using namespace std;

int ligados (int n){
    int k = 0;
    while (n){
        if (n&1) k++;
        n>>=1;
    }
    return k;
}

double prob (vector <double> v){
    int n = v.size();
    double pro = 0;
    for (int i = 0; i < (1<<n); i++){
        double aux = 1;

        if ( ligados(i) != n/2) continue;
       // cout << i << endl;
        for (int j = 0; j < n; j++){
            if (i&(1<<j)){
                aux *= v[j];
            } else{
                aux *= (1- v[j]);
            }
        }
      //  cout << aux << endl;
        pro += aux;
    }
    return pro;
}

double v[201];

int main(){
    int tt;
    scanf ("%d", &tt);

    for (int cc = 1; cc <= tt; cc++){
        printf ("Case #%d: ", cc);

        int n, k;
        scanf ("%d %d", &n, &k);
        for (int i = 0; i < n; i++) scanf ("%lf", v + i);
        double ans = -1;
        for (int i = 1; i < (1<<n); i++){
            if (ligados(i) == k){
               // cout << i << endl;
                vector <double> test;
                for (int j = 0; j < n; j++){
                    if (i&(1<<j)){
                        test.push_back (v[j]);
                       // cout << v[j] << " ";
                    }
                }
                double p = prob(test);
                ans = max (p, ans);
            }
        }
        printf ("%.10lf\n", ans);
    }

    return 0;
}
