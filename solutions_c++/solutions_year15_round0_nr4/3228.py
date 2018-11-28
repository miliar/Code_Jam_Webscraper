// codersan
#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define init(a,b) memset(a,b,sizeof(a));
#define pnl() printf("\n");
#define tr(container,it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define sortv(a) sort(a.begin(),a.end());
#define go()  int t; cin>>t; while(t--)
#define forl(i,a,b) for(int i=a;i<b;i++)
#define rofl(i,a,b) for(int i=a;i>b;i--)
#define LL long long int
#define mod 1000000007
using namespace std;
typedef vector<int> vi;
typedef pair<int , int> pii;
typedef vector<pii> vpii;
inline LL gcd(LL a, LL b){ LL temp; while(b>0)	{ temp= b; b=a%b; a=temp;}	return a;}
inline LL fast(LL a, LL b)
{
    LL prod=1;
    while(b)
    {
        if(b&1)prod=(prod*a);
        a=(a*a),b/=2;
    }
    return prod;
}
int main()
{
    #ifndef ONLINE_JUDGE
       freopen("C:\\Users\\codersan\\Desktop\\GCJ\\Bin.in", "r", stdin);
        freopen("C:\\Users\\codersan\\Desktop\\GCJ\\Bout.txt", "w", stdout);
    #endif
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {

        int x,r,c,p;
        int rt,ct;
        cin>>x>>rt>>ct;
        r=min(ct,rt);
        c=max(ct,rt);
        p=r*c;
        cout<<"Case #"<<j<<": ";
        if(x==1)
         printf("GABRIEL\n");
        else if(x==2)
        {
            if((r>1||c>1) && p%x==0)
                printf("GABRIEL\n");
            else
                printf("RICHARD\n");
        }
        else if(p%x!=0||x>=(2*r+1)||(x>=(c+r-2)&&x>3))
            printf("RICHARD\n");
        else if(x>r && x>c)
            printf("RICHARD\n");
        else
            printf("GABRIEL\n");
    }

return 0;
}
