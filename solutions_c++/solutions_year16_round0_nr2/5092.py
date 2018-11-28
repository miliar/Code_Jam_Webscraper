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



int main()
{
    ///I_DO_LOVE_TANYA_ROMANOVA_ <3
    //freopen("F:/in.txt","r",stdin);
    //freopen("F:/out.txt","w",stdout);
    int tc,ind,t1,ans,lol=1;
    char ch1;
    scanf("%d",&tc);
    string s1,perf;

    while( tc-- )
    {
        ans=0;
        cin>>s1;
        perf="";
        ind=0;
        for( int A=0; A<s1.size(); A++ )
        {
            perf+="+";
        }
        t1=0;
        ch1=s1[t1];
        t1++;
        while(1)
        {

            while( ch1 == s1[t1] )
            {
                t1++;
            }
            if( t1 == s1.size() )break;
            for( int A=0; A < t1; A++ )
            {
                if( s1[A] == '+' )
                {
                    s1[A] = '-';
                }
                else if( s1[A] == '-' )
                {
                    s1[A] = '+';
                }
            }
            ch1=s1[t1];
            //cout<<s1<<endl;
            ans++;
        }
        if( s1 != perf )
        ans++;
        printf("Case #%d: %d\n",lol,ans);
        lol++;
    }
}
