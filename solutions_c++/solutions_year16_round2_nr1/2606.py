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
    int i,j;
    int test;
    int t;
    cin>>t;
    FOR(test,1,t)
    {
        string s;
        cin>>s;
        int a[26];
        FOR(i,0,25)
        a[i]=0;
        int len=s.length();

        FOR(i,0,len-1)
        {
            a[s[i]-'A']++;
        }
        string ans="";
        char arr[]={'Z','W','U','O','R','X','F','V','G','I'};
        char m[]={'0','2','4','1','3','6','5','7','8','9'};
        string str[]={"ZERO","TWO","FOUR","ONE","THREE","SIX","FIVE","SEVEN","EIGHT","NINE"};
        FOR(i,0,9)
        {
            int c=a[arr[i]-'A'];
            FOR(j,1,c)
            {
                ans=ans+m[i];
            }
            int len1=str[i].length();
            FOR(j,0,len1-1)
            {
                a[str[i][j]-'A']-=c;
            }
        }
        sort(ans.begin(),ans.end());
        cout<<"Case #"<<test<<": "<<ans<<"\n";
    }
    return 0;
}
