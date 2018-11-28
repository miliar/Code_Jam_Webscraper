#include <iostream>
#include <set>
#include <stdio.h>
#include <stdlib.h>
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define LL long long
using namespace std;
int solve()
{
    string S;
    cin>>S;
    int l = S.length();
    int result = 0;
    int p=0,n=0;
    while(1)
    {
    while(p<l && S.at(p)=='+') p++;
    if (p>=l)
        break;
    if (n !=p) result++;
    n = p;
    while(n<l &&  S.at(n)=='-') n++;
    if (n !=p) result++;
    p=n;

}

    return result;

}
int main()
{
    //solve();
    //return 0;
    freopen("/home/happylife/programing/code_jam//B-small-attempt0.in","r",stdin);
    freopen("/home/happylife/programing/code_jam/B-small-attempt0.out","w",stdout);
    int N;
    cin>>N;
    REP(I,N)
    {
        cout<<"Case #"<<I+1<<": " << solve()<< endl;
    }

    return 0;
}
