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

char x[100];
bool undone();
int len=0;
int main()
{
    ofstream outfile;
    ifstream inpfile;
    inpfile.open("B-large.in");
    outfile.open("prob1.txt");
    int t;
    inpfile >> t;
    string state;
    int cunt=1;
    int res=0;
    while(t--)
    {
        inpfile>>state;
        len = state.length();
        rep(0 , state.length()-1)
        {
            x[i] = state[i];
        }
        while(undone())
        {
            int i=1;
            if(len==1)
            {
                if(x[0]=='-')
                    x[0]='+';
                else
                    res++;
                x[0]='+';
                res++;
            }
            else
            {
                if(x[0]=='-')
                {
                    for(i=0; i<len && x[i]!='+'; i++)
                    {
                        x[i] = '+';
                    }
                    res++;
                }
                else
                {
                    for(i=0; i<len && x[i]!='-'; i++)
                    {
                        x[i]='-';
                    }
                    res++;
                    for(int j=0; x[j]!='+' && j<len; j++)
                    {
                        x[j] = '+';
                    }
                    res++;
                }
            }
        }
        outfile<<"Case #"<<cunt<<": "<<res<<endl;
        cunt++;
        res=0;
    }

    return 0;
}

bool undone()
{
    rep(0 , len-1)
        if(x[i]=='-')
            return true;
    return false;
}
