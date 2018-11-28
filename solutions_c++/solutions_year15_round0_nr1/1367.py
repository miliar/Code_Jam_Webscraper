#include<iostream>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#include<set>
#define ll long long int
#define mk make_pair
#define pb push_back
using namespace std;


int main()
{
    int t,w=1;
    freopen("input.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        int i,j,k,l,m,n,d,arr[1111]={0},co=0,ans=0;
        cin>>n;
        string s;
        cin>>s;
        for(i=0;i<=n;i++)
        {
            if(co<i)
            {
                ans+=i-co;
                co=i;
            }
            co+=s[i]-'0';
        }
        cout<<"Case #"<<w<<": "<<ans<<"\n";
        w++;
    }
    return 0;
}
