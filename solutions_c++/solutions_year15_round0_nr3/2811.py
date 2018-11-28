//Author: Siddharth Saluja
//Quote: "LIVE FOR YOUR AIM"

#include<bits/stdc++.h>

/* Constants */
#define mod 1000000007
#define imax 2147483647
#define imin -2147483648
#define pi 3.14159265358979323846264338327950
#define eps 1E-9
/* constants end  */
//#define DEBUG

/* stl templates */
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define vi vector<int>
#define vs vector<string>
#define vvi vector<vector<int> >
#define vpii vector<pair<int,int> >
#define vl vector<long long>
#define vvl vector<vector<long long> >
#define vpll vector<pair<long,long> >
#define sz(x) (int)x.size()
#define ln(s) (int)s.length()
#define ppb pop_back
#define all(x) x.begin(),x.end()
#define pii pair<int,int>
#define pll pair<long long,long long>
#define psi pair<string,int>
#define psl pair<string,long long >
#define aa first
#define bb second
/* stl templates end */

/* looping templates */
#define fori(s,e) for(i=s;i<=e;i++)
#define forj(s,e) for(j=s;j<=e;j++)
#define fork(s,e) for(k=s;k<=e;k++)
#define rep(i,s,e) for(int i=s;i<=e;i++)
/* looping templates end */

/* general templates */
#define mem(x,y) memset(x,y,sizeof(x));
#define ull unsigned long long
#define ll long long
#define s(a) scanf("%d",&a)
#define lls(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define p(a) printf("%d",a)
#define llp(a) printf("%lld",a)
#define sp(a) printf("%s",a)
#define cp(a) printf("%c",a)
#define nline printf("\n")
#define space printf(" ")
/* general templates end */


using namespace std;
ll int scan()
{
    ll int t=0;
    char c,ch;
    ch=getchar();
    if (ch=='-')
    {
        c=getchar();
    }
    else
    {
        c=ch;
    }
    while(c<'0' || c>'9')
    {
        c=getchar();
    }
    while(c>='0' && c<='9')
    {
        t=(t<<3)+(t<<1)+c-'0';
        c=getchar();
    }
    if (ch=='-' )
    {
        return -t;
    }
    else
    {
        return t;
    }
}

int a[10002];
int dp[10002][10002];
int mat[5][5];

int main()
{
#ifdef DEBUG
cout<<"Debugging\n";
#endif
freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
ios::sync_with_stdio(false);
ll int i,j,k,t,n,m,x,y,l;
string s;
mat[1][1]=1;
mat[1][2]=2;
mat[1][3]=3;
mat[1][4]=4;
mat[2][1]=2;
mat[2][2]=-1;
mat[2][3]=4;
mat[2][4]=-3;
mat[3][1]=3;
mat[3][2]=-4;
mat[3][3]=-1;
mat[3][4]=2;
mat[4][1]=4;
mat[4][2]=3;
mat[4][3]=-2;
mat[4][4]=-1;
cin>>t;
ll u=t;
while(t--)
{
    cin>>l>>x;
    cin>>s;
    string str="";
    for(i=0;i<x;i++)
    {
        str=str+s;
    }
    for(i=0;i<str.length();i++)
    {
        if(str[i]=='i')
            a[i]=2;
        else if(str[i]=='j')
            a[i]=3;
        else
            a[i]=4;
        //cout<<a[i]<<" ";
    }
    for(i=0;i<sz(str);i++)
    {
        dp[i][i]=a[i];
        for(j=i+1;j<sz(str);j++)
        {
            if(dp[i][j-1]<0)
            dp[i][j]=mat[-dp[i][j-1]][a[j]]*(-1);
            else
            dp[i][j]=mat[dp[i][j-1]][a[j]];
        }
    }
    for(i=0;i<sz(str);i++)
    {
        if(dp[0][i]==2)
        {
            for(j=i+1;j<sz(str);j++)
            {
                if(dp[i+1][j]==3 && dp[j+1][sz(str)-1]==4)
                {
                    cout<<"Case #"<<u-t<<": YES\n";
                    goto abc;
                }
            }
        }
    }
    //cout<<dp[0][2]<<" yyy\n";
    cout<<"Case #"<<u-t<<": NO\n";
    abc:
    int pp;
}

return 0;
}
