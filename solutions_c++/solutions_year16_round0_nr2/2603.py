//created by shikhar vishnoi

#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <string.h>
#include <math.h>
#define ll long long
#define pb push_back
#define iosync ios_base::sync_with_stdio(false);cin.tie(0);
const ll mod=1000000007;
const double pi=3.14159265358979323846;
using namespace std;

ll solve (string s)
{
    ll plus=0,minus=0,i=0;
    char ch;
    while(i<s.size())
    {
        ch=s[i];
        while(s[i] == ch)
            i++;
        if(ch == '+')
            plus++;
        if(ch == '-')
            minus++;
    }
    if(plus == 1 && minus == 0)
        return 0;
    else if(minus == 1 && plus == 0)
        return 1;
    else if (ch=='+')
        return (plus+minus-1);
    else
        return (plus+minus);
}

int main ()
{
    
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
    iosync
    ll T;
    cin>>T;
    for(ll t=1; t<=T; t++)
    {
        string s;
        cin>>s;
        cout<<"Case #"<<t<<": "<<solve(s)<<endl;
    }
    return 0;
}