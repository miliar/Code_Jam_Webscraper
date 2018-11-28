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

#define endl '\n'
#define ll long long
#define fo(i,n) for(i=0;i<n;i++)
#define rep(i,n) for(i=n-1;i>=0;i--)
#define mod 1000000007


int gcd(int a,int b){return b==0?a:gcd(b,a%b);}
int lcm(int a,int b){return ((a*b)/gcd(a,b));}

using namespace std;

int a[5000];
vector <int> ans;


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("ansbl.out","w",stdout);
    ll t,T;
    cin >> T;
    for(t=1;t<=T;t++)
    {

        memset(a,0,sizeof(a));
        ans.clear();
        int i,j,k,l,m,n,x,maxx=0;
        cin >> n;
        for(i=0;i<2*n-1;i++)
        {
            for(j=0;j<n;j++)
            {
                cin >> x;
                a[x]++;
                maxx=max(maxx,x);
            }
        }
        for(i=0;i<=maxx&&ans.size()<n;i++)
        {
            if((a[i]!=0)&&(a[i]%2!=0))
                ans.push_back(i);
        }
        cout << "Case #" << t <<": ";
        for(i=0;i<n;i++)
        {
            cout << ans[i] << " ";
        }
        cout << endl;
    }

}

