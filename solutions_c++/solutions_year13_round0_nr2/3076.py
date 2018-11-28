#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <set>
#include <cmath>
#include <cstring>

#include <stdio.h>
#include <string.h>
#include <sstream>
#include <stdlib.h>
#include <vector>
#include <iomanip>
#include <ctime>

using namespace std;

#ifdef __GNUC__
typedef long long ll;typedef unsigned long long ull;
#else
typedef __int64 ll;  typedef unsigned __int64 ull;
#pragma warn -csu
#endif

//Type Definition
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef vector<double>vd;
typedef vector<ll>vll;
typedef vector<string> vs;
typedef vector<vi>vvi;
typedef map<string,int> msi;
typedef map<int,int>mii;
typedef map<pii,int>mpi;

#define INF (1<<28)
#define SIZE 110
#define ERR 1e-9
#define PI 3.141592653589793

#define REP(i,n) for (i=0;i<n;i++)
#define REV(i,n) for (i=n;i>=0;i--)
#define FOR(i,p,k) for (i=p; i<k;i++)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)

#define Sort(x) sort(x.begin(),x.end())
#define Reverse(x) reverse(x.begin(),x.end())
#define MP(a,b) make_pair(a,b)
#define Clear(x,with) memset(x,with,sizeof(x))
#define SZ(x) (int)x.size()
#define length(x) (int)x.length()
#define All(x) x.begin(),x.end()
#define pb push_back
#define popcount(i) __builtin_popcount(i)
#define gcd(a,b)    __gcd(a,b)
#define lcm(a,b) ((a)*((b)/gcd(a,b)))
#define two(X) (1<<(X))
#define twoL(X) (((ll)(1))<<(X))
#define setBit(mask,i) (mask|two(i))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define maximum(v) *max_element(All(v))
#define minimum(v) *min_element(All(v))
#define X first
#define Y second
#define CS c_str()
#define EQ(a,b) (fabs(a-b)<ERR)

//For debugging
template<class T> void debug(T e){cout<<e<<endl;}
template<class T1,class T2> void debug(T1 e1,T2 e2){cout<<e1<<"\t"<<e2<<endl;}
template<class T1,class T2,class T3> void debug(T1 e1,T2 e2,T3 e3){cout<<e1<<"\t"<<e2<<"\t"<<e3<<endl;}
template<class T1,class T2,class T3,class T4> void debug(T1 e1,T2 e2,T3 e3,T4 e4){cout<<e1<<"\t"<<e2<<"\t"<<e3<<"\t"<<e4<<endl;}
template<class T1,class T2,class T3,class T4,class T5> void debug(T1 e1,T2 e2,T3 e3,T4 e4,T5 e5){cout<<e1<<"\t"<<e2<<"\t"<<e3<<"\t"<<e4<<"\t"<<e5<<endl;}
template<class T> void debug(vector<T> e){int i;REP(i,SZ(e)) cout<<e[i]<<" ";cout<<endl;}
template<class T> void debug(vector<T> e,int n){int i;REP(i,n) cout<<e[i]<<" ";cout<<endl;}
template<class T> void debug(vector< basic_string<T> > e){int i,j;REP(i,SZ(e)) {REP(j,SZ(e[i])) cout<<e[i][j];cout<<endl;} cout<<endl;}
template<class T> void debug(vector< basic_string<T> > e,int row,int col){int i,j;REP(i,row) {REP(j,col) cout<<e[i][j];cout<<endl;} cout<<endl;}
template<class T> void debug(vector< vector<T> > e,int row,int col){int i,j;REP(i,row) {REP(j,col) cout<<e[i][j]<<"\t";cout<<endl;} cout<<endl;}
template<class T> void debug(T e[SIZE][SIZE],int row,int col){int i,j;REP(i,row) {REP(j,col) cout<<e[i][j]<<" ";cout<<endl;}}
template<class T> void debug(T e[],int row){int i;REP(i,row) cout<<e[i]<<" ";cout<<endl;}

