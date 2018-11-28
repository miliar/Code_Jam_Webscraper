
// User: lovelotus(Prem Kamal)

//#include<bits/stdc++.h>
//#define _ ios_base::sync_with_stdio(0);cin.tie(0);

#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<map>
#include<string>
#include<vector>
#include<queue>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<stack>
#include<set>
#include<utility>
#define pii pair<int,int>
#define pip pair<int,pii>
#define F first
#define S second
#define lli long long int
using namespace std;


int main()
{
    freopen("C:\\Users\\lovelotus\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\lovelotus\\Desktop\\output.txt","w",stdout);
    int t,tst=1;
    double c,f,x,val1,val2,ans,it;
    scanf("%d",&t);
    while(t--)
    {
        ans=0.0000000;
        it=2.000000;
        scanf("%lf%lf%lf",&c,&f,&x);
        val1=c/it + x/(it+f);
        val2=x/it;
        while(val1<val2)
        {
            ans+=c/it;
            it+=f;
            val1=c/it+x/(it+f);
            val2=x/it;
        }
        ans+=x/it;
        printf("Case #%d: %.8lf\n",tst,ans);
        tst++;
    }
    return 0;
}
