//jbuilder :V
//#include<bits/stdc++.h>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <sstream>
#include <math.h>
#include <cstring>
#include <set>



#define endl '\n'
#define ll long long
#define fo(i,n) for(i=0;i<n;i++)
#define rep(i,n) for(i=n-1;i>=0;i--)
#define mod 1000000007

int gcd(int a,int b){return b==0?a:gcd(b,a%b);}
int lcm(int a,int b){return ((a*b)/gcd(a,b));}

using namespace std;



char a[100],b[101];
ll ans[11],n;

ll powr(ll a,ll b)
{
    ll i,j=1;
    for(i=1;i<=b;i++)
    {
        j*=a;
    }
    return j;

}

bool check()
{
    ll temp=0,i,j,k,l,x,y;
    l=strlen(a);
  //  cout << temp << " " << a;
    for(x=2;x<=10;x++)
    {
        temp=0;
        for(y=0;y<l;y++)
        {
            temp+=(powr(x,l-y-1)*(a[y]-'0'));
        }
        //cout << temp << " " << a;
        ll flag1=0;
        for(y=2;y*y<=temp;y++)
        {
            if(temp%y==0)
            {
                flag1=1;
                ans[x]=y;
                break;
            }

        }
        if(!flag1)
            return 0;
    }
    return 1;
}

bool check2()
{
    ll temp=0,i,j,k,l,x,y;
    l=strlen(b);
    for(x=2;x<=10;x++)
    {
        temp=0;
        for(y=0;y<l;y++)
        {
            temp+=(powr(x,l-y-1)*(b[y]-'0'));
        }
    //    cout << b <<" " << temp << endl;
        ll flag1=0;
        for(y=2;y*y<=temp;y++)
        {
            if(temp%y==0)
            {
                flag1=1;
                ans[x]=y;
                break;
            }
        }
        if(!flag1)
            return 0;
    }
    return 1;
}


int main()
{

    freopen("C-small-attempt0.in","r",stdin);
    freopen("ggC.out","w",stdout);
    int t,T;
    cin >> T;
    for(t=1;t<=T;t++)
    {

        int i,j,k,l,m=0,flagbreak=0;
        cin >> n >> k;
        cout << "Case #" << t <<  ":" << endl;
        a[0]='1';
        a[n-1]='1';
        a[n]='\0';
        for(i=1;i<n-1;i++)
        {
            a[i]='0';
        }

        for(i=1;i<=n-1;i++)
        {
            if(flagbreak==1)
                break;
           //cout << a <<" " << endl;
            if(check())
            {
                cout << a << " ";
                for(j=2;j<=10;j++)
                {
                    cout << ans[j] << " ";
                }
                cout << endl;
                m++;
                if(m==k)
                    break;
            }
            strcpy(b,a);
            for(j=n-2;j>i;j--)
            {
                b[j]='1';
               // cout << b << " " << endl;
                if(check2())
                {
                    cout << b << " ";
                    for(int jj=2;jj<=10;jj++)
                    {
                        cout << ans[jj] << " ";
                    }
                    cout << endl;
                    m++;
                    if(m==k)
                    {
                            flagbreak=1;
                            break;
                    }
                }
            }
            a[i]='1';
        }

        //cout << m;
    }

}



