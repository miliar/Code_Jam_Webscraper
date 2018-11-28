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
#include<unordered_set>
#include<unordered_map>



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
#define VD          vector<double>
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


vector< vector<string> > senS;
vector< vector<int> > sen;

map<string,int>mp;
char ar[20000];

int ans()
{
    sen.clear();
    senS.clear();
    mp.clear();

    int n,i,j,k,msk;

    cin>>n;
    gets(ar);

    rii(n)
    {
        gets(ar);
        string s=ar;
        SS ss(s);
        VS cur;
        while(ss>>s)
        {
            cur.pb(s);
            mp[s]=0;
        }
        senS.pb(cur);
    }

    int words=0;

    fore(it,mp)
        it->sc=words++;


    rii(n)
    {
        VI cur;

        rij(SZ(senS[i]))
            cur.pb(mp[ senS[i][j] ]);

        sen.pb(cur);
    }

    VI per(words,0);
//    deb(words);
    rii(2)
    {
        rij(SZ(sen[i]))
            per[ sen[i][j] ]|=p2(i);
    }

    int ans=0;

    rii(words)
        if(per[i]==3)
                ans++;

    if(n==2)    return ans;
    ans=1000000;
    int ind,e,now;
    VI tmp;
    int kk=n-2;

    for(msk=0;msk<p2(kk);msk++)
    {
        tmp=per;
        rii(n-2)
        {
            if(EX(msk,i))
                e=1;
            else e=2;
            ind=i+2;

            rij(SZ(sen[ind]))
                tmp[ sen[ind][j] ]|=e;

        }

        now=0;
         rii(words)
            if(tmp[i]==3)
                now++;
        //deb(now);
        ans=min(ans,now);
    }

    return ans;
}


int main()
{
//    ios_base::sync_with_stdio(0);cin.tie(0);
//    cout << fixed << setprecision(3) << (-20/3.0) << endl;
//    cout << setprecision(10)<<(-20/3.0)<<std::endl;


//    freopen("in.in","r",stdin);
    freopen("C-small-attempt0.in","r",stdin);
//    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.in","w",stdout);




    int i,j,k,tks=1,ks=1,n;

    cin>>tks;



    while(tks--)
    {
        n=ans();
        printf("Case #%d: %d\n",ks++,n);
    }


    return 0;
}




