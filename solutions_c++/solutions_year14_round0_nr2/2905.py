//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
using namespace std;
int main()
{
    int a,s,d,f,g,h,j,k,l,q;
    freopen("in.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
    double z,x,c,v,b,n,m,ans;
    cin>>a;
    for(s=1;s<=a;s++)
    {
        cin>>z>>x>>c;
        l=c+1;
        ans=c/2.0;
        b=2.0;
        v=0.0;
        for(d=1;d<=l;d++)
        {
            v=v+z/b;
            b=b+x;
            n=v+c/b;
            ans=min(ans,n);
        }
        printf("Case #%d: %.10lf\n",s,ans);
    }
}
