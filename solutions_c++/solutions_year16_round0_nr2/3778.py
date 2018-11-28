//OUM HARI OUM, OUM TATSAT
// OUM NAMA VAGABATE BASUDEBAY
// OUM NAMA MA SWARASATI OUM NAMA

#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<stdlib.h>
#include<iostream>
#include<algorithm>

#define cl(vctr) vctr.clear()
#define ms(v, ar) memset(ar, v, sizeof(ar))

const double pi=(double)(2.0 * acos( 0.0 ));
const int inf=1 << 30;
const double eps=1E-9;
const double e = exp(1.0);
const int sz=100000 + 5;
const int mod=1000000000 + 7;

using namespace std;
typedef long long int ll;

vector<bool> s;
char n[105];
int m[205],dis[255];

int main()
{
    freopen("Bin.in","r",stdin);
    freopen("Bout.in","w",stdout);
    int t,T,i,j,l,u,v,ls,gr,res;
    scanf("%d",&t);
    T=t;
    while(t--)
    {
        scanf("%s",&n);
        l=strlen(n);
//        for(i=0,j=(1<<l)+1;i<j;i++) dis[i]=inf;
//        queue<int> Q;
//        Q.push(n);
//        dis[n]=0;
//        while(!Q.empty())
//        {
//            u=Q.front();Q.pop();
//            for(i=0;i<l;i++)
//            {
//                v=u^m[i];
//                if(dis[v]>1+dis[u])
//                    dis[v]=1+dis[u],Q.push(v);
//            }
//        }
//        res=dis[(1<<l)-1];
     n[l]=0;
     gr=0;
     ls=0;
    for(i=0;i<l;i++)
    {
        if(n[i]!=n[1+i])
            {
                gr++;
                if(n[i]=='-') ls=gr;
            }
    }
    res=ls;
        printf("Case #%d: %d\n",T-t,res);
    }

//    int i;
//    for(i=0;i<100;i++)
//    {
//        if(i&1) printf("-");
//        else printf("+");
//    }
//
//    printf("\n");

    return 0;
}
