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
    ll t , n, p[100],x;
    cin>>t;
    while(t--)
    {
        ll a[26];
        cin>>n;
        x=0;
        rep(i,0,n)
        {cin>>a[i];
        x+=a[i];
        }
cout<<"Case #"<<hh<<": ";
        while(x>0)
        {

        int p1,p2,ma=0;

        rep(i,0,n)
        {
            if(a[i]>ma)
            {
                ma=a[i];
                p1=i;
            }
        }
a[p1]--;

        p2=-1;

                 ma=0;
        rep(i,0,n)
        {
            if(a[i]>ma)
            {
                ma=a[i];
                p2=i;
            }
        }

        if(p2==-1||(ma==1&&x==3&&p2!=-1))
        {cout<<(char)(p1+65)<<" ";
        x--;
        }
        else
        {
            cout<<(char)(p1+65)<<(char)(p2+65)<<" ";
           a[p2]--;
            x-=2;
        }
    }
cout<<"\n";
hh++;
    }

}
