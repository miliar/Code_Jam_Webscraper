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
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
    int n,f1,cs=1;
    scanf("%d",&n);
    while(n>0)
    {
    int c=0,aux=0;
    scanf("%d",&f1);
    int a[4][4];int v[4];
    FOR(i,0,4)
    {
        FOR(j,0,4)
        {
            cin>>a[i][j];
        }
    }
    FOR(x,0,4)
    {
        v[x]=a[f1-1][x];
    }
    int r2;
    scanf("%d",&r2);
    FOR(i,0,4)
    {
        FOR(j,0,4)
        {
            cin>>a[i][j];
        }
    }
        FOR(b,0,4)
        {
            FOR(e,0,4)
            {
                if(v[b]==a[r2-1][e])
                {
                    c++;
                    aux=v[b];
                }
            }
        }
        if(c==0)
        {
            cout<<"Case #"<<cs<<": Volunteer cheated!"<<endl;
        }
        else
        if(c>1)
        {
            cout<<"Case #"<<cs<<": Bad magician!"<<endl;
        }
        else
        {
            cout<<"Case #"<<cs<<": "<<aux<<endl;
        }
        n-=1;
        cs+=1;
  }
}
