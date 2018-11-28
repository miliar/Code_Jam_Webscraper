#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <vector>

using namespace std;

#define N 1004
#define pb push_back

int t, n;
vector<double>::iterator ita, itb, er;
vector<double>::reverse_iterator rit;
vector<double> a, b;

int main(){
    double x;
    
    scanf("%d", &t);
    for(int nt = 1; nt <= t; ++nt){
        scanf("%d", &n);
        a.clear(); b.clear();
        for(int i = 0; i < n; ++i){ scanf("%lf", &x); a.pb(x); }
        for(int i = 0; i < n; ++i){ scanf("%lf", &x); b.pb(x); }
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        vector<double> c(b.begin(), b.end());
        vector<double> a2(a.begin(), a.end());
        int pt1 = 0, pt2 = 0;

        /*for(int i = 0; i < a.size(); ++i) printf("%lf ", a[i]);
        printf("\n");
        for(int i = 0; i < a.size(); ++i) printf("%lf ", b[i]);
        printf("\n");*/

        //deceitful
        int achou;
        for(int i = 0; i < n; ++i){
            achou = 0;
            //nao ganha de ninguem -> joga fora
            if(a[0] < b[0]){
                b.pop_back();
                a.erase(a.begin());
            }
            //senao joga menor
            else{
                a.erase(a.begin());
                b.erase(b.begin());
                pt1++;
            }
        }

        //normal
        //reverse(a2.begin(), a2.end());
        for(ita = a2.begin(); ita < a2.end(); ita++){
            achou = 0;
            //enconta menor que ganha de a
            for(itb = c.begin(); itb < c.end(); itb++){
                if(*ita < *itb){
                    achou = 1;
                    er = itb;
                    break;
                }
            }
            if(achou) {
                c.erase(er);
            }
            else{
                pt2++;
                c.erase(c.begin());
            }
        }
        printf("Case #%d: %d %d\n", nt, pt1, pt2);

    }

    return 0;
}
