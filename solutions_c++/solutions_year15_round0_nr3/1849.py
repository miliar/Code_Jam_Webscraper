#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <numeric>
#include <algorithm>
#include <functional>
using namespace std;

const inline int __GET_INT(){int ret;scanf("%d",&ret);return ret;}
#define INPT_INT __GET_INT()

typedef long long LL;
//1 = 1, i = 2, j = 3, k = 4

char str[10005], dp[10005][5][2][4];
int L, X, n, mp[258], mat[][4] = {{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};

char calc(int pos, int last, bool isNeg, int done)
{
    if( pos == n )
    {
        return ((last==4) && (isNeg==false) && (last==(2+done)));
    }
    char &ret = dp[pos][last][isNeg][done];
    if( ret != -1 )
    {
        return ret;
    }
    ret = 0;
    int cur = mp[str[pos%L]];

    if(last != 4 && last == (2+done) && !isNeg)
    {
        ret = max(ret, calc(pos+1,cur,false,done+1));
    }

    int next = mat[last-1][cur-1] * (isNeg?-1:1);
    ret = max(ret, calc(pos+1,abs(next),next<0,done));
    return ret;
}

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small.out","w",stdout);

    int T = INPT_INT;
    mp['1'] = 1; mp['i'] = 2; mp['j'] = 3; mp['k'] = 4;
    string res[] = {"NO","YES"};

    for(int ca = 1; ca <= T; ++ca)
    {
        L = INPT_INT; X = INPT_INT;
        scanf("%s",str);

        n = L*X;
        memset(dp,-1,sizeof(dp));
        printf("Case #%d: %s\n",ca,res[calc(1,mp[str[0]],false,0)].c_str());
    }
	return 0;
}
