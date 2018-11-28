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


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int n,r=1;
    scanf("%d",&n);
    while(n>0)
    {
        double c,f,x,ck=2,ct=0,sum=0,aux=0,sf=0;
        int q=1;
        scanf("%lf",&c);
        scanf("%lf",&f);
        scanf("%lf",&x);
        for(;;)
        {
            sum=aux+(x/ck);
            //cout<<"sum: "<<sum<<endl;
            aux=aux+(c/ck);
            //cout<<"aux: "<<aux<<endl;
            ck=ck+f;
            if(q!=1)
            {
                if(sum>sf)
                {
                    printf("Case #%d: %.7lf\n",r,sf);
                    break;
                }
            }
            sf=sum;
            q++;
        }
        n-=1;
        r+=1;
    }

}
