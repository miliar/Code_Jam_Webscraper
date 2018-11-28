

/*
         ________
        / ______ \
       / /      \ \
      / /        \ \
     / /          \_|
 ___| |_____________________________________
(__   _________  ________  _____   ________)
    | |        /  \       \ \    | |  __
    | |       / /\ \       \ \   | | //\\
    | |      | /_ \ \       \ \__| |//__\\
    | | __    \_ \ \ \      /  __  |  __ |
    | | \ \    / /  \ |    /  /  | |\\  //
    | |  \ \  / /   / /   /  /   | | \\//
    | |   \ \/ /   / /    \ |    | |
    | |    \__/   / /      \ \___| |
    |_|          /_/        \____  |
                             ____| |__
                            |  __  __ \
                             \ \/ /  \ \__
                              \__/    \___)
*/

/// 01001010 01101001 01110011 01101000 01101110 01110101

/*

          JJJJJJJJJJJ IIIIIIIIII    SSSSSSSSSSSSSSS  HHHHHHHHH     HHHHHHHHH NNNNNNNN        NNNNNNNN UUUUUUUU     UUUUUUUU
          J:::::::::J I::::::::I  SS:::::::::::::::S H:::::::H     H:::::::H N:::::::N       N::::::N U::::::U     U::::::U
          J:::::::::J I::::::::I S:::::SSSSSS::::::S H:::::::H     H:::::::H N::::::::N      N::::::N U::::::U     U::::::U
          JJ:::::::JJ II::::::II S:::::S     SSSSSSS HH::::::H     H::::::HH N:::::::::N     N::::::N UU:::::U     U:::::UU
            J:::::J     I::::I   S:::::S               H:::::H     H:::::H   N::::::::::N    N::::::N  U:::::U     U:::::U
            J:::::J     I::::I   S:::::S               H:::::H     H:::::H   N:::::::::::N   N::::::N  U:::::D     D:::::U
            J:::::J     I::::I    S::::SSSS            H::::::HHHHH::::::H   N:::::::N::::N  N::::::N  U:::::D     D:::::U
            J:::::J     I::::I     SS::::::SSSSS       H:::::::::::::::::H   N::::::N N::::N N::::::N  U:::::D     D:::::U
            J:::::J     I::::I       SSS::::::::SS     H:::::::::::::::::H   N::::::N  N::::N:::::::N  U:::::D     D:::::U
JJJJJJJ     J:::::J     I::::I          SSSSSS::::S    H::::::HHHHH::::::H   N::::::N   N:::::::::::N  U:::::D     D:::::U
J:::::J     J:::::J     I::::I               S:::::S   H:::::H     H:::::H   N::::::N    N::::::::::N  U:::::D     D:::::U
J::::::J   J::::::J     I::::I               S:::::S   H:::::H     H:::::H   N::::::N     N:::::::::N  U::::::U   U::::::U
J:::::::JJJ:::::::J   II::::::II SSSSSSS     S:::::S HH::::::H     H::::::HH N::::::N      N::::::::N  U:::::::UUU:::::::U
 JJ:::::::::::::JJ    I::::::::I S::::::SSSSSS:::::S H:::::::H     H:::::::H N::::::N       N:::::::N   UU:::::::::::::UU
   JJ:::::::::JJ      I::::::::I S:::::::::::::::SS  H:::::::H     H:::::::H N::::::N        N::::::N     UU:::::::::UU
     JJJJJJJJJ        IIIIIIIIII  SSSSSSSSSSSSSSS    HHHHHHHHH     HHHHHHHHH NNNNNNNN         NNNNNNN       UUUUUUUUU

*/

/// Etorri nintzen ikusi nuen eta ni konkistatu.

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

using namespace std;

#define ms(a,b)             memset(a, b, sizeof(a))
#define pb(a)               push_back(a)
#define pi                  (2*acos(0))
#define oo                  0x7e7e7e7e
#define dd                  double
#define ll                  long long
#define ff                  float
#define MP                  make_pair
#define ERR                 10E-7
#define fr                  first
#define sc                  second
#define SZ(a)               (int)a.size()
#define all(a)              a.begin(),a.end()

#define intlim              2147483648
#define rtintlim            46340
#define llim                9223372036854775808
#define rtllim              3037000499

#define pall                pair<ll,ll>
#define padd                pair<dd,dd>
#define paii                pair<int,int>
#define ull                 unsigned long long
#define csprint             printf("Case %lld:\n", C++)
#define bpc                 __builtin_popcount
#define EQ(a,b)             (fabs(a-b)<ERR)
#define fast_input_output   ios_base::sync_with_stdio(0);cin.tie(0);
#define I                   int

#define rep(i,n)            for(int i=0; i<n; i++)
#define per(i,n)            for(int i=n-1; i>=0; i--)

using namespace std;

//ll Pow(ll B,ll P){      ll R=1; while(P>0)      {if(P%2==1)     R=(R*B);P/=2;B=(B*B);}return R;}
//int BigMod(ll B,ll P,ll M){     ll R=1; while(P>0)      {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return (int)R;} /// (B^P)%M
//ll Gcd(ll a,ll b){ if(b==0)return a; Gcd(b,a%b); return;}

///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1};                       //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};   //8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1}; //Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1};            //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31};               //month

//ll fact[] = {1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87178291200,1307674368000,20922789888000,355687428096000,6402373705728000,121645100408832000,2432902008176640000};

#define max_x 1010
#define max_y 1010

ll T, C=1, N, kas=0;

void process()
{
    cin>>T;
    while(T--)
    {
        ll O_O;string s;
        cin>>O_O>>s;
        ll ct=0, tot=0;
        for(I i=0; i<SZ(s); i++)
        {
            I a = s[i]-'0';
            if(tot<i)
            {
                ct+=i-tot;
                tot+=i-tot+a;
            }
            else
            {
                tot+=a;
            }
        }
        cout<<"Case #"<<++kas<<": "<<ct<<endl;
    }
    return;
}

int main()
{
    //fast_input_output
    freopen("input_a_large.txt","r",stdin);
    freopen("output_a_large.txt","w",stdout);

    process();
    return 0;
}

