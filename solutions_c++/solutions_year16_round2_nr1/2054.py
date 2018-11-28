// Copyright 2015 © Ayush Garg
// All rights reserved.
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define rep(i,x,y) for(i=x;i<y;i++)
#define f first
#define s second
#define si(x)   scanf("%d",&x)
#define sl(x)   scanf("%I64d",&x)
#define author ayushgarg
#define CLR(x)  memset(x,0,sizeof(x))
#define RESET(x,a) memset(x,a,sizeof(x))
#define pi pair<int,int>
#define pb push_back
#define mp make_pair
#define debug(x) cout<<">value ("<<#x<<") : "<<x<<endl;
#define mod 1000000007

string s,s2;
string l[12]={"TWO","EIGHT","SIX","ZERO","FOUR","FIVE","SEVEN","THREE","ONE","NINE"};
int ord[12]={2,8,6,0,4,5,7,3,1,9};
int a[150],b[20];

int main()
{
//    ios_base::sync_with_stdio(false);
//    cin.tie(NULL);
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int i,t,j,n,ct,ans,x;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {

        cin>>s;
        CLR(a);
        CLR(b);
        n=(int)s.size();
        for(i=0;i<n;i++)
        {
            a[s[i]-'A']++;
        }

        ans=0;

        for(i=0;i<10;i++)
        {
            s2=l[i];
            x=1000000;
            for(j=0;j<(int)s2.size();j++)
            {
               x=min(x,a[s2[j]-'A']);
            }
            b[ord[i]]=x;

            for(j=0;j<(int)s2.size();j++)
            {
               a[s2[j]-'A']-=x;
            }
        }

        printf("Case #%d: ",tt);
        for(i=0;i<10;i++)
        {
            while(b[i])
            {
                cout<<i;
                b[i]--;
            }
        }
        cout<<endl;
    }
    return 0;
}
