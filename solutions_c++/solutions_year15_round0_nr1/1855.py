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

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int T = INPT_INT;

    for(int ca = 1; ca <= T; ++ca)
    {
        int len; char S[1002];

        scanf("%d %s",&len,S);

        int totalClap = 0, res = 0;

        for(int shyNess = 0; shyNess <= len; ++shyNess) if(S[shyNess] > '0')
        {
            if( shyNess > totalClap )
            {
                res += shyNess - totalClap;
                totalClap += shyNess - totalClap;
            }
            totalClap += S[shyNess]-'0';
        }
        printf("Case #%d: %d\n",ca,res);
    }
	return 0;
}