//Important Functions
template< class T > void setmax(T &a, T b) { if(a < b) a = b; }
template< class T > void setmin(T &a, T b) { if(b < a) a = b; }
template<class T> T Abs(T x) {return x > 0 ? x : -x;}
template<class T> inline T sqr(T x){return x*x;}
template<class T> inline bool isPrime(T n){if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
template<class T> inline T Mod(T n,T m) {return (n%m+m)%m;} //For Positive Negative No.

//int,double is converted to string
template<class T> string toString(T n){ostringstream oss;oss<<n;oss.flush();return oss.str();}
//string is converted to int
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
//string is converted to Long long
ll toLl(string s){ll r=0;istringstream sin(s); sin>>r; return r;}
//string is coverted to Double
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toDouble
//check character is vowel
bool IsVowel(char ch){ch=tolower(ch);if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u')return true;return false;}
//isUpperCase
bool isUpperCase(char c){return c>='A' && c<='Z';}
//isLowerCase
bool isLowerCase(char c){return c>='a' && c<='z';}
//compute b^p
ll Pow(ll B,ll P){  ll R=1; while(P>0)  {if(P%2==1) R=(R*B);P/=2;B=(B*B);}return R;}
//compute b^p%m
int BigMod(ll B,ll P,ll M){ ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return (int)R;}
/*calculates (a*b)%c taking into account that a*b might overflow */
ll mulmod(ll a,ll b,ll c){ ll x = 0,y=a%c; while(b>0){ if(b%2 == 1){x=(x+y)%c;} y=(y*2)%c;b/= 2;}return x%c;}
//print a number in binary format with n length
void binprint(ll mask,ll n){ll i;string s="";do{s+=(mask%2+'0');mask/=2;}while(mask);Reverse(s);s=string(max(n-SZ(s),0LL),'0')+s;for(i=SZ(s)-n;i<SZ(s);i++) printf("%c",s[i]);printf("\n");}
//ASCII Chart
void ASCII_Chart(){int i,j,k;printf("ASCII Chart:(30-129)\n");FOR(i,30,50){REP(j,5){k=i+j*20;printf("%3d---> '%c'   ",k,k);}printf("\n");}}
//SubstringGenerate
vector<string> SubstringGenerate(string str){int i,j,len;vs store;len=SZ(str);REP(i,len) FOR(j,i,len)store.pb(str.substr(i,j-i+1));return store;}
//Degree to Radian
double deg2rad(double x){ return (PI*x)/180.0; }
//Radian to Degree
double rad2deg(double x){ return (180.0*x)/PI; }

//int month[]={-1,31,28,31,30,31,30,31,31,30,31,30,31};  //Not Leap Year
//string monthName[]={"","JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"};
//string dayName[]={"SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"};

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[]={-1,-1,+0,+1,+1,+0};int dy[]={-1,+1,+2,+1,-1,-2}; //Hexagonal Direction

//#include<conio.h> //for using getch();

//struct pq{ int cost,node; pq(int _cost=0,int _node=0){cost=_cost;node=_node;}bool operator<(const pq &b)const {return cost>b.cost;}}; // Min Priority Queue
//bool comp(pq a,pq b){ return a.cost < b.cost;} //Asc Sort by cost

int main(){
 freopen("B-large.in","r",stdin);
 freopen("outB.txt","w",stdout);
 
 long t,i,j,k,n,m,max;
 int a[200][200],b[200][200],f=0;
 
 cin>>t;
 
 for(k=1;k<=t;k++){
   cin>>n>>m;
   f=0;
   for(i=0;i<n;i++){
     for(j=0;j<m;j++){
       cin>>a[i][j];
       b[i][j]=100;               
     }               
   }
   
   cout<<"Case #"<<k<<": ";
   
   for(i=0;i<n;i++){
     max=0;
     for(j=0;j<m;j++){
       if(a[i][j]>max)
         max=a[i][j];               
     }
     for(j=0;j<m;j++){
       b[i][j]=max;              
     }               
   }                
   
   for(i=0;i<m;i++){
     max=0;
     for(j=0;j<n;j++){
       if(a[j][i]>max)
         max=a[j][i];               
     }
     for(j=0;j<n;j++){
       if(b[j][i]>max)
         b[j][i]=max;              
     }               
   }
   
   for(i=0;i<n;i++){
     for(j=0;j<m;j++){
       if(a[i][j]!=b[i][j]){
         f=1;
         break;                   
       }               
     }
     if(f==1)
     break;               
   }                
   
   if(f==1)
     cout<<"NO"<<endl;
     else
       cout<<"YES"<<endl;                     
 }
      
 return 0;
}
