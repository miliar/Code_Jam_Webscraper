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

#define sqr(x) ((x)*(x))
#define INF LONG_LONG_MAX
#define PI 2*acos(0)
#define pb push_back

i64 visited[20];
vector <i64> printer,v1,ans;

i64 power(i64 num1,i64 power)
{
    i64 ans=1;
    for(i64 A=1;A<=power;A++)
    {
        ans*=num1;
    }
    return ans;
}

i64 n1,n2,c1;

void call()
{

    if( c1 == n2)
        return;
    i64 temp;
    i64 d2,d3,d4,d5,d6,d7,d8,d9,d10,p;
    if( printer.size() == n1-2 )
    {
        p=n1-1;
        d2=0,d3=0,d4=0,d5=0,d6=0,d7=0,d8=0,d9=0,d10=0;
       /// cout<<1;
        d2+=power(2,p);
        d3+=power(3,p);
        d4+=power(4,p);
        d5+=power(5,p);
        d6+=power(6,p);
        d7+=power(7,p);
        d8+=power(8,p);
        d9+=power(9,p);
        d10+=power(10,p);

        for(i64 A=0;A<printer.size();A++)
        {
            p--;
            ///cout<<printer[A]<<endl;
            d2+=power(2,p)*printer[A];
            d3+=power(3,p)*printer[A];
            d4+=power(4,p)*printer[A];
            d5+=power(5,p)*printer[A];
            d6+=power(6,p)*printer[A];
            d7+=power(7,p)*printer[A];
            d8+=power(8,p)*printer[A];
            d9+=power(9,p)*printer[A];
            d10+=power(10,p)*printer[A];
        }
        /// cout<<1;
        d2+=1;
        d3+=1;
        d4+=1;
        d5+=1;
        d6+=1;
        d7+=1;
        d8+=1;
        d9+=1;
        d10+=1;


        for( i64 A=2; A*A <= d2 ; A++)
        {
            if( d2 % A == 0)
            {
                ans.pb(A);
                break;
            }
        }

        for( i64 A=2; A*A <= d3 ; A++)
        {
            if( d3 % A == 0)
            {
                ans.pb(A);
                break;
            }
        }

        for( i64 A=2; A*A <= d4 ; A++)
        {
            if( d4 % A == 0)
            {
                ans.pb(A);
                break;
            }

        }

        for( i64 A=2; A*A <= d5 ; A++)
        {
            if( d5 % A == 0)
            {
                ans.pb(A);
                break;
            }
        }

        for( i64 A=2; A*A <= d6 ; A++)
        {
            if( d6 % A == 0)
            {
                ans.pb(A);
                break;
            }
        }

        for( i64 A=2; A*A <= d7 ; A++)
        {
            if( d7 % A == 0)
            {
                ans.pb(A);
                break;
            }
        }

        for( i64 A=2; A*A <= d8 ; A++)
        {
            if( d8 % A == 0)
            {
                ans.pb(A);
                break;
            }
        }

        for( i64 A=2; A*A <= d9 ; A++)
        {
            if( d9 % A == 0)
            {
                ans.pb(A);
                break;
            }
        }

        for( i64 A=2; A*A <= d10 ; A++)
        {
            if( d10 % A == 0)
            {
                ans.pb(A);
                break;
            }
        }

        if( ans.size() == 9 )
        {
            c1++;
            printf("%lld ",d10);
            for( i64 A=0; A<ans.size(); A++ )
            {
                printf("%lld",ans[A]);
                if( A!= ans.size()-1 )
                    printf(" ");
            }
            printf("\n");
            ans.clear();
        }
        else
        ans.clear();
        /*cout<<d2<<endl;
        cout<<d3<<endl;
        cout<<d4<<endl;
        cout<<d5<<endl;
        cout<<d6<<endl;
        cout<<d7<<endl;
        cout<<d8<<endl;
        cout<<d9<<endl;
        cout<<d10<<endl;
        cout<<endl<<endl;*/
        return;
    }

    for(i64 A=1;A<=2;A++)
    {
        if( c1 == n2 )return;
        temp=v1[A];
        printer.pb(temp);
        visited[temp]++;
        call();
        printer.pop_back();
        //visited[temp]--;
    }
}
int main()
{
     //freopen("F:/in.txt","r",stdin);
    //freopen("F:/out.txt","w",stdout);

    v1.pb(-100);
    v1.pb(0);
    v1.pb(1);
    i64 tc,lol=1;
    scanf("%lld",&tc);
    while( tc-- )
    {

        c1=0;
        ans.clear(),printer.clear();
        scanf("%lld %lld",&n1,&n2);
        printf("Case #%lld:\n",lol);
        lol++;
        call();

    }
}
