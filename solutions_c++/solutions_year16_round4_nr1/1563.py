#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <cctype>
#include <set>
#include <bitset>
#include <algorithm>
#include <list>
#include <utility>
#include <functional>
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


//#include<unordered_set>
//#include<unordered_map>

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
#define fii(a,b)    for(int i=a;i<b;i++)
#define fij(a,b)    for(int j=a;j<b;j++)
#define fik(a,b)    for(int k=a;k<b;k++)
#define fil(a,b)    for(int l=a;l<b;l++)
#define ri(i,a)     for(int i=0;i<a;i++)
#define rii(a)      for(int i=0;i<a;i++)
#define rij(a)      for(int j=0;j<a;j++)
#define rik(a)      for(int k=0;k<a;k++)
#define fore(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)
#define ERR         (1e-7)
#define EQ(a,b)     (fabs((a)-(b))<ERR)
#define all(a)      (a).begin(),(a).end()
#define rall(a)      (a).rbegin(),(a).rend()
#define p2(a)       (1LL<<a)
#define EX(msk,a)   (msk&p2(a))
#define isInRange(v,l,h) (min(l,h)<=v && v<=max(l,h))


#define __LOCAL__

#ifdef __LOCAL__
	#define deb(a)      cerr<<"#"<<__LINE__<<" -> "<<#a<<"  "<<a<<endl;
	// #define deb(a)      cout<<"#"<<__LINE__<<" -> "<<#a<<"  "<<a<<endl;
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
#else

#define deb(a) ;
#define debug(a...)  ;

#endif



const double pi=acos(-1.0);
const double eps=1e-7;

template<class TT>TT sqr(TT a){return a*a;}
template<class TT>TT abs(TT a){if(a<0)  return -a;return a;}
typedef pair<int,int> pii;
int win[200][200];


bool check(string &s)
{
    int n = SZ(s);
    string cur="";
    string old =s;

    while(SZ(old)>1)
    {
        cur="";
        for(int i=0;i<SZ(old); i+=2)
            if(old[i]==old[i+1])
                return false;
            else cur+=win[old[i]  ][old[i+1] ];

        old = cur;
    }
    return true;
}



int main()
{
//    ios_base::sync_with_stdio(0);cin.tie(0);
//    cout << fixed << setprecision(3) << (-20/3.0) << endl;
//    cout << setprecision(10)<<(-20/3.0)<<std::endl;


//    freopen("in.in","r",stdin);
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);

    int i,j,n,m;
    win['R']['P'] = win['P']['R']= 'R';
    win['P']['S'] = win['S']['P']= 'P';
    win['S']['R'] = win['R']['S']= 'S';

    int tks,ks=1;
    int ar[3];
    cin>>tks;
    while(tks--)
    {
        cin>>n;
        rii(3)
            cin>>ar[i];

        string s="";

        rii(ar[0])  s+='R';
        rii(ar[1])  s+='P';
        rii(ar[2])  s+='S';

        sort(all(s));
//        deb(s);

        string ans="ZZZZ";




        do{
            bool ch=check(s);
            if(ch && s<ans)
                ans = s;
        }while(next_permutation(all(s)));


        if(ans=="ZZZZ")
            cout<<"Case #"<<ks<<": IMPOSSIBLE\n";
        else cout<<"Case #"<<ks<<": "<<ans<<"\n";

        ks++;
    }

    return 0;
}




