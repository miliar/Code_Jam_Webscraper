#include<iostream>
#include<algorithm>
using namespace std;
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include <vector>
#include<queue>
#include<bitset>
#define ll long long
typedef pair<int, int > pii;
#define pb push_back
#define mk make_pair
#define rep(p,q,r) for(int p=q;p<r;p++)
vector<int> v[100010];

int vis[100002]={0};

int main()
{
    ll t,n,x,s,cas=1;
    cin>>t;
    while(t--)
    {
        bitset<10> b;
        scanf("%lld",&x);
        for(int i=0;i<10;i++)
            b[i]=0;
        int f=0;
        s=0;
        while(f==0)
        {
            if(s==s+x)
                break;
            s+=x;
            n=s;
            while(n>0)
            {
                b[n%10]=1;
                n/=10;
            }
            n=0;
            for(int i=0;i<10;i++)
                n+=b[i];
            if(n==10)
                {f=1;break;}
        }

        printf("Case #%d: ",cas);
        if(f==0)
            printf("INSOMNIA\n");
        else
            printf("%lld\n",s);
            cas++;
    }
}

