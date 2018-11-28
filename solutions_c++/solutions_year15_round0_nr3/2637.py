#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cmath>
#include <ctype.h>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <list>
#include <limits.h>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <string>
#include <string.h>
#include <time.h>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> ipair;
typedef vector<int> vi;

void FJ(){
    #ifndef ONLINE_JUDGE
        freopen("I.txt","r",stdin);
    #endif
}

#define MAX 1000000007
#define MOD 1000000007
#define FT first
#define SE second
#define SZ size()
#define BG begin()
#define EN end()
#define SP system("pause")
#define PB(a) push_back(a)
#define rep(i,n) REP(i,0,n)
#define MP(a,b) make_pair(a,b)
#define PT(a) printf("%d\n",a)
#define GT(a) int a;scanf("%d",&a)
#define MS(a,b) memset(a,b,sizeof(a))
#define FI freopen("I.txt","r",stdin)
#define FO freopen("O.txt","w",stdout)
#define rev(i,n) for(int i=n;i>=0;i--)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define take(ar,n) int ar[n]; rep(i,n) cin>>ar[i]
#define foreach(V,it) for(typeof((V).BG)it=(V.BG);it!=V.EN;it++)
pair<char,int> PR(pair<char,int> a,char b)
{
    if(a.FT=='1') return MP(b,a.SE);
    if(b=='1')    return MP(a.FT,a.SE);
    if(a.FT==b) return MP('1',a.SE*(-1));
    if(a.FT=='i' && b=='j') return MP('k',a.SE);
    if(a.FT=='j' && b=='i') return MP('k',a.SE*(-1));
    if(a.FT=='j' && b=='k') return MP('i',a.SE);
    if(a.FT=='k' && b=='j') return MP('i',a.SE*(-1));
    if(a.FT=='i' && b=='k') return MP('j',a.SE*(-1));
    if(a.FT=='k' && b=='i') return MP('j',a.SE);
}
void show(pair<char,int>P)
{
    if(P.SE==1) printf("%c\n",P.FT);
    else printf("-%c\n",P.FT);
}
pair<char,int> PC(pair<char,int> A,pair<char,int> B)
{
    if(A.FT=='1')
    {
        if(B.FT=='1') return MP('1',A.SE*B.SE);
        if(B.FT=='i') return MP('i',A.SE*B.SE);
        if(B.FT=='j') return MP('j',A.SE*B.SE);
        if(B.FT=='k') return MP('k',A.SE*B.SE);
    }
    else if(A.FT=='i')
    {
        if(B.FT=='1') return MP('i',A.SE*B.SE);
        if(B.FT=='i') return MP('1',-1*A.SE*B.SE);
        if(B.FT=='j') return MP('k',A.SE*B.SE);
        if(B.FT=='k') return MP('j',-1*A.SE*B.SE);
    }
    else if(A.FT=='j')
    {
        if(B.FT=='1') return MP('j',A.SE*B.SE);
        if(B.FT=='i') return MP('k',-1*A.SE*B.SE);
        if(B.FT=='j') return MP('1',-1*A.SE*B.SE);
        if(B.FT=='k') return MP('i',A.SE*B.SE);
    }
    else if(A.FT=='k')
    {
        if(B.FT=='1') return MP('k',A.SE*B.SE);
        if(B.FT=='i') return MP('j',A.SE*B.SE);
        if(B.FT=='j') return MP('i',-1*A.SE*B.SE);
        if(B.FT=='k') return MP('1',-1*A.SE*B.SE);
    }

}
int main()
{
    FJ();
    FO;
    GT(test);
	rep(zz,test)
	{
        printf("Case #%d: ",zz+1);
        int l,x;
        cin>>l>>x;
        string s,r;
        cin>>s;
        rep(i,x) r+=s;
        int n=r.size();
        pair<char,int> rr[n+7];
        map<char,int> mp;
        rr[0].FT=r[0];
        mp[r[0]]++;
        rr[0].SE=1;
        REP(i,1,n) rr[i]=PR(rr[i-1],r[i]),mp[r[i]]++;
        if(mp.size()==1)
        {
            puts("NO");
            continue;
        }
//        REP(i,0,n) show(rr[i]);
        bool did=false;
        for(int i=0;i<n;i++)
        {
            if(rr[i].FT=='i' && rr[i].SE==1)
            {
                for(int j=i+1;j<n;j++)
                {
                    pair<char,int> P1=PC(rr[j],rr[i]),P2=PC(PC(rr[j],rr[i]),PC(rr[n-1],rr[i])) ;
                    if(P1==MP('j',1) && P2==MP('k',1))
                    {
                        did=true;
                        break;
                    }
                }
            }
            if(did) break;
        }
        if(did) puts("YES");
        else puts("NO");
	}
    return 0;
}
