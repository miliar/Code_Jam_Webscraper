#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <sstream>
#include <limits>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <queue>
#include <deque>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <map>
#include <set>
#define PI (acos(-1.0))
#define Abs(a) (((a)<0) ? (-(a)) :(a) )
#define rep(i,n) for((i)=0;(i)<(n);(i)++)
#define Rep(i,n) for(int i=0;i<(n);i++)
#define Rrep(i,n) for(int i=((n)-1);i>=0;i--)
#define rrep(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define Pii pair<int,int>
#define PB push_back
#define Size(x) ((int)(x.size()))
using namespace std;
typedef long long mint;
typedef unsigned long long umint;
string ans[3][15];
enum player{r,p,s};
string make_choice(const string &a,const string &b)
{
    if(a<b)
        return a+b;
    return b+a;
}
string calc(int n,player cur)
{
    if(ans[cur][n]!="")
        return ans[cur][n];

    if(n==0)
    {
        if(cur==r)
        {
            ans[cur][n]="R";
        }
        else if(cur==p)
        {
            ans[cur][n]="P";
        }
        else
        {
            ans[cur][n]="S";
        }
        return ans[cur][n];
    }
    if(cur==r)
    {
        string a=calc(n-1,r),b=calc(n-1,s);
        ans[cur][n]=make_choice(a,b);
    }
    else if(cur==s)
    {
        string a=calc(n-1,s),b=calc(n-1,p);
        ans[cur][n]=make_choice(a,b);
    }
    else
    {
        string a=calc(n-1,p),b=calc(n-1,r);
        ans[cur][n]=make_choice(a,b);
    }
    return ans[cur][n];
}
string tryans(player val,int N,int rr,int pp,int ss)
{
    string ini=calc(N,val);
    for(int i=0;i<ini.size();i++)
    {
        if(ini[i]=='R')
            rr--;
        else if(ini[i]=='P')
            pp--;
        else
            ss--;
    }
    if(rr==0&&pp==0&&ss==0)
        return ini;
    else
        return "";
}
void getans(string &ansv,const string &cand)
{
    if(ansv==""||ansv<cand)
        ansv=cand;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    int T;
    cin>>T;
    //cout<<r<<" "<<p<<" "<<s<<endl;
    for(int t=1;t<=T;t++)
    {
        int n,rr,pp,ss;
        cin>>n>>rr>>pp>>ss;
        string ansv="";
        for(int i=0;i<3;i++)
        {
            string cand=tryans((player)i,n,rr,pp,ss);
            if(cand!="")
                getans(ansv,cand);
        }
        const string imp="IMPOSSIBLE";
        printf("Case #%d: ",t);

        if(ansv=="")
            cout<<imp<<endl;
        else
            cout<<ansv<<endl;
    }
    return 0;
}