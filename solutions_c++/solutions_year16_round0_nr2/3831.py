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
int find_length(bool bits[],bool a,int s)
{
    int l=0,i=0;
    while(i<s&&bits[i++]==a)
        l++;
    return l;
}
main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;cin>>t;
    f(k,1,t+1)
    {
        bool bits[101];
        string s;
        cin>>s;
        f(i,0,s.length())
        {
            if(s[i]=='+')
                bits[i]=1;
            else
                bits[i]=0;
        }int time=0,l=0;
        while(l<s.length())
        {
            l=find_length(bits,bits[0],s.length());
            if(bits[0]==0)
            {
                f(i,0,l)
                bits[i]=1;
                time++;
            }
            else
            {
                if(l<s.length())
                {
                    f(i,0,l)
                    bits[i]=0;
                    time++;
                }
            }
        }
        cout<<"Case #"<<k<<": "<<time<<"\n";
    }
}
            
                
