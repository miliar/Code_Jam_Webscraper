using namespace std;
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<bitset>

#include<climits>
#include<cstring>
#include<cstdio>
#include<cmath>

template <class T> string toStr(const T &x)
{ stringstream s; s << x; return s.str(); }

template <class T> int toInt(const T &x)
{ stringstream s; s << x; int r; s >> r; return r; }

#define MPI acos(-1)
#define fr(i,j,n) for(int i=j;i<n;++i)
#define FR(i,n) fr(i,0,n)
#define foreach(x,v) for(typeof (v).begin() x = (v).begin(); x!= (v).end(); x++)
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define RI(x) scanf("%d",&x)
#define DRI(x) int x;RI(x)
#define RII(x,y) scanf("%d%d",&x,&y)
#define DRII(x,y) int x,y;RII(x,y)
#define PI(x) printf("%d ",x)
#define PIS(x) printf("%d\n",x)
#define D(x) cout<< #x " = "<<(x)<<endl
#define Dd(x) printf("#x = %lf\n", x)
#define Dbg if(1)
#define PB push_back
#define MK make_pair
#define F first
#define S second

typedef long long ll;
typedef vector<ll> vl;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vs> vss;
typedef vector<int,int> vii;
typedef vector<vi> vvi;
typedef pair <int,int> pii;
typedef pair <double,double> pdd;
typedef map<string,int> msi;
typedef long long int lli;

bool mycmp (pair<string,int> a,pair<string,int> b) { return (a.second<b.second); }

bool checkNum(lli a)
{
   int reverse = 0, temp; 
   temp = a;
 
   while( temp != 0 )
   {
      reverse = reverse * 10;
      reverse = reverse + temp%10;
      temp = temp/10;
   }
 
   if ( a == reverse )
      return true;
   else
     return false;
}
int MAXN = 1000;
int main()
{
    int t;
    vector<lli> myGood;
    for(ll i = 1; i*i <= MAXN ; i++)
    {
       lli t = i*i;
       if(checkNum(t) && checkNum(i))
          myGood.PB(t);
    }       
    cin >> t;
    FR(j,t)
    {
       lli a,b;
       scanf("%lld %lld", &a, &b);
       int cont = 0;
       FR(i,myGood.size())
       {
          if(myGood[i] >= a && myGood[i] <=b)
             cont++;
       }           
       cout<<"Case #"<<j+1<<": "<<cont<<endl;
     }
     return 0;
 }
    
    
    
    
    
    
    
    
