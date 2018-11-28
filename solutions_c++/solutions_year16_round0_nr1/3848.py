#include<iostream>
#include<algorithm>
#include<cstdio>
#include<string.h>
#include<climits>
#include<vector>
#include<stack>
#include<set>
#include<math.h>
using namespace std;
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define sint(i) scanf("%d",&i)
#define ss(s) scanf("%s",s)
#define pii pair<int,int>
#define mp(i,j) make_pair(i,j)
#define ll long long
#define MAX 1000000000
#define MOD 1000000007
#define vi vector<int>
#define vvi vector < vi >
#define pb(i) push_back(i);
#define tr(v,it) for(it=v.begin();it!=v.end();it++)
string digits(int n)
{
    string s="";
    if(n==0)
    return "0";
    while(n>0)
    {
        s=s+(char)((n%10)+'0');
        n=n/10;
    }
    return s;
}
int main()
{
    freopen("test.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int i;
    int t;
    cin>>t;
    int test;
    FOR(test,1,t)
    {
        string s;
        ll n;
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<test<<": INSOMNIA\n";
            continue;
        }
        int visited[11];
        FOR(i,0,10)
        visited[i]=0;
        i=1;
        int c=0,j;
        while(1)
        {
            s=digits(i*n);
            int len=s.length();
            FOR(j,0,len-1)
            {
                if(!visited[s[j]-'0'])
                {
                    visited[s[j]-'0']=1;
                    c++;
                }
            }
            if(c==10)
            {
                cout<<"Case #"<<test<<": "<<(i*n)<<"\n";
                break;
            }
            i++;
        }
    }
    return 0;
}
