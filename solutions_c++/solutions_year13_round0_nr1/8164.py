
/**
 * BISMILLAHIRRAHMANIRRAHIM
 * @author Raihan
 * SUST_CSE_10
 */

#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <list>
#define MAXL 110
#define MAXS 1000010
#define MAXP 90000
#define INFIN 1001001001
using namespace std;
#define pq priority_queue
#define btc(x) __builtin_popcount(x)
#define mp(x, y) make_pair(x, y)
#define paii pair< int, int >
#define pasi pair< string, int >
#define pais pair< int, string >
#define mem(a,b) memset(a, b, sizeof(a))
#define pb(a) push_back(a)
#define pi (2*acos(0))
#define oo 1<<20
#define dd double
#define ll long long int
#define llu long long unsigned
#define ERR 1e-5
#define fst first
#define sec second
#define SZ(a) (int)a.size()
#define All(a) a.begin(),a.end()
#define FOR(i,p,k) for (i=p; i<k;i++)
#define REP(i,n) for (i=0;i<n;i++)
#define REV(i,n) for (i=n;i>=0;i--)
//int x[]={1,0,-1,0};int y[]={0,1,0,-1}; //4 Direction
//int x[]={1,1,0,-1,-1,-1,0,1};int y[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int x[]={2,1,-1,-2,-2,-1,1,2};int y[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int x[]={2,1,-1,-2,-1,1};int y[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///Power && Bigmod
//ll Pow(ll B,ll P){  ll R=1; while(P>0)  {if(P%2==1) R=(R*B);P/=2;B=(B*B);}return R;}
//int BigMod(ll B,ll P,ll M){ ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return (int)R;} /// (B^P)%M
///Sieve_Prime
//int prime[MAXP]; bool flag[MAXL];
//int sieve() { int i, j, total = 0, val;val = sqrt(MAXL)+1;flag[0]=flag[1]=1;for(i=2; i<val; i++)if(!flag[i])
//for(j=i; j*i<=MAXL; j++)flag[i*j] = 1;for(i=2; i<=MAXL; i++)if(!flag[i])prime[total++] = i; return total; }
///IntToString
//string tostring(int n) {string s, ret;do{s+=(n%10+'0');n/=10;}while(n);for(int i=s.size()-1;i>=0;i--)ret += s[i];return ret;}
///StringToInt
//int toint(string s) {int ret=0;for(int i=0;i<s.size();i++){ret=(s[i]-'0')+ret*10;}return ret;}
///StringMod
//int string_mod(string s, int b) {int ret=0;for(int i=0;i<s.size();i++){ret=(s[i]-'0'%b)+ret*10;}return ret%b;}
///GCD && LCM
template<class T> inline T lcm(T a,T b) { if(a<0)return lcm(-a,b); if(b<0)return lcm(a,-b); return a*(b/(gcd(a,b)));}
template<class T> inline T gcd(T a,T b) { if(a<0)return gcd(-a,b); if(b<0)return gcd(a,-b); return (b==0)?a:gcd(b,a%b);}

void check_p(int row, int col, char player);
char str[ MAXL ][ MAXL ], f_pl;
int cnt_r, cnt_c, cnt_rd, cnt_ld;

int main()
{
    freopen("A-small-attempt7.in","r",stdin);
    freopen("A-small-attempt7.out","w",stdout);
    int i, j, t, test;
    scanf("%d", &test);
    for(t=1; t<=test; t++)
    {
        mem( str , 0 );
        bool mark = true;
        for(i=0; i<4; i++)
        scanf("%s", &str[ i ] );
        for(i=0; i<4; i++)
            for(j=0; j<4; j++)
                if( str[i][j]=='.' ) {
                    mark = false;
                    break;
                }
        int res_x = 0, res_o = 0;
        for(i=0; i<4; i++)
        {
            for(j=0; j<4; j++)
            {
                if( str[i][j]=='X' ) {
                    check_p( i, j, 'X' );
                    if( cnt_r==4 || cnt_c==4 || cnt_rd==4 || cnt_ld==4 )
                        res_x = 1;
                }
            }
        }
        if( res_x )
            printf("Case #%d: X won\n", t);
        else
        {
            for(i=0; i<4; i++)
            {
                for(j=0; j<4; j++)
                {
                    if( str[i][j]=='O' ) {
                        check_p( i, j, 'O' );
                        if( cnt_r==4 || cnt_c==4 || cnt_rd==4 || cnt_ld==4 )
                            res_o = 1;
                    }
                }
            }
            if( res_o )
                printf("Case #%d: O won\n", t);
            else if( !mark )
                printf("Case #%d: Game has not completed\n", t);
            else
                printf("Case #%d: Draw\n", t);
        }
    }
    return 0;
}

