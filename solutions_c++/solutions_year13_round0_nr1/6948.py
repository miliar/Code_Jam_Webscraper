#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <deque>
#include <stack>
#include <queue>
#include <iterator>
#include <functional>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <sstream>
#include <cstdlib>
#include <iomanip>
#include <limits.h>
# include <string.h>
#define _(x,a) memset(x,a,sizeof(x))
#define LL long long
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define GC ({ char t;scanf("%c",&t);t;})
#define forn(i,n) for(int i = 0; i < (int)(n); i++)
#define forr(i,n) for(int i = (int)(n)-1; i >= 0; i--)
#define forn1(i,n) for(int i = 1; i <= (int)(n); i++)
#define forr1(i,n) for(int i = (int)(n); i >= 1; i--)
#define forit(it,x) for(it = (x).begin(); it != (x).end(); it++)
#define mp make_pair
#define pb push_back
#define fr first
#define sc second
#define sz size()
#define all(x) x.begin(), x.end()
#define double long double

#define nl printf("\n");
#define si(a) scanf("%[^\n]",a);
#define sp(a) printf("\n%s",a);
#define ip(t) printf("%d\n",t);
#define cp(t) printf("%c\n",t);
using namespace std;

typedef vector<int> vi;
//typedef vector<int64> vi64;
typedef pair<int, int> pii;
//typedef pair<int64, int64> pii64;
typedef vector< vi > vvi;
typedef vector< bool > vb;
typedef vector< char > vc;
typedef vector< vb > vvb;
typedef vector<string> vs;
typedef vector<char> vc;
typedef vector< vc > vvc;
typedef vector<double> vd;
typedef map<string, int> msi;
typedef map<int, string> mis;
typedef pair< pii, int> ppi;
typedef pair< int, pii > pip;
typedef set<int> si;
typedef map<int, vi > miv;
typedef vector< pii > vpii;
typedef map<int,int> mii;
typedef multiset<int> mlsi;

template<typename T> T gcd(T a, T b)
{
	return b ? gcd(b, a % b) : a;
}

template<typename T> T sqr(T x)
{
	return x*x;
}

template<typename T> T cube(T x)
{
	return x * x*x;
}

int main()
{
//freopen("default.cpp","r",stdin);
int t=0,m=1;
char a[4][4];
char win='X';
cin>>t;
for(m=1;m<=t;m++)
{
    int i=0,j=0,res=0,count_d=0;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
            {
                cin>>a[i][j];
                if(a[i][j]=='.')
                    count_d++;
            }
    }
//    for(i=0;i<4;i++)
//    {
//        for(j=0;j<4;j++)
//            {
//                cout<<a[i][j];
//            }
//    }
    for(i=0;i<4;i++)
    {
        int flag=-1,count_x=0,count_o=0,count_t=0;
        for(j=0;j<4;j++)
        {
            if(a[i][j]=='.')
                break;
            if(a[i][j]=='T')
                {
                    count_t++;
                }
            if(a[i][j]=='X')
                {
                    if(flag==0)
                        break;
                    else
                    {
                        flag=1;
                        count_x++;
                        //cout<<"X="<<count_x<<endl;
                    }
                }
            if(a[i][j]=='O')
                {
                    if(flag==1)
                        break;
                    else
                        {
                            flag=0;
                            count_o++;
                        }
                }

        }
        if( count_x==4 || ( count_x==3 && count_t==1))
            {
                res=1;
                win='X';
                break;
            }
        else if( count_o==4 || ( count_o==3 && count_t==1))
            {
                res=1;
                win='O';
                break;
            }

    }
if(res==0)
{
        for(j=0;j<4;j++)
    {
        int flag=-1,count_x=0,count_o=0,count_t=0;
        for(i=0;i<4;i++)
        {
            if(a[i][j]=='.')
                break;
            if(a[i][j]=='T')
                {
                    count_t++;
                }
            if(a[i][j]=='X')
                {
                    if(flag==0)
                        break;
                    else
                    {
                        flag=1;
                        count_x++;
                        //cout<<"X="<<count_x<<endl;
                    }
                }
            if(a[i][j]=='O')
                {
                    if(flag==1)
                        break;
                    else
                        {
                            flag=0;
                            count_o++;
                        }
                }

        }
        if( count_x==4 || ( count_x==3 && count_t==1))
            {
                res=1;
                win='X';
                break;
            }
        else if( count_o==4 || ( count_o==3 && count_t==1))
            {
                res=1;
                win='O';
                break;
            }

    }
}
if(res==0)
{
    int flag=-1,count_x=0,count_o=0,count_t=0;
        for(j=0,i=0;j<4,i<4;j++,i++)

    {



            if(a[i][j]=='.')
                break;
            if(a[i][j]=='T')
                {
                    count_t++;
                }
            if(a[i][j]=='X')
                {
                    if(flag==0)
                        break;
                    else
                    {
                        flag=1;
                        count_x++;
                        //cout<<"X="<<count_x<<endl;
                    }
                }
            if(a[i][j]=='O')
                {
                    if(flag==1)
                        break;
                    else
                        {
                            flag=0;
                            count_o++;
                        }
                }


        if( count_x==4 || ( count_x==3 && count_t==1))
            {
                res=1;
                win='X';
                break;
            }
        else if( count_o==4 || ( count_o==3 && count_t==1))
            {
                res=1;
                win='O';
                break;
            }

    }
}
if(res==0)
{
    int flag=-1,count_x=0,count_o=0,count_t=0;
        for(j=3,i=0;j>=0,i<4;j--,i++)

    {



            if(a[i][j]=='.')
                break;
            if(a[i][j]=='T')
                {
                    count_t++;
                }
            if(a[i][j]=='X')
                {
                    if(flag==0)
                        break;
                    else
                    {
                        flag=1;
                        count_x++;
                        //cout<<"X="<<count_x<<endl;
                    }
                }
            if(a[i][j]=='O')
                {
                    if(flag==1)
                        break;
                    else
                        {
                            flag=0;
                            count_o++;
                        }
                }


        if( count_x==4 || ( count_x==3 && count_t==1))
            {
                res=1;
                win='X';
                break;
            }
        else if( count_o==4 || ( count_o==3 && count_t==1))
            {
                res=1;
                win='O';
                break;
            }

    }
}

cout<<"Case #"<<m<<":";
if(res==1)
    {
        cout<<" "<<win<<" won\n";
    }
else
    {
        if(count_d==0)
            cout<<" Draw\n";
        else
            cout<<" Game has not completed\n";

    }
}

return 0;
}

