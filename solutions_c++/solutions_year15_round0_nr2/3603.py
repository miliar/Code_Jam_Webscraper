# include <cstdio>
#include<iostream>
#include <cstring>
#include <algorithm>
#include<bits/stdc++.h>

using namespace std;

#define sd(x) scanf("%lld",&x);
#define LL long long
#define LD long double
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define Fill(a, b) memset(a, b, sizeof(a))
#define INF 1001000009
#define MaxVal 200100

int func(int a)
{

}


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out_largeb.txt","w",stdout);
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        int d;
        cin>>d;
        int a[1001]={0};
        int temp;
        int maxi=-1;
        //bool check=false;
        for(int i=0;i<d;i++)
        {
            cin>>a[i];temp=a[i];
            if(temp>maxi)maxi=temp;

        }
        int mini=maxi,curr=0;
        for(int i=1;i<=maxi;i++)
        {
            int res=i;

            for(int j=0;j<d;j++)
            {
                if(a[j]<=i)continue;
                if((a[j]%i) == 0)
                {
                    res+=a[j]/i;
                    res--;
                }
                else
                {
                    res+=a[j]/i;
                }
            }
            if(mini>res)mini=res;
        }
        cout<<"Case #"<<test<<": "<<mini<<endl;
    }
}

