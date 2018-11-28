# include <cstdio>
# include <iostream>
# include <map>
# include <list>
# include <map>
# include <vector>
# include <cstring>
# include <string>
# include <set>
# include <climits>
# include <cstdlib>
# include <algorithm>
# include <cmath>
# include<sstream>
# define  MAX 50005
# define  MOD 1000000007
# define  S(x)       scanf("%d",&x)
# define  SL(x)      scanf("%lld",&x)
# define  NL       printf("\n")
# define SP printf(" ")
# define  P(x)       printf("%d",x)
# define  PL(x)      printf("%lld",x)
# define  FOR(i,a)   for(i=0;i<a;i++)
# define  REP(i,a,b) for(i=a;i<=b;i++)
# define REP_IT(it,m) for(it=m.begin();it!=m.end();it++)
# define PB push_back
//string tostr(ll x)     { stringstream ss; ss << x; return ss.str(); }
//ll toint(string &s)    { stringstream ss; ss << s; long long x; ss >> x; return x; }
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
using namespace std;

bool row(vector<string >s,char c)
{
    int tmp;int i,j;
    FOR(i,4)
    {
        tmp=0;
        FOR(j,4)
        {
            if(s[i][j]==c ||s[i][j]=='T')
            tmp++;
        }
        if(tmp==4)
        return true;
    }
    return false;
}

bool col(vector<string >s,char c)
{
    int tmp;int i,j;
    FOR(j,4)
    {
        tmp=0;
        FOR(i,4)
        {
            if(s[i][j]==c ||s[i][j]=='T')
            tmp++;
        }
        if(tmp==4)
        return true;
    }
    return false;
}

bool diag1(vector<string >s,char c)
{
    int tmp=0;int i,j;
    FOR(i,4)
    {

        if(s[i][i]==c ||s[i][i]=='T')
        tmp++;

    }
    if(tmp==4)
        return true;
    return false;
}
bool diag2(vector<string >s,char c)
{
    int tmp=0;int i,j;
    FOR(i,4)
    {

        if(s[3-i][i]==c ||s[3-i][i]=='T')
        tmp++;

    }
    if(tmp==4)
        return true;
    return false;
}

bool won(vector<string >s,char c)
{
    return (row(s,c)||col(s,c)||diag1(s,c)||diag2(s,c));
}

bool complete(vector<string >s)
{
    int i,j;
    FOR(i,4)
    {
        FOR(j,4)
        {
            if(s[i][j]=='.')
            return false;
        }
    }
    return true;
}
int main()
{

freopen("A-large.in","rt",stdin);
freopen("out.txt","wt",stdout);
int i,j,t,test;
string str;

scanf("%d\n",&test);
REP(t,1,test)
{
    vector<string >s;
    FOR(i,4)
    {
        cin>>str;
        s.PB(str);
    }/*
    FOR(i,4)
    {
        FOR(j,4)
        {
            printf("%c",s[i][j]);
        }
        NL;
    }*/
    if(won(s,'X'))
    cout<<"Case #"<<t<<": X won\n";
    else if(won(s,'O'))
    cout<<"Case #"<<t<<": O won\n";
    else if(!complete(s))
    cout<<"Case #"<<t<<": Game has not completed\n";

    else
    cout<<"Case #"<<t<<": Draw\n";
//    cin>>str;//cout<<str;NL;
}
return 0;
}
