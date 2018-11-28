#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define int64 unsigned long long
#define INF numeric_limits<int64>::max()
#define lsb(x) (-x)&x
using namespace std;
int solve(string s)
{
    int flips=0;
    for(int i=(int)s.size()-1;i>=0;i--)
    {
        char x=s[i];
        if(flips%2==1)
            x=(x=='+' ? '-' : '+');
        if(x=='-')
            flips++;
    }
    return flips;
}
int main()
{
    int Tests;
    cin>>Tests;
    for(int t=1;t<=Tests;t++)
    {
        string s;
        cin>>s;
        cout<<"Case #"<<t<<": "<<solve(s)<<'\n';
    }
    return 0;
}

