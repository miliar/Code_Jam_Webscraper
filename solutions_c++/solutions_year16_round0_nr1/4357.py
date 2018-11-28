#include <iostream>
#include <set>
#include <stdio.h>
#include <stdlib.h>
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define LL long long
using namespace std;
string solve()
{
    LL N,n2;
    bool f_flag;
    cin>>N;
    if (N == 0) return "INSOMNIA";
    string stringtmp;
    char chartmp[20];
    set<char> charset;
    FOR(I,1,1000)
    {
        n2 = N * I;
        sprintf(chartmp,"%lld", n2);
        stringtmp = chartmp;
        for (char i: stringtmp)      charset.insert(i);
        f_flag = true;
        FOR(J,48,58)
        {
            if (charset.find(char(J)) == charset.end())
            {
                f_flag = false;
                break;
            }
        }
        if (f_flag)        break;
    }
    sprintf(chartmp,"%lld", n2);
    stringtmp = chartmp;
    return stringtmp;

}
int main()
{
//    solve();
//    return 0;
    freopen("/home/happylife/programing/code_jam/A-small-attempt0.in","r",stdin);
    freopen("/home/happylife/programing/code_jam/A-small-attempt0.out","w",stdout);
    int N;
    cin>>N;
    REP(I,N)
    {
        string rst = solve();
        cout<<"Case #"<<I+1<<": " << rst<< endl;
    }

    return 0;
}
