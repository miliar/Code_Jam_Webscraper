//0000000000000000000000000000//
//%%%%   Archit Srivastava %%%//
//        NIT Durgapur        //
//0000000000000000000000000000//
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,b) for(i=0;i<b;i++)
#define rep1(i,b) for(i=1;i<=b;i++)
#define mod 1000000007
#define pi(n) printf("%d",n)
#define pin(n) printf("%d\n",n)
#define piw(n) printf("%d ",n)
#define pll(n) printf("%lld",n)
#define plln(n) printf("%lld\n",n)
#define pllw(n) printf("%lld ",n)
#define sll(n) scanf("%lld",&n)
#define ss(s) scanf("%s",s)
#define ps(s) printf("%s",s)
#define psn(s) printf("%s\n",s)
#define psw(s) printf("%s ",s)
#define si(n) scanf("%d",&n)
#define pn printf("\n")
#define pw printf(" ")
#define PI (3.141592653589793)
#define MAX_SIZ 1000005
/*
inline int ri()
{
    int n=0;char c;
    while(1)
    {
        c=getchar_unlocked();
        if(c=='\n'||c==' '||c==EOF)break;
        n=(n<<3) + (n<<1) +c-48;
    }
    return n;
}
inline long long rll()
{
    long long n=0;
    char c;
    while(1)
    {
        c=getchar_unlocked();
        if(c=='\n'||c==' '||c==EOF)break;
        n=(n<<3) + (n<<1) + c - 48;
    }
    return n;
}
*/
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

int main()
{
    int t,x;
    si(t);
    x=t;
    while(t--)
    {
        printf("Case #%d: ",x-t);
        int n,i,j;
        si(n);
        map<int,int> mp;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                int temp;
                si(temp);
                if(i==n)
                {
                    mp[temp]++;
                }
            }
        }
        si(n);//piw(n);
        int flag=0,occ=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                int temp;
                si(temp);
                if(i==n)
                {
//                    piw(temp);
                    mp[temp]++;
                    if(mp[temp]>1)
                    {
                        flag++;
                        occ=temp;
                    }
                }
            }
        }
        if(!flag)
        {
            printf("Volunteer cheated!\n");
        }
        else if(flag==1)
        {
            pin(occ);
        }
        else
            printf("Bad magician!\n");


    }
}
