#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define INF numeric_limits<int>::max()
#define int64 long long
#define lsb(x) (x)&(-x)
using namespace std;
//ifstream in("1.in");
string digits[]={ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int d[30][30],freq[30],sol[30],st[30];
bool foundSol;
void solve(int k)
{
    if(foundSol==true)
        return;
    if(k==0)
    {
        foundSol=true;
        for(int i=0;i<=9;i++)
            sol[i]=st[i];
        return;
    }
    else for(int i=0;i<=9;i++)
    {
        bool ok=true;
        for(int j=0;j<=27;j++)
        if( d[i][j] > freq[j])
        {
            ok=false;
            break;
        }
        if(ok==false)
            continue;
        int newK=0;
        for(int j=0;j<=27;j++)
        {
            freq[j]-=d[i][j];
            newK+=freq[j];
        }
        st[i]++;
        solve(newK);
        st[i]--;
        for(int j=0;j<=27;j++)
            freq[j]+=d[i][j];

    }
}
int main()
{
    int NT;
    for(int i=0;i<=9;i++)
    for(int j=0;j<(int)digits[i].size();j++)
        d[i][ digits[i][j]-'A' ]++;
    cin>>NT;
    for(int t=1;t<=NT;t++)
    {
        for(int i=0;i<=27;i++)
            freq[i]=sol[i]=st[i]=0;
        string s;
        cin>>s;
        for(int i=0;i<(int)s.size();i++)
            freq[ s[i]-'A' ]++;
        foundSol=false;
        solve( (int)s.size() );
        cout<<"Case #"<<t<<": ";
        for(int i=0;i<=9;i++)
        for(;sol[i]>0;sol[i]--)
            cout<<i;
        cout<<'\n';
    }
    return 0;
}
