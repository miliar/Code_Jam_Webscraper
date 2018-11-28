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

#define PI 3.141592653589793
#define fr(i,j,n) for(int i=j;i<n;++i)
#define FR(i,n) fr(i,0,n)
#define foreach(x,v) for(typeof (v).begin() x = (v).begin(); x!= (v).end(); x++)
#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define RI(x) scanf("%d",&x)
#define DRI(x) int x;RI(x)
#define RII(x,y) scanf("%d%d",&x,&y)
#define DRII(x,y) int x,y;RII(x,y)
//#define PI(x) printf("%d ",x)
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
typedef long double ld;

int main()
{
   int t;
   cin >> t;
   FR(i,t)
   {
      ld r,b;
      cin >> r >> b;
      lli circles = 0;
      ld whiteCircle = r;
      ld blackCircle = 0.0;
      lli cont = 0;
      while(true)
      {  
         if(cont%2 != 0){         
             whiteCircle = blackCircle +1.0;
             //cout<<whiteCircle<<endl;
             cont++;
         }
         else
         {
             blackCircle = whiteCircle + 1.0;
             ld area =  (PI*(blackCircle*blackCircle)) - (PI*(whiteCircle*whiteCircle));
             ld milneed = area/PI;
             //cout<<blackCircle<<" "<<area<<" "<<PI<<" "<<b<<" "<<milneed<<endl;
             if(fabs(milneed - b) < 0.00001 || milneed < b){
                circles ++;
                b -= milneed;
                cont++;
                continue;
             }
             else if(b < milneed)
                break;
             
         }
      }
      cout<<"Case #"<<i+1<<": "<<circles<<endl;
   }
   return 0;
}
         
         
      
      
      
      
      
      
      
      
      
      
   
