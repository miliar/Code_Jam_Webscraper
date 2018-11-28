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

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("gg.out","w",stdout);
    bool check[11];
    int i,j,k,l,m,n,temp;

    cin >> n;
    for(i=1;i<=n;i++)
    {
        memset(check,0,sizeof(check));
        int countt=0;
        cin >> m;
        temp=m;
        j=1;
        if(temp==0)
        {
            cout << "Case #" << i << ": " <<"INSOMNIA" << endl;
            continue;
        }
        while(countt!=10)
        {

            while(temp!=0)
            {
                int x=temp%10;
                if(!check[x])
                {
                    check[x]=1;
                    countt++;
                }
                temp/=10;
            }
            j++;
            temp=m*j;
        }
        cout << "Case #" << i << ": " <<m*(j-1) << endl;
    }

}











