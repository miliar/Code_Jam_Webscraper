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
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);


    char st[110], ch;
    int i, j, len, cnt, tcase, cs=1;
    sf1(tcase);

    for(j=1; j<=tcase; j++)
    {
        cin>>st;
        len = strlen(st);
        cnt = 0;
        ch = '+';
        for(i=len-1; i>=0; i--)
        {
            if(st[i] != ch)
            {
                cnt++;
                ch = st[i];
            }
        }

        printf("Case #%d: %d\n", j, cnt);
    }

    return 0;
}

