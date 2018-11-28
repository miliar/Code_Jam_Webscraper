#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define ll long long
#define mod 1000000007LL
#define pil pair<int,ll>
#define pli pair<ll,int>
#define pll pair<ll,ll>
#define all(v) v.begin(),v.end()
#define inf 1000000000
#define N 112345
vector<string>v,v1;
int main()
{
    freopen("2.in","r",stdin);
    freopen("2-out.txt","w",stdout);
    int t,cs=1;
    scanf("%d",&t);
    while(t--)
    {
        int i,j,k,n,m;
        string s;
        cin>>s;
        n=s.size();
        v.clear();
        string h="";
        h+=s[0];
        for(i=1;i<n;i++)
            if(s[i]<h[0])
                h+=s[i];
            else
                h=s[i]+h;
        printf("Case #%d: ",cs);
        cout<<h<<endl;
        cs++;
    }
    return 0;
}

