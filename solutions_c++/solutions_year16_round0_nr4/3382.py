#include<bits/stdc++.h>
#define mp make_pair
#define PII pair<int,int>
#define fi first
#define se second
using namespace std;

const int NMAX=105;

int t,k,s,c;

int main()
{
    int i,j;
    freopen("date.in","r",stdin);
    freopen("date.out","w",stdout);
    cin.sync_with_stdio(false);
    cin>>t;
    for (j=1;j<=t;j++)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<j<<": ";
        while (s) {cout<<s<<" ";s--;}
        cout<<"\n";
    }
    return 0;
}

