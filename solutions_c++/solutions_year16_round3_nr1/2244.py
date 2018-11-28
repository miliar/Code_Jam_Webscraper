#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define mp make_pair

set < pair <int , int> > Q;


int main (){
    freopen ("A-large.in" , "r" , stdin);

freopen ("output.txt" , "w" , stdout);

    int tests;
    cin >> tests;
    for (int t = 1 ; t <= tests; ++t){
            int n;
            scanf ("%d" , &n);
            for (int i = 0 ; i < n  ; ++i) {
                    int cnt;
                    scanf ("%d" , &cnt);
                    Q.insert (mp(-cnt , i));
            }
            printf ("Case #%d:" , t);

            while (!Q.empty()) {
                    int A = Q.begin()->se;
                    int A1 = -Q.begin()->fi;Q.erase (Q.begin());

                    int B = Q.begin()->se;
                    int B1 = -Q.begin()->fi;Q.erase (Q.begin());

                    if (Q.empty()||A1 > 1 && A1 == B1) {
                        printf (" %c%c" , char(A + 'A') , char(B + 'A'));
                        if (A1 > 1)
                                Q.insert (mp(-A1 + 1, A)),
                                Q.insert (mp(-B1 + 1, B));
                        continue;
                    }

                    printf (" %c" , char(A + 'A'));
                    if (A1 > 1)
                            Q.insert (mp(-A1 + 1, A));Q.insert (mp(-B1, B));
            }
            printf ("\n");
    }
    return 0;
}
