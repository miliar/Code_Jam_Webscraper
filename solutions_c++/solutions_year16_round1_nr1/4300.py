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
    ll t,p=1,n;
    cin>>t;
    while(t--)
    {

    string s,str;
    cin>>s;
    n=s.length();
    str=s.substr(0,1);
    for(int i=1;i<n;i++)
    {
        if(s[i]>=str[0])
        str=s.substr(i,1)+str;
        else
            str=str+s.substr(i,1);
    }
    cout<<"Case #"<<p<<": ";
    cout<<str<<"\n";
    p++;

    }
}
