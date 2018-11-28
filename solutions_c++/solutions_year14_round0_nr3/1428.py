//#include<bits/stdc++.h>
#include<iostream>
#include<sstream>
#include<string>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<cctype>
#include<set>
#include<bitset>
#include<algorithm>
#include<list>
#include<utility>
#include<functional>
#include <deque>
#include <numeric>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <assert.h>



#include<cmath>
#include<math.h>

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

using namespace std;

#define deb(a)      cerr<<" -> "<<#a<<"  "<<a<<endl;
#define popcount(a) (__builtin_popcountll(a))
#define SZ(a)       ((int)a.size())
#define fs           first
#define sc           second
#define pb          push_back
#define ll          long long
#define MP          make_pair
#define SS          stringstream
#define VS          vector<string>
#define VI          vector<int>
#define CON(a,b)  ((a).find(b)!=(a).end())
#define mem(a,b)    memset(a,b,sizeof(a))
#define memc(a,b)   memcpy(a,b,sizeof(b))
#define accu(a,b,c) accumulate((a),(b),(c))
#define fi(i,a,b)   for(i=a;i<b;i++)
#define fii(a,b)    for(i=a;i<b;i++)
#define fij(a,b)    for(j=a;j<b;j++)
#define fik(a,b)    for(k=a;k<b;k++)
#define fil(a,b)    for(l=a;l<b;l++)
#define ri(i,a)     for(i=0;i<a;i++)
#define rii(a)      for(i=0;i<a;i++)
#define rij(a)      for(j=0;j<a;j++)
#define rik(a)      for(k=0;k<a;k++)
#define ril(a)      for(l=0;l<a;l++)
#define fore(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
#define ERR         (1e-7)
#define EQ(a,b)     (fabs((a)-(b))<ERR)
#define all(a)      (a).begin(),(a).end()
#define rall(a)      (a).rbegin(),(a).rend()
#define p2(a)       (1LL<<a)
#define EX(msk,a)   (msk&p2(a))



//#define debug(args...)          {dbg,args; cerr<<endl;}
//#define debug(args...)          {cout<<" #--> ";dbg,args; cerr<<endl;}
#define debug(a...)          {cerr<<" #--> ";dbg,a; cerr<<endl;}

struct debugger
{
    ///Collected from rudradevbasak
    template<typename T> debugger& operator , (const T v)
    {
        cerr<<v<<" ";
        return *this;
    }
} dbg;


const double pi=acos(-1.0);
const double eps=1e-7;

template<class TT>TT sqr(TT a){return a*a;}
template<class TT>TT abs(TT a){if(a<0)  return -a;return a;}
template<class ZZ>ZZ max(ZZ a,ZZ b,ZZ c){return max(a,max(b,c));}
template<class ZZ>ZZ min(ZZ a,ZZ b,ZZ c){return min(a,min(b,c));}
typedef pair<int,int> pii;

//struct T
//{
//    int a,b,c;
//    T(int ai=0,int bi=0,int ci=0)
//    {
//        a = ai;
//        b = bi;
//        c = ci;
//    }
//
//};
//
//bool com(T a,T b)
//{
//    if()    return ;
//    return ;
//}


//typedef double type;
//struct P{
//    type x,y,z;
//    P(type xi=0,type yi=0,type zi=0):x(xi),y(yi),z(zi){};
//    void scan(){cin>>x>>y>>z;}
//    void scan1(){scanf("%lf%lf%lf",&x,&y,&z);}
//};


//bool operator < (const P &a,const P &b){return a>b;}
//bool com(P a,P b){return;}

//struct pq{int n,w;
//    pq(int nn=0,int ww=0):n(nn),w(ww){}
//    bool operator<(const pq &b) const{return w<b.w;}
//};

char bo[55][55];
char s = '*';


void print(int r,int c)
{
    bo[0][0] = 'c';
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
            printf("%c",bo[i][j]);
        printf("\n");
    }
}


bool get()
{
    int r,c,m,i,j;
    scanf("%d%d%d",&r,&c,&m);
    mem(bo,'.');


    if(r*c==m+1)
    {
        mem(bo,'*');
    }
    else if(r==1)
    {
        i=c-1;
        while(m-- && i>-1)
            bo[0][i--] = s;
    }
    else if(c==1)
    {
        i=r-1;
        while(m-- && i>-1)
            bo[i--][0] = s;
    }
    else
    {
        if((r==2 || c==2) && m%2==1)    return false;
        if(r*c<m+4)    return false;
        bool tst = true;
        int a,b,ns = r*c-m,re;

        for(i=2;i<=r;i++)
        {
            j = (ns+i-1)/i;
            if(j>c ||  j<2) continue;
            re = i*j-ns;
            //debug(i,j,re);
            if((i>2 && j>2 && re<i+j-4 ) || re==0)
            {
                tst = false;

                mem(bo,'*');
                for(a=0;a<i;a++)
                    for(b=0;b<j;b++)
                        bo[a][b] = '.';

                a = i-1;
                b = j-1;
                while(re > 0 && a>1)
                {
                    re--;
                    bo[a--][b] = s;
                }

                a= i-1;
                b = j-2;
                while(re > 0 && b>1)
                {
                    re--;
                    bo[a][b--] = s;
                }

                break;
            }

        }

        if(tst) return !tst;
    }
    print(r,c);
    return true;
}


//    freopen("in.txt","r",stdin);



int main()
{
//    freopen("in.txt","r",stdin);
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    //ios_base::sync_with_stdio(false);
    //std::cout << std::setprecision(13)<<b<<std::endl;
    int tks,ks=1,n,k,cnt,ans;

    scanf("%d",&tks);


    while(tks--)
    {
        printf("Case #%d:\n",ks++);
        if(!get())
        {
            printf("Impossible\n");
        }

    }

    return 0;
}
