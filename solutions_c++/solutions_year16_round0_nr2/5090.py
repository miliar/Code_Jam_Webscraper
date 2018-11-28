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
    freopen("B-large.in","r",stdin);
    freopen("ggB.out","w",stdout);
    int t,T;
    cin >> T;
    for(t=1;t<=T;t++)
    {
        int i,j,k,l,m,n,ans=0;
        char a[105];
        cin >> a;
        l=strlen(a);
        int flag1=0,flag2=0;
        for(i=0;i<l;i++)
        {
            if(a[i]=='-')
            {
                if(flag2==1)
                {
                    ans++;
                    flag1=1;
                    flag2=0;
                }
                flag1=1;
            }
            if(a[i]=='+')
            {
                if(flag1==1)
                {
                    ans++;
                    flag2=1;
                    flag1=0;
                }
                flag2=1;
            }

        }
        if(flag1==1)
            ans++;
        cout << "Case #" << t<<": "<<ans << endl;

    }

}