void check_p(int row, int col, char player)
{
    int i, j, r, c;
    cnt_r = 0, cnt_c = 0, cnt_rd = 0, cnt_ld = 0;
    //row chek
    for(i=0; i<4; i++)
    {
        r = row - i;
        c = col;
        if( r<0 ) break;
        if( ( str[ r ][ c ]==player && (player=='X'||player=='O') ) )
            cnt_r++;
        if( cnt_r==3 && str[ r ][ c ]=='T' )
            cnt_r++;
    }
    for(i=1; i<4; i++)
    {
        r = row + i;
        c = col;
        if( r>=4 ) break;
        if( ( str[ r ][ c ]==player && (player=='X'||player=='O') ) )
            cnt_r++;
        if( cnt_r==3 && str[ r ][ c ]=='T' )
            cnt_r++;
    }
    //col chek
    for(i=0; i<4; i++)
    {
        r = row;
        c = col - i;
        if( c<0 ) break;
        if( ( str[ r ][ c ]==player && (player=='X'||player=='O') ) )
            cnt_c++;
        if( cnt_c==3 && str[ r ][ c ]=='T' )
            cnt_c++;
//        cout<<r<<" "<<c<<" "<<cnt_c<<endl;
    }
    for(i=1; i<4; i++)
    {
        r = row;
        c = col + i;
        if( c>=4 ) break;
        if( ( str[ r ][ c ]==player && (player=='X'||player=='O') ) )
            cnt_c++;
        if( cnt_c==3 && str[ r ][ c ]=='T' )
            cnt_c++;
//        cout<<r<<" "<<c<<" "<<cnt_c<<endl<<endl;
    }
    //rdig chek
    for(i=0; i<4; i++)
    {
        r = row - i;
        c = col - i;
        if( r<0 || c<0 ) break;
        if( ( str[ r ][ c ]==player && (player=='X'||player=='O') ) )
            cnt_rd++;
        if( cnt_rd==3 && str[ r ][ c ]=='T' )
            cnt_rd++;
    }
    for(i=1; i<4; i++)
    {
        r = row + i;
        c = col + i;
        if( r>=4 || c>=4 ) break;
        if( ( str[ r ][ c ]==player && (player=='X'||player=='O') ) )
            cnt_rd++;
        if( cnt_rd==3 && str[ r ][ c ]=='T' )
            cnt_rd++;
    }
    //ldig chek
    for(i=0; i<4; i++)
    {
        r = row - i;
        c = col + i;
        if( r<0 || c>=4 ) break;
        if( ( str[ r ][ c ]==player && (player=='X'||player=='O') ) )
            cnt_ld++;
        if( cnt_ld==3 && str[ r ][ c ]=='T' )
            cnt_ld++;
    }
    for(i=1; i<4; i++)
    {
        r = row + i;
        c = col - i;
        if( r>=4 || c<0 ) break;
        if( ( str[ r ][ c ]==player && (player=='X'||player=='O') ) )
            cnt_ld++;
        if( cnt_ld==3 && str[ r ][ c ]=='T' )
            cnt_ld++;
    }
//    cout<<"row "<<row<<" col "<<col<<" "<<cnt_r<<" "<<cnt_c<<" "<<cnt_rd<<" "<<cnt_ld<<" play "<<player<<endl<<endl;
}



/*
10
XTTT
....
OOT.
....

XOXO
OXOX
XOXO
OXOT
*/


