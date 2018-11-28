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
#include <cmath>
#include <cstdio>
using namespace std;
typedef long long ll;
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
int main()
{
	FILE* fin = freopen("A-small-attempt4.in","rt",stdin);
	FILE* fout = freopen("A.out","wt",stdout);
    int t;
    std::cin>>t;

    for(int pp = 0; pp <t;pp++)
    {
        int n;
        scanf("%d",&n);
        vector<string> v;
        char tmp[150];
        gets(tmp);
        FOR(i,0,n)
        {
            memset(tmp,0,sizeof(tmp));
            gets(tmp);
            v.push_back(tmp);
        }
        bool find = false;
        string real, sss;
        vector<vector<int> > vi;
        FOR(i,0,n)
        {
            vector<int> cc;
            sss.clear();
            sss += v[i][0];
            int ccc = 1;
            FOR(j,1,v[i].size())
            {
                if (v[i][j] != v[i][j-1])
                {
                    sss += v[i][j];
                    cc.push_back(ccc);
                    ccc=1;
                }
                else
                    ccc++;
            }
            cc.push_back(ccc);
            if (i == 0)
                real = sss;
            if (sss != real)
            {
                printf("Case #%d: Fegla Won\n", pp+1);
                find =true;
                break;
            }
            vi.push_back(cc);
        }
        if(!find)
        {
            int sum = 0;

            FOR(i,0,vi[0].size())
            {
                sum+=(abs(vi[0][i] - vi[1][i]));
            }
            printf("Case #%d: %d\n", pp+1, sum);
        }
    }
    fclose(fout);
    fclose(fin);
    return 0;
}
