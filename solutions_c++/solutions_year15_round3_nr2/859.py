#include <bits/stdc++.h>
using namespace std;

#define FOR(p,star,end) for(int p = star ; p<end ; p++)
#define FORR(p,star,end) for(int p = star ; p>=end ; p--)
#define INF 1000000000
#define MOD 1000000007
#define MAX 101
#define LOGMAX 14
#define pi pair<int ,int >
#define vi vector<int>
#define vp vector< pair<int ,int> >
#define vii vector< vector<int> >
#define vip vector<vector<pair<int , int > > >
#define pb push_back
#define mp make_pair
#define ll long long
#define sz(v) ((int)v.size())
#define f first
#define s second
#define EPS 10-7

using namespace std;
int k , l , s;
string Key,tar;
double ans ;
double Maxi;
double B;
vector<string>All;
map<double,double>M;
double Rem(string c)
{
    double res=Maxi;
    FOR(i,0,c.size()-l+1)
    {
        string tem="";
        FOR(j,i,i+l)
        tem+=c[j];
        if(tem==tar)
            res--;

    }
    return res;
}
double Get(string c)
{
    double res=0.0;
    FOR(i,0,c.size()-l+1)
    {
        string tem="";
        FOR(j,i,i+l)
        tem+=c[j];
        if(tem==tar)
            res++;

    }
    return res;
}


void go ( string c, int rem)
{


    if(rem==0)
    {
        Maxi = max(Maxi,Get(c));
        // cout << c <<endl;
        All.pb(c);
        return;

    }

    FOR(i,0,k)
    go(c+Key[i],rem-1);


}
/*
void build()
{
    int Oc[30];
    memset(Oc,0,sizeof Oc);
    FOR(i,0,Key.size())
    Oc[Key[i]-'A']++;
    double Base = Key.size()*1.0;
    FOR(i,0,30)
    P[i]=(Oc[i]*1.0)/Base;

}*/
int main ()
{

    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin >> t;
    FOR(tc,1,t+1)
    {
        Maxi=0.0;
        B=0.0;

        ans=0.0;
        cin >> k >> l >> s;
        cin >> Key ;
        cin>> tar;
        // build();



        go("",s);
        FOR(i,0,All.size())
        {
            M[Rem(All[i])]++;
            B++;
        }
        //  cout << B << "here ";
        if(B>0.0)
        {
            for(map<double,double>::iterator it = M.begin(); it!=M.end(); it++)
                ans+=((it->second)/B)*(it->first);
        }
        printf("Case #%d: %.6lf\n",tc,ans);

        All.clear();
        M.clear();

    }
}
