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
//#include<unordered_set>
//#include<unordered_map>



#include<cmath>
#include<math.h>

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>

using namespace std;

#define deb(a)      cerr<<"#"<<__LINE__<<" -> "<<#a<<"  "<<a<<endl;
#define popcount(a) (__builtin_popcountll(a))
#define SZ(a)       ((int)a.size())
#define fs           first
#define sc           second
#define pb          push_back
#define ll          long long
#define ld          long double
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




#define debug(a...)          {cout<<" #--> ";dbg,a; cout<<endl;}

struct debugger
{
    ///Collected from rudradevbasak
    template<typename T> debugger& operator , (const T v)
    {
        cout<<v<<" ";
        return *this;
    }
} dbg;


const double pi=acos(-1.0);
const double eps=1e-7;

template<class TT>TT sqr(TT a){return a*a;}
template<class TT>TT abs(TT a){if(a<0)  return -a;return a;}
typedef pair<int,int> pii;


const int S=10001;
short val[S][S];
char ar[S+5];
char inp[S+5];

///i=2
///j=3
///k=4

int ev[5][5]={
    {0,0,0,0,0},
    {0,1,2,3,4},
    {0,2,-1,4,-3},
    {0,3,-4,-1,2},
    {0,4,3,-2,-1},
};

int get(int x)
{
    if(x=='i')  return 2;
    if(x=='j')  return 3;
    if(x=='k')  return 4;
    return x;
}

int getVal(int x,int y)
{
    if(x*y<0)   return -ev[abs(x)][abs(y)];
    return ev[abs(x)][abs(y)];
}

bool isPossible(int l,int n)
{
    int len=0;
    for(int i=0;i<n;i++)
    {
        strcpy(&ar[len],inp);
        len+=l;
    }

    for(int i=0;i<len;i++)
        ar[i] = get(ar[i]);

    for(int i=0;i<len;i++)
    {
        val[i][i]=ar[i];
        for(int j=i+1;j<len;j++)
            val[i][j]=getVal(val[i][j-1],ar[j]);
    }

    for(int i=0;i<len;i++)
    {
        if(val[0][i]!=2)    continue;
        for(int j=i+1;j<len-1;j++)
            if(val[i+1][j]==3 && val[j+1][len-1]==4)
                return true;
    }


    return false;
}

int main()
{
//    freopen("in.in","r",stdin);


    freopen("C-small-attempt0.in","r",stdin);
//    freopen("B-large.in","r",stdin);

    freopen("out.in","w",stdout);


//    ios_base::sync_with_stdio(0);cin.tie(0);
//    cout << fixed << setprecision(3) << (-20/3.0) << endl;
//    cout << setprecision(10)<<(-20/3.0)<<std::endl;

    int i,j,k,tks=1,ks=1,l,n,ans;


    scanf("%d",&tks);
    while(tks--){
        scanf("%d%d",&l,&n);
        scanf("%s",inp);
        printf("Case #%d: ",ks++);

        bool flag=isPossible(l,n);
        if(flag)puts("YES");
        else puts("NO");
    }

    return 0;
}




