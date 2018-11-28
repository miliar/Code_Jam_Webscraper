#include <bits/stdc++.h>

#define mod 1000000007
#define inf 1000000000000
#define root2 1.41421
#define root3 1.73205
#define pi 3.14159
#define MAX 100001
#define ll long long int
#define ss(n) scanf("%lld", &n)
#define ssf(n) scanf("%lf", &n)
#define gc getchar
#define pb push_back
using namespace std;

int main()
{
    ifstream in("D-small-attempt0.in");
    ofstream out("output.txt");
    ll t, i, k, j=1, s, c;
    in>>t;
    while(j<=t)
    {
        in>>k>>c>>s;
        out<<"Case #"<<j<<": ";
        for(i=0;i<k;i++)
        {
            out<<i+1;
            if(i<k-1)
                out<<" ";
        }
        out<<endl;
        j++;
    }
}

