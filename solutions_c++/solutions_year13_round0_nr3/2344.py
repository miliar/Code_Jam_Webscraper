#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <string.h>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>
#include <queue>

#define X first
#define Y second
#define ll long long

using namespace std;

bool check(ll x)
{
     int mas[111];
     mas[0]=0;
     while ( x>0 )
     {
           mas[0]++;
           mas[mas[0]]=x%10;
           x/=10;      
     }     
     int st=1, fin=mas[0];
     while (st<fin)
     {
           if ( mas[st]!=mas[fin] )
              return 0;
           st++; fin--;           
     }
     return 1;
}
vector<ll>v;
int main ()
{
    freopen("C-large-1.in", "r", stdin);
    freopen("C-large-1.out", "w", stdout);
    for (ll i=1; i<=30000000; i++)
    {
        if ( check(i) && check(i*i) )
           v.push_back(i*i);
    }   
    int n;
    cin>>n;
    for (int i=1; i<=n; i++)
    {
        ll A, B, ans=0;
        cin>>A>>B;
        for (int j=0; j<v.size(); j++)
            ans+=( v[j]>=A && v[j]<=B );
        printf("Case #%d: ", i);
        cout<<ans<<endl;
    }
    return 0;
}
