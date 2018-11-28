#include<bits/stdc++.h>
using namespace std;
int t;
void solve(int tc)
{
    double c,f,x;
    cin>>c>>f>>x;
    double waittimetofarm,waittimetoend;
    double cps=2.0,at=0;
    waittimetofarm=c/cps;
    waittimetoend=x/cps;
    //cout<<waittimetoend<<" "<<waittimetofarm+x/(cps+f)<<"\n";
    while(waittimetoend>waittimetofarm+x/(cps+f))
    {

        at+=waittimetofarm;
        cps+=f;
        waittimetoend=x/cps;
        waittimetofarm=c/cps;
        //cout<<"Cookies per sec "<<cps<<"\n";
        //cout<<waittimetoend<<" "<<waittimetofarm+x/(cps+f)<<" "<<at<<"\n";
    }
    at+=waittimetoend;
    cout<<"Case #"<<tc<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<at<<"\n";
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        solve(i);
    }
}
