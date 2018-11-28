#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_##i=(b);i<_##i;++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define MP          make_pair
#define S           size()
typedef long long   LL;

void conversor(long long n,int m[],int i)
{
    if (n!=0)
    {
        m[i-1]=n%2;
        conversor(n/2,m,i-1);
    }
}
int main() {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("small-input_pB.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T ;cas++)
    {
        printf("Case #%d: ", cas);
        int a,b,k;
        cin>>a>>b>>k;
        int cn=0;
        for(int kk=0;kk<a;kk++)
        {
            for(int pp=0;pp<b;pp++)
            {
                if((kk&pp)<k)
                {
                    cn++;
                }
            }
        }
        cout<<cn<<endl;
    }
}
