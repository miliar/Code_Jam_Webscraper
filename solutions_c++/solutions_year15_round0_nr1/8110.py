#include<bits/stdc++.h>
#define FRU freopen("out.txt","w",stdout)
#define FRO freopen("A-large.in","r",stdin)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(ara,n) memset(ara,n,sizeof ara)
#define loop(i,j,n) for(i=j;i<n;i++)
#define rloop(i,j,n) for(i=n;i>=j;i--)
#define INF 2147483647
//const int row[]={-1, -1, -1,  0,  0,  1,  1,  1};  // Kings Move
//const int col[]={-1,  0,  1, -1,  1, -1,  0,  1};  // Kings Move
//const int row[]={-2, -2, -1, -1,  1,  1,  2,  2};  // Knights Move
//const int col[]={-1,  1, -2,  2, -2,  2, -1,  1};  // Knights Move
//const int row[]={-1,0,0,1,0};
//const int col[]={0,-1,1,0,0};
int gcd(int a,int b)
{
    return b==0?a:gcd(b,a%b);
}
int lcm(int a,int b)
{
    return ((a*b)/gcd(a,b));
}


using namespace std;
int todisit(char c)
{
    return c-'0';
}

int main()
{
FRO;
FRU;
//std::ios_base::sync_with_stdio(false);
    int a,b,c,i,j,k,tc,t;
    int n,m,cnt=0;
    scanf("%d",&tc);
    for(t=1; t<=tc; t++)
    {
        string s;
        cnt=0;
        int cur=0;
        cin>>n>>s;
        cur=todisit(s[0]);
        for(i=1;i<=n;i++)
        {
            m=todisit(s[i]);
            if(cur<i)
            {
                cnt+=i-cur;
                cur+=i-cur;
            }
            cur+=m;
        }
        printf("Case #%d: %d\n",t,cnt);
    }
    return 0;
}
