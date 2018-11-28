#include<bits/stdc++.h>
#define FRU freopen("out.txt","w",stdout)
#define FRO freopen("A-large.in","r",stdin)
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define mem(ara,n) memset(ara,n,sizeof ara)
#define loop(i,j,n) for(i=j;i<n;i++)
#define rloop(i,j,n) for(i=n;i>=j;i--)
#define INF 2147483647
#define ll long long
#define pii pair<int,int>
#define eps 1e-9
#define mii map<int,int>
#define vi vector<int>
#define all(n) n.begin(),n.end()
#define inf INF

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

/*bool bitcheck(int n,int pos)
{
    return (bool)(n & (1<<pos));
}

int biton(int n,int pos)
{
    return n=n or (1<<pos);
}
int bitoff(int n,int pos)
{
    return n=n & ~(1<<pos);
}*/

using namespace std;

int main()
{
FRO;
FRU;
//std::ios_base::sync_with_stdio(false);
    int a,b,c,i,j,k,tc,t;
    int m,cnt=0;
    ll n;
    scanf("%d",&tc);
    int ara[10];
    for(t=1; t<=tc; t++)
    {
        scanf("%lld",&n);
        mem(ara,0);
        int flg=1;
        cnt=0;
        ll tmp=n,grr;
        while(tmp)
        {
            ara[tmp%10]++;
            //printf("%lld ",tmp%10);
            tmp/=10;
        }
        //printf("absdfbjh\n");
        for(i=0; i<10; i++)if(ara[i]==0)cnt++;
        printf("Case #%d: ",t);
        if(n==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        //printf("%d\n",cnt);
        ll num=n;
        for(i=1; i<=1000; i++)
        {
            //printf("%lld\n",n);
            //for(j=0;j<10;j++)printf("%d ",ara[j]);printf("\n");
            n+=num;
            tmp=n;
            while(tmp)
            {
                grr=tmp%10;
                if(ara[grr]==0)cnt--;
                ara[grr]++;
                tmp/=10;
            }
            if(cnt==0)
            {//printf("%d ",i);
                flg=0;
                printf("%lld\n",n);
                break;
            }
        }
        if(flg)
        {
            printf("INSOMNIA\n");
        }
    }
    return 0;
}
