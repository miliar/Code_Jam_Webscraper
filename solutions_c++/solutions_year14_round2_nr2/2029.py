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
using namespace std;
typedef long long ll;
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)

int main()
{
	FILE* fin = freopen("B-small-attempt0.in","rt",stdin);
	FILE* fout = freopen("b-out.txt","wt",stdout);
    int t;
    std::cin>>t;
    
    FOR(xx,0,t)
    {
        int a,b,k;
        scanf("%d %d %d",&a,&b,&k);
        int cnt = 0;
        FOR(i,0,a)
        {
            FOR(j,0,b)
            {
                if((i&j) < k)
                    cnt++;
            }
        }
        printf("Case #%d: %d\n", xx+1, cnt);
    }
    fclose(fout);
    fclose(fin);
    return 0;
}