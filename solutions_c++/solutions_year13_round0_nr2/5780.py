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
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("salida4.out","w",stdout);
    int t,N,M,co;
    bool sol;
    int A[10][10];
    cin>>t;
    for(int a=0;a<t;a++)
    {
        sol=true;
        cin>>N>>M;
        for(int b1=0;b1<N;b1++)
        {
            for(int b2=0;b2<M;b2++)
            {
                cin>>A[b1][b2];
            }
        }
        for(int c1=0;c1<N;c1++)
        {
            for(int c2=0;c2<M;c2++)
            {
                co=0;
                if(A[c1][c2]==1)
                {
                    for(int d1=0;d1<N;d1++){if(A[d1][c2]==2)co++;}
                    if(co>0){for(int d2=0;d2<M;d2++){if(A[c1][d2]==2)sol=false;}}
                }
                if(sol==false)break;
            }
            if(sol==false)break;
        }
        if(sol==true)printf("Case #%d: YES\n",a+1);
        else printf("Case #%d: NO\n",a+1);
    }
}
