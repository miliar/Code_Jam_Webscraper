#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <vector>
using namespace std;
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)

int main()
{
	FILE* fin = freopen("A-small.in","rt",stdin);
	FILE* fout = freopen("A-small.out","wt",stdout);
    int t;
    cin>>t;
    for(int zz=0;zz<t;zz++)
    {
        vector<vector<int> > v;
        FOR(i,0,2)
        {
            int a;
            cin >> a;
            FOR(j,0,4)
            {
                vector<int> t;
                FOR(k,0,4)
                {
                    
                    int b[4];
                    cin >> b[k];
                    if ( j == a-1)
                        t.push_back(b[k]);
                }
                if ( j == a-1)
                    v.push_back(t);
            }
        }
        int cnt = 0;
        vector<int> r;
        FOR(i,0,4)
        {
            FOR(j,0,4)
            {
                if (v[0][i] == v[1][j])
                {
                    cnt++;
                    r.push_back(v[1][j]);
                }
            }
        }
        if (cnt == 0)
            printf("Case #%d: Volunteer cheated!\n", zz+1);
        else if (cnt == 1)
            printf("Case #%d: %d\n", zz+1, r[0]);
        else
            printf("Case #%d: Bad magician!\n", zz+1);
    }
    fclose(fout);
    fclose(fin);
    return 0;
}