/*          بسم الله الرحمن الرحيم
    Author: Nishat Tasnim Ahmed Meem
    Shahjalal University Of Science & Technology, '13batch
*/

#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<deque>
#include<map>
#include<sstream>
#include<set>
#include<utility>

using namespace std;

#define inf 1<<28
#define ll long long
#define sf1(a) scanf("%d",&a)
#define sf2(a,b) scanf("%d %d",&a,&b)
#define sf3(a,b,c) scanf("%d %d %d", &a,&b, &c)
#define sf4(a,b,c, d) scanf("%d %d %d %d", &a,&b, &c, &d)
#define sf1ll(a) scanf("%lld",&a)
#define sf2ll(a,b) scanf("%lld %lld",&a,&b)
#define sf3ll(a,b,c) scanf("%lld %lld %lld", &a,&b, &c)
#define sf4ll(a,b,c, d) scanf("%lld %lld %lld %lld", &a,&b, &c, &d)
#define pi acos(-1)
#define sz 10000+10
#define pii pair<int, int>

template<class T> T power(T N,T P)
{
    return (P==0)?  1: N*power(N,P-1);   //N^P
}
template<class T> T gcd(T a,T b)
{
    if(b == 0)return a;    //gcd(a,b)
    return gcd(b,a%b);
}

template<class T1> void deb(T1 e1)
{
    cout<<e1<<endl;
}
template<class T1,class T2> void deb(T1 e1,T2 e2)
{
    cout<<e1<<" "<<e2<<endl;
}
template<class T1,class T2,class T3> void deb(T1 e1,T2 e2,T3 e3)
{
    cout<<e1<<" "<<e2<<" "<<e3<<endl;
}
template<class T1,class T2,class T3,class T4> void deb(T1 e1,T2 e2,T3 e3,T4 e4)
{
    cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<endl;
}
template<class T1,class T2,class T3,class T4,class T5> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5)
{
    cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<endl;
}
template<class T1,class T2,class T3,class T4,class T5,class T6> void deb(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5,T6 e6)
{
    cout<<e1<<" "<<e2<<" "<<e3<<" "<<e4<<" "<<e5<<" "<<e6<<endl;
}

//ll BigMod(ll B,ll P,ll M){ ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R;} /// (B^P)%M

//ll gcd(ll a,ll b){if(b == 0)return a;return gcd(b,a%b);}
//ll lcm(ll a,ll b){return (a/gcd(a,b))*b;}


//int Set(int N,int pos){return N=N | (1<<pos);}
//int Reset(int N,int pos){return N= N & ~(1<<pos);}
//bool Check(int N,int pos){return (bool)(N & (1<<pos));}
//N & (N % 2 ? 0 : ~0) | ( ((N & 2)>>1) ^ (N & 1) )://XOR of 1-n numbers

int dx[] = { 0, 1,  0, -1, -1, 1,  1, -1 };
int dy[] = { 1, 0, -1,  0,  1, 1, -1, -1 };
int xx[] = { -1, 1, 2, 2,  1, -1, -2, -2 };
int yy[] = {  2, 2, 1,-1, -2, -2, -1,  1 };


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);


    bool flag[13];
    int i, j, tcase, cs=1, cnt, c;
    ll n, m, k, p, q;
    sf1(tcase);

    while(tcase--)
    {
        sf1ll(n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n", cs++);
            continue;
        }
        cnt = 0;
        c=2;
        q = n;
        memset(flag, false, sizeof flag);
        while(1)
        {
            m = q;
            //cout<<q<<endl;
            while(m)
            {
                p = m%10;
                if(!flag[p])
                {
                    cnt++;
                    flag[p] = true;
                }
                m/=10;
            }

            if(cnt == 10) break;
            q = n*c;
            c++;
        }
        printf("Case #%d: %lld\n", cs++, q);

    }

    return 0;
}

