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
    int hh=1;
    ll maxx[60];
    memset(maxx,0,sizeof(maxx));
     maxx[1]=1;
    rep(i,2,50)
        {
            rep(j,1,i)
            maxx[i]+=maxx[j];
        }
/*
rep(i,1,20)
cout<<maxx[i]<<" ";
cout<<"\n";
*/
    ll t , n, p[100],x;
    cin>>t;
    while(t--)
    {
        ll mat[60][60],b,m,ind[60],dp[60];
        memset(mat,0,sizeof(mat));
        memset(dp,0,sizeof(dp));
        memset(ind,0,sizeof(ind));
        cin>>b>>m;
        n=b;
        cout<<"Case #"<<hh<<": ";



        if(m>maxx[b])
            cout<<"IMPOSSIBLE\n";
        else
        {
            cout<<"POSSIBLE\n";
            x=m;
            int d=2;
            mat[1][2]=1;
            while(x>0)
            {
                if(x%2==1)
                {
                    ind[d]=1;

                }
                d++;
                x/=2;
            }
            /*
rep(i,1,b+1)
cout<<ind[i]<<" ";
cout<<"\n";*/
        rep(i,1,b+1)
        {
            if(ind[i]==1)
            {
                if(i!=b)
                mat[i][b]=1;
                rep(j,1,i+1)
                rep(k,1,j)
                mat[k][j]=1;
            }
        }
        rep(i,1,b+1)
{
    rep(j,1,b+1)
cout<<mat[i][j];
cout<<"\n";

    }
        }
hh++;
    }
}
