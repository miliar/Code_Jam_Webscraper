#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<algorithm>
#include<string>
#include<stack>
#include<cstring>
#include<utility>
#include<cmath>
#include<queue>
#include<cstdlib>

using namespace std;

#define LL long long
#define REP(i,a,b) for(int i = a;i<b;i++)
#define REP0(i,b) REP(i,0,b)
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)



int CASES,TEST = 0;;
LL r,t;

LL check(LL root)
{
    LL v = 2*(root)*(root) - root + 2*root*r;
    //cout<<root<<" "<<v<<endl;
    while(v<t)
    {
        root++;
       v = 2*(root)*(root) - root + 2*root*r;
        //cout<<root<<" "<<v<<endl;
    }
    while(v>t)
    {
        root--;
        v = 2*(root)*(root) - root + 2*root*r;
        //cout<<root<<" "<<v<<endl;
    }
    return root;
}



int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);

    scanf("%d",&CASES);
    while(TEST<CASES)
    {
        scanf("%lld %lld",&r,&t);
        double alpha = 4.0*r*r;

        alpha = alpha - (24.0*r) + 36;

        alpha += (8.0*(t-2.0*r));
        alpha = sqrt(alpha);

        alpha -= (2.0*r-6);

        //long double beta = -(2*r-1)-(sqrt((4*r*r)+1-(4*r)+8*(t-1)));
        alpha/=4;

        //beta/=4;
        LL ret = check((LL)alpha-1);
        printf("Case #%d: %lld\n",++TEST,ret);


    }


}
