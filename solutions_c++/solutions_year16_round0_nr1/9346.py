#include <stdio.h>
#include <stdlib.h>
#include <bits/stdc++.h>

//type definitions
#define rep(a,b) for(int i=a;i<=b;i++)
#define rev(a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define in(n) scanf("%d",&n)

///STL
#define vi vector<int>
#define vvi vector< vector<int> >
#define pb push_back
#define mp make_pair
#define mii map<int,int>
#define pii pair<int,int>
#define f first
#define s second

//Iterator!
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it++)

/// Constants
#define ll long long
#define mod 1000000007
#define EPS 1e-7
#define sqr(x) ((x)*(x))
#define sqrt(x) sqrt(1.0*(x))
/// Files.
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

using namespace std;


vector <bool> vis(10);
void Clear();
bool check();

int main()
{
    ofstream outfile;
    ifstream inpfile;
    inpfile.open("A-large.in");
    outfile.open("prob1.txt");
    int tests;
    inpfile>>tests;
    ll i=1;
    ll num;
    int cunt=1;
    int t;
    while(tests--)
    {
        inpfile>>t;
        if(t==0)
        {
            outfile<<"Case #"<<cunt<<": INSOMNIA"<<endl;
            cunt++;
            continue;
        }
        while(check())
        {
            num = t*i;
            ll tmp=num;
            while(tmp)
            {
                vis[tmp%10]=true;
                tmp/=10;
            }
            i++;
        }
        i=1;
        outfile<<"Case #"<<cunt<<": "<<num<<endl;
        cunt++;
        Clear();
    }

    return 0;
}
bool check()
{
    rep(0 , 9)
        if(!vis[i])
            return true;
    return false;
}

void Clear()
{
    rep(0 , 9)
        vis[i]=false;
}
