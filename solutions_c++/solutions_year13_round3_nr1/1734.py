#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <algorithm>
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "math.h"
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define REP(i, a, b) \
    for(int i=int(a); i<int(b); ++i)

int main()
{
    FILE *fout = fopen ("test.out", "w");

    int tc, n, ret, cn = 1;
    scanf("%d", &tc);
    string s;
    while(tc--){
        cin>>s>>n;
        ret = 0;
        REP(i,0,s.length()){
            int maxl = 0;
            int poml = 0;
            bool lc = false;
            REP(j,i,s.length()){
                if(s[j]!='a' && s[j]!='e' && s[j]!='i' && s[j]!='o' && s[j]!='u'){
                    if(lc){
                        ++poml;
                    }
                    else{
                        poml = 1;
                        lc = true;
                    }
                }
                else{
                    if(poml > maxl)
                        maxl = poml;
                    lc = false;
                }

                if(maxl >= n || poml >= n)
                    ++ret;
            }
        }

        fprintf(fout, "Case #%d: %d\n", cn++, ret);
    }

    return 0;
}
