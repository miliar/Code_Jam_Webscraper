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
#define WHITE 0
#define GREY  1
#define BLACK  2
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
    int tc,lol=1;
    scanf("%d",&tc);
    deque <char> d1;
    string x;


    while( tc-- )
    {
        cin>>x;
        d1.push_back(x[0]);




        for( int A=1; A<x.size(); A++ )
        {
            if( x[A] >= d1.front() )
            {
                d1.push_front(x[A]);
            }

            else
            {
                d1.push_back(x[A]);
            }
        }

        printf("Case #%d: ",lol);

        while( !d1.empty() )
        {
            cout<<d1.front();
            d1.pop_front();
        }
        lol++;
        printf("\n");

    }
}

