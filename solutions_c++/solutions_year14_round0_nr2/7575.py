#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    double C,F,X;
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>C>>F>>X;
        double tmp=X/C-2.0/F;
        int K=0;
        if(tmp>0) K=(int)(tmp);
        double ans=0;
        for(int i=0;i<K;i++)
        {
            ans+=(C/(2.0+((double)(i))*F));
        }
        ans+=(X/(2.0+((double)(K))*F));
        printf("Case #%d: %.7f\n",ca,ans);
    }
    return 0;
}
