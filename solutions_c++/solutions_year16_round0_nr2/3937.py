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
        cin>>s;
        int len=s.length();

        int c=0;
        for(i=0;i<len;i++)
        {
            if(s[i]=='-')
            c++;
        }

        int ans=0,j;
        while(c)
        {
            //converting start
            if(s[0]=='+')
            ans++;
            for(i=0;i<len;i++)
            {
                if(s[i]=='+')
                {
                    c++;
                    s[i]='-';
                }
                else
                break;
            }

            for(i=len-1;i>=0;i--)
            {
                if(s[i]=='-')
                {
                    ans++;
                    break;
                }
            }
            for(j=0;j<=i;j++)
            {
                if(s[j]=='+')
                {
                    s[j]='-';
                    c++;
                }
                else
                {
                    s[j]='+';
                    c--;
                }
            }
            reverse(s.begin(),s.begin()+i+1);
           // cout<<s<<"\n";
        }
        cout<<"Case #"<<test<<": "<<ans<<"\n";
    }
    return 0;
}
