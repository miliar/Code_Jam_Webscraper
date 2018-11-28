#include <bits/stdc++.h>
using namespace std;

#define i64 long long
#define u32 unsigned int
#define u64 unsigned long long

#define Neg(v) memset((v), -1, sizeof(v))
#define Zero(v) memset((v), 0, sizeof(v))

#define For(t,i,c) for(t::iterator i =(c).begin(); i != (c).end(); ++i)
#define RFor(t,v,c) for(t::reverse_iterator i = (c).rbegin(); i != (c).rend(); ++i)

#define FOR( A, L, U ) for(int A=(int)L ; A<=(int)U ; A++ )
#define RFOR( A, U, L ) for(int A=(int)U ; A>=(int)L ; A-- )
#define ff first
#define ss second
#define sqr(x) ((x)*(x))
#define INF LONG_LONG_MAX
#define PI 2*acos(0)
#define pb push_back
#define dbug cout<<1<<endl
const double eps = 1e-9;
//int r[]={1,0,-1,0};int c[]={0,1,0,-1}; ///4 Direction
//int r[]={1,1,0,-1,-1,-1,0,1};int c[]={0,1,1,1,0,-1,-1,-1};///8 direction
//int r[]={2,1,-1,-2,-2,-1,1,2};int c[]={1,2,2,1,-1,-2,-2,-1};///Knight Direction
//int r[]={2,1,-1,-2,-1,1};int c[]={0,1,1,0,-1,-1}; ///Hexagonal Direction

struct cmpStruct {
  bool operator() (int const & lhs, int const & rhs) const
  {
    return lhs > rhs;
  }
};

i64 visited[20];

int main()
{
    ///I_DO_LOVE_TANYA_ROMANOVA_ <3
    //freopen("F:/in.txt","r",stdin);
    //freopen("F:/out.txt","w",stdout);
    i64 tc,num,temp,ans,t1,t2,lol=1,m;
    scanf("%lld",&tc);
    bool judge;
    while(tc--)
    {
        judge=true;
        Zero(visited);
        m=1;
        scanf("%lld",&num);

        if( num == 0 )
        {
            printf("Case #%lld: INSOMNIA\n",lol);
            lol++;
            continue;
        }
        ans=0;
        while(1)
        {
            temp=num*m;
            if( temp/m != num )
            {
                judge=false;
                break;
            }
            while( temp != 0 )
            {
                t1=temp%10;
                temp/=10;
                if( visited[t1] == 0 )
                {
                    ans++;
                    visited[t1]=1;
                }
            }

            if( ans == 10 )
            {
                t2=num*m;
                break;
            }
            m++;
        }
        if( judge )
        printf("Case #%lld: %lld\n",lol,t2);
        else
        printf("Case #%lld: INSOMNIA\n",lol);
        lol++;
    }
}

