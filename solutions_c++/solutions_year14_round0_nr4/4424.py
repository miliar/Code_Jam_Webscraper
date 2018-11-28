#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <fstream>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz size()
#define bg begin()
#define en end()
#define Y second
#define X first
typedef long long ll;

#define fi freopen("input.txt","r",stdin)
#define fo freopen("output.txt","w",stdout)

const double pi     =   acos(-1.0);
const double eps    =   1e-8;

#define print(a) cout<<(#a)<<" = "<<a<<"  ";
#define println(a) cout<<(#a)<<" = "<<a<<"\n";
#define fill(a,val) memset(a ,val, sizeof(a) );

vector <string> parse(string s, string c)
{
  int len = c.length(), p = -len, np;
  vector <string> ans;

  do
    {
      np = s.find(c, p+len);
      ans.push_back(s.substr(p+len, np - p - len));
      p = np;
    }
  while (p != string::npos);

  return ans;
}


/*Solution code starts here */

#define maxn (1<<10)


int n;

int memo[maxn+10][maxn+10];
int memo2[maxn+10][maxn+10];

vector<double> a,b;

int  fair( int x, int y)
{
    if( (x==0) && (y==0) )
    {
        return 0;
    }

    int &ans=memo[x][y];

    if(ans!=-1)
         return ans;

    ans=0;

    for(int i=0;i<n;i++)
         if( x &(1<<i) )
        {
                 //find if larger , else find smallet one

                   int id=-1;
                   int add=0;

                    for(int j=0;j<n;j++)
                         if( y & (1<<j) )
                          if( a[i] < b[j] )
                          {
                              id=j;
                              break;
                          }

                    if(id==-1)
                    {
                           for(int j=0;j<n;j++)
                              if( y & (1<<j) )
                             {
                               id=j;
                               add=1;
                               break;
                             }
                    }

                    int nx=x^(1<<i);
                    int ny=y^(1<<id);

                    ans=max( ans , fair(nx,ny)+add);

        }

        return ans;
}


int  unfair( int x, int y)
{
    if( (x==0) && (y==0) )
    {
        return 0;
    }

    int &ans=memo2[x][y];

    if(ans!=-1)
         return ans;

    ans=0;

    for(int i=0;i<n;i++)
         if( x &(1<<i) )
        {
                 //find if larger , else find LARGEST one , that is not fit

                   int id=-1;
                   int add=0;

                    for(int j=n-1;j>=0;j--)
                         if( y & (1<<j) )
                          if( a[i] < b[j] )
                          {
                              id=j;
                              break;
                          }

                    if(id==-1)
                    {
                           for(int j=n-1;j>=0;j--)
                              if( y & (1<<j) )
                             {
                               id=j;
                               add=1;
                               break;
                             }
                    }

                    int nx=x^(1<<i);
                    int ny=y^(1<<id);

                    ans=max( ans , unfair(nx,ny)+add);

        }

        return ans;
}


void process( int t)
{
    cin>>n;

     a.resize(n);
     b.resize(n);

    for(int i=0;i<n;i++)
         cin>>a[i];

    for(int i=0;i<n;i++)
          cin>>b[i];

    sort(a.bg,a.en);
    sort(b.bg,b.en);

//
//      cout<<"\n\n";
//
//       for(int i=0;i<n;i++)
//         cout<<a[i]<<"  ";
//
//      cout<<"\n\n";
//
//    for(int i=0;i<n;i++)
//          cout<<b[i]<<"  ";
//
//          cout<<"\n\n";


   //fair game

    fill(memo,-1);

    int mask=(1<<n)-1;
    int z=fair( mask,mask);

       //Unfair game

    fill(memo2,-1);

     mask=(1<<n)-1;
    int y=unfair( mask,mask);


    cout<<"Case #"<<t<<": "<<y<<" "<<z<<endl;

}

int main()
{

   fi;fo;


   int test;


   cin>>test;

   for(int i=1;i<=test;i++)
     process(i);


 return 0;

}
