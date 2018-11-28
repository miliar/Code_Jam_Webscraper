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
    ifstream in("B-large.in");
    ofstream out("output.txt");
    ll t, i, n, cnt, j=1;
    string S;
    in>>t;
    while(j<=t)
    {
        in>>S;
        n=S.size();
        out<<"Case #"<<j<<": ";
        cnt=0;
        for(i=1;i<n;i++)
            if(S[i-1]!=S[i])
                cnt++;
        if(S[n-1]=='-')
            cnt++;
        out<<cnt<<endl;
        j++;
    }
}
