
/*
   ______    _____
        |    |    \
        |    |     \
        |    |_____/
   \-   |    |     \
    \  /     |     /
     \/      |____/


*/


/*Mes que un equipe*/

//জিষ্ণু ব্যানার্জী
//একজন পরিত্যাক্ত কোডার
//জীবনের কারাগারে আজীবন সাজাপ্রাপ্ত একজন আসামী


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
#include <bitset>
#include <ctime>

#define ms(a,b) memset(a, b, sizeof(a))
#define pb(a) push_back(a)
#define pi (2*acos(0))
#define oo 1<<29
#define dd double
#define ll long long
#define ff float
#define MP make_pair
#define ERR 10E-7
#define fr first
#define sc second
#define SZ(a) (int)a.size()
#define all(a) a.begin(),a.end()

#define intlim 2147483648
#define rtintlim 46340
#define llim 9223372036854775808
#define rtllim 3037000499

#define pall pair<ll,ll>
//#define MUL 100000
#define padd pair<dd,dd>
#define paii pair<int,int>
#define ull unsigned long long
#define csprint printf("Case %lld:\n", C++)
#define bpc __builtin_popcount
#define EQ(a,b)     (fabs(a-b)<ERR)
#define fast_input_output ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

//ll Pow(ll B,ll P){      ll R=1; while(P>0)      {if(P%2==1)     R=(R*B);P/=2;B=(B*B);}return R;}
//int BigMod(ll B,ll P,ll M){     ll R=1; while(P>0)      {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return (int)R;} /// (B^P)%M
//ll Gcd(ll a,ll b){ if(b==0)return a; Gcd(b,a%b); return;}

///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

//ll fact[] = {1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87178291200,1307674368000,20922789888000,355687428096000,6402373705728000,121645100408832000,2432902008176640000};

#define max_x 1010
#define max_y 1010

ll T, C=1, N;
vector<dd>nao, ken;
bool color[10000];

void process()
{
    cin>>T;
    int MUL = 100000;
    while(T--)
    {
        nao.clear();
        ken.clear();
        ms(color,0);
        cin>>N;
        for(int i=0; i<N; i++)
        {
            dd x;int y;
            cin>>x;y=x*MUL;
            nao.pb(x);
        }
        for(int i=0; i<N; i++)
        {
            dd x;int y;
            cin>>x;y=x*MUL;
            ken.pb(x);
        }
        sort(all(nao));
        sort(all(ken));
//        for(int i=0; i<N; i++)
//        {
//            cout<<nao[i]<<"  "<<ken[i]<<endl;
//        }

        int ct1=0, ct2=0;
        for(int i=N-1; i>=0; i--)
        {
            bool flag = false;
            for(int j=0; j<N; j++)
            {
                if(nao[i]<ken[j] and !color[j])
                {
//                    cout<<i<<" "<<j<<endl;
                    color[j]=true;
                    flag = true;
                    break;
                }
            }
            if(!flag)
            {
                for(int j=0; j<N; j++)
                {
                    if(!color[j])
                    {
//                        cout<<i<<" "<<j<<endl;
                        color[j]=true;
                        flag = true;
                        ct1++;
                        break;
                    }
                }
            }
        }
        //
        ms(color,0);
        for(int i=N-1; i>=0; i--)
        {
            bool flag = false;
            for(int j=0; j<N; j++)
            {
                if(ken[i]<nao[j] and !color[j])
                {
//                    cout<<i<<" "<<j<<endl;
                    color[j]=true;
                    flag = true;
                    ct2++;
                    break;
                }
            }
            if(!flag)
            {
                for(int j=0; j<N; j++)
                {
                    if(!color[j])
                    {
//                        cout<<i<<" "<<j<<endl;
                        color[j]=true;
                        flag = true;
                        break;
                    }
                }
            }
        }
        cout<<"Case #"<<C++<<": ";
        cout<<ct2<<" "<<ct1<<endl;
    }
    return;
}

int main()
{
    fast_input_output
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    process();
    return 0;
}
