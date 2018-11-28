 /*
 Problem name :
 Algorithm : Not Sure Yet
 Contest/Practice :
 Source :
 Comment : Whenever you start to believe  yourself, people also start to believe in you
 Date : --
 Last Update : 25-Mar-2015
*/

/*
    Am I wrong for thinking out the box from where I stay?
    Am I wrong for saying that I choose another way?

    I ain't tryna do what everybody else doing
    Just cause everybody doing what they all do
    If one thing I know, I'll fall but I'll grow
    I'm walking down this road of mine, this road that I call home

*/



#include<bits/stdc++.h>

#define pause           system("pause");
#define FOR(s,e,inc)    for(int i=s;i<=e;i+=inc)
#define mod             1000000007
#define inf             1<<30
#define pb              push_back
#define ppb             pop_back
#define mp              make_pair
#define F               first
#define S               second
#define sz(x)           ((int)x.size())
#define sqr(x)          ( (x)* (x) )
#define eps             1e-9
#define lcm(x,y)        (abs(x) /gcd(x,y))* abs(y)
#define on(x,w)         x|(1<<w)
#define check(x,w)      (x&(1<<w))
#define all(x)          (x).begin(),(x).end()
#define pf              printf
#define sf              scanf
#define pi              acos(-1.0)
#define reset(x,v)      memset(x,v,sizeof(x));
#define AND             &&
#define OR              ||
#define what_is(x)      cerr<<#x<<" is "<<x<<"\n";

typedef long long ll;
typedef unsigned long long llu;

using namespace std;


template<class T>
inline T mod_v(T num)
{
    if(num>=0)
        return num%mod;
    else
        return (num%mod+mod)%mod;
}
template<class T>
inline T gcd(T a,T b)
{
    a=abs(a);
    b=abs(b);

    while(b) b ^= a ^= b ^= a %= b;
    return a;
}

template<class T>
T fast_pow(T n , T p)
{
    if(p==0) return 1;
    if(p%2)
    {
        T g=mod_v ( mod_v(n) * mod_v(fast_pow(n,p-1)) );
        return g;
    }
    else
    {
        T g=fast_pow(n,p/2);
        g=mod_v( mod_v(g) * mod_v(g) ) ;
        return g;
    }
}

template<class T>
inline T modInverse(T n)
{
    return fast_pow(n,mod-2);
}

template<class T>
inline void debug(string S1,T S2,string S3)
{
    cout<<S1<<S2<<S3;
}

bool equalTo ( double a, double b ){ if ( fabs ( a - b ) <= eps ) return true; else return false; }
bool notEqual ( double a, double b ){if ( fabs ( a - b ) > eps ) return true; else return false; }
bool lessThan ( double a, double b ){ if ( a + eps < b ) return true; else return false; }
bool lessThanEqual ( double a, double b ){if ( a < b + eps ) return true;   else return false;}
bool greaterThan ( double a, double b ){if ( a > b + eps ) return true;else return false;}
bool greaterThanEqual ( double a, double b ){if ( a + eps > b ) return true;else return false;}


template<class T>
inline int in(register T& num)
{
    register char c=0;
    num=0;
    bool n=false;
    while(c<33)c=getchar();
    while(c>33){
        if(c=='-')
            n=true;
        else num=num*10+c-'0';
        c=getchar();
    }
    num=n?-num:num;
    return 1;
}

/******* ! Code start from here ! *******/

class nod
{
public:
    int cnt,v;

    nod(int cnt,int v)

    {
        this->cnt=cnt;
        this->v=v;
    }

    bool operator < (const nod& a) const
    {
        return cnt<a.cnt;
    }
};


int main()
{
//     std::ios_base::sync_with_stdio(false);

    #ifdef kimbbakar
        freopen ( "in.txt", "r", stdin );
        freopen ( "out.txt", "w", stdout );
    #endif

    int t,tcase=1;

    int n;

    in(t);

    while(t--)
    {
        in(n);
        int val;

        priority_queue<nod>q;

        int total=0;

        for(int i=0;i<n;i++)
        {
            in(val);

            q.push(nod(val,i) );

            total+=val;
        }

        pf("Case #%d:",tcase++);

        while(total>0)
        {
            if(q.size()>=2)
            {
                nod x1=q.top();
                q.pop();
                nod x2=q.top();
                q.pop();

                if(x2.cnt==x1.cnt)
                {
                    if(x1.cnt==1)
                    {
                        if(q.size()==1)
                        {
                            pf(" %c",x1.v+'A');
                            x1.cnt-=1;

                            if(x1.cnt)
                                q.push(x1);
                            q.push(x2);

                            total-=1;
                        }
                        else
                        {
                            pf(" %c%c",x1.v+'A',x2.v+'A');
                            x1.cnt-=1;
                            x2.cnt-=1;

                            if(x1.cnt)
                            q.push(x1);

                            if(x2.cnt)
                            q.push(x2);

                            total-=2;

                        }
                    }
                    else
                    {
                        pf(" %c%c",x1.v+'A',x2.v+'A');
                        x1.cnt-=1;
                        x2.cnt-=1;

                        if(x1.cnt)
                        q.push(x1);

                        if(x2.cnt)
                        q.push(x2);

                        total-=2;

                    }
                }
                else
                {
                    pf(" %c%c",x1.v+'A',x1.v+'A');
                    x1.cnt-=2;

                    if(x1.cnt)
                    q.push(x1);

                    q.push(x2);

                    total-=2;
                }

            }
            else
            {
                if(q.top().cnt%2==0)
                {
                    nod x=q.top();
                    q.pop();

                    pf(" %c%c",x.v+'A',x.v+'A');
                    x.cnt-=2;

                    if(x.cnt)
                    q.push(x);

                    total-=2;
                }
                else
                {
                    nod x=q.top();
                    q.pop();

                    pf(" %c",x.v+'A');
                    x.cnt-=1;

                    if(x.cnt)
                        q.push(x);

                    total-=1;
                }
            }
        }

        pf("\n");
    }


    return 0;
}





