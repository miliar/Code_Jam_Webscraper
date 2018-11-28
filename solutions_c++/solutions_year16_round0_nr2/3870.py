#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

bool check(string &s)
{
    for(int i=0;i<s.length();i++)
    {
        if(s[i] == '-')
            return true;
    }
    return false;
}

void flip(string &s,int x)
{
    reverse(s.begin(),s.begin()+x+1);
    for(int i=0;i<=x;i++)
    {
        if(s[i] == '+')
            s[i] = '-';
        else
            s[i] = '+';
    }
}

int solve(string &s,int n)
{
    int i,j;
    int ret = 1;
    for(i=n-1;i>=0;i--)
    {
        if(s[i] == '-')
            break;
    }
    
    for(j=0;j<i;j++)
    {
        if(s[j] == '-')
            break;
    }
    j--;
    if(j >= 0)
    {
        flip(s,j);
        ret++;
    }
    
    flip(s,i);
    return ret;
    
}

int main()
{
    int t;
    string s;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    int sv = t;
    
    while(t--)
    {
        cin>>s;
        int n = int(s.length());
        int ans = 0;
        while(check(s))
        {
            
            ans += solve(s,n);
            //cout<<s<<endl;
        }
        cout<<"Case #"<<sv-t<<": "<<ans<<endl;
    }
    
    //system("pause");
    return 0;
}
