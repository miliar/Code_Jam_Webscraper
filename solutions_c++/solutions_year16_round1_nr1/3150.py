#include<iostream>
#include<cstdio>
#include<climits>
#include<algorithm>
#include<string>
#include<cstring>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<bitset>
#include<cmath>

#define f(i,a,b) for(int i=a;i<b;i++)
#define b(i,a,b) for(int i=a;i>b;i--)
#define mpr(a,b) make_pair(a,b)
#define pr pair<int,int>
#define si(a) scanf("%d",&a)
#define sll(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define newline printf("\n")
#define ll long long 
using namespace std;
main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    string s;
    cin>>t;
    f(j,1,t+1)
    {
        cin>>s;string n;
        int l=s.length();
        n=n+s[0];char c=s[0];
        f(i,1,l)
        {
            if(c>s[i])
                n=n+s[i];
            else
                n=s[i]+n;
            c=n[0];
        }
        cout<<"Case #"<<j<<": "<<n<<"\n";
    }
}
    
