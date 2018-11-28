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

deque <char> ans;

char a[1005];


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ansl.out","w",stdout);
    ll t,T;
    cin >> T;
    for(t=1;t<=T;t++)
    {
        int i,j,k,l,m;
        ans.clear();
        cin >> a;
        ans.push_back(a[0]);
        for(i=1;i<strlen(a);i++)
        {
            deque <char>::iterator it=ans.begin();
            if(a[i]>=*it)
                ans.push_front(a[i]);
            else
                ans.push_back(a[i]);
        }
        cout << "Case #" << t << ": ";
        for(deque <char>::iterator it=ans.begin();it!=ans.end();it++)
        {
            cout << *it;
        }
        cout << endl;
    }


}

