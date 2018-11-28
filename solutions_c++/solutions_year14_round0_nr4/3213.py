/**Header file**/
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<iostream>
#include<assert.h>

/**Define file I/O **/
#define f_input freopen("input.txt","r",stdin)
#define f_output freopen("output.txt","w",stdout)

/**Define memory set function**/
#define mem(x,y) memset(x,y,sizeof(x))
#define CLEAR(x) memset(x,0,sizeof(x))

/**Define function and object**/
#define pb push_back
#define Sort(v) sort(v.begin(),v.end())
#define RSort(v) sort(v.rbegin(),v.rend())
#define CSort(v,C) sort(v.begin(),v.end(),C)
#define all(v) (v).begin(),(v).end()
#define sqr(x) ((x)*(x))
#define find_dist(a,b) sqrt(sqr(a.x-b.x)+sqr(a.y-b.y))

/**Define constant value**/
#define ERR 1e-9
#define pi 2*acos(0)
#define PI 3.141592653589793

/**Define input**/
#define scanint(a) scanf("%d",&a)
#define scanLLD(a) scanf("%lld",&a)
#define scanstr(s) scanf("%s",s)
#define scanline(l) scanf(" %[^\n]",l);

/**Define Bitwise operation**/
#define check(n, pos) (n & (1<<(pos)))
#define biton(n, pos) (n | (1<<(pos)))
#define bitoff(n, pos) (n & ~(1<<(pos)))

/**Define color**/
#define WHITE 0
#define GREY 1
#define BLACK 2

using namespace std;

/**Typedef**/
typedef vector<int> vint;
typedef vector< vint > vint2D;
typedef vector<string> vstr;
typedef vector<char>vchar;
typedef vector< vchar >vchar2D;
typedef queue<int> Qi;
typedef queue< Qi > Qii;
typedef map<int,int> Mii;
typedef map<string,int> Msi;
typedef map<int,string> Mis;
typedef stack<int> stk;
typedef pair<int,int> pp;
typedef pair<int, pp > ppp;
typedef long long int LLD;
const int inf=0x7FFFFFFF;

/**Template & structure**/
struct point_int{int x,y;point_int(){}point_int(int a,int b){x=a,y=b;}}; ///Point for x,y (int) coordinate in 2D space
struct point_double{double x,y;point_double(){}point_double(double a,double b){x=a,y=b;}}; ///Point for x,y (double) coordinate in 2D space
struct Node{int v,w;Node() {}bool operator<(const Node &a)const{return w>a.w;}Node(int _v,int _w){v=_v,w=_w;}};///Node for Dijkstra
template<class T>T gcd(T a,T b){return b == 0 ? a : gcd(b, a % b);}
template<typename T>T lcm(T a, T b) {return a / gcd(a,b) * b;}
template<class T>T big_mod(T n,T p,T m){if(p==0)return (T)1;T x=big_mod(n,p/2,m);x=(x*x)%m;if(p&1)x=(x*n)%m;return x;}
template<class T>T multiplication(T n,T p,T m){if(p==0)return (T)0;T x=multiplication(n,p/2,m);x=(x+x)%m;if(p&1)x=(x+n)%m;return x;}
template<class T>T my_pow(T n,T p){if(p==0)return 1;T x=my_pow(n,p/2);x=(x*x);if(p&1)x=(x*n);return x;} ///n to the power p
template <class T> double getdist(T a, T b){return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));}/// distance between a & b
template <class T> T extract(string s, T ret) {stringstream ss(s); ss >> ret; return ret;}/// extract words or numbers from a line
template <class T> string tostring(T n) {stringstream ss; ss << n; return ss.str();}/// convert a number to string
template<class T> inline T Mod(T n,T m) {return (n%m+m)%m;} ///For Positive Negative No.
template<class T> T MIN3(T a,T b,T c) {return min(a,min(b,c));} /// minimum of 3 number
template<class T> T MAX3(T a,T b,T c) {return max(a,max(b,c));} ///maximum of 3 number
template <class T> void print_vector(T &v){int sz=v.size();if(sz)cout<<v[0];for(int i = 1; i < sz; i++)cout << ' '<<v[i];cout<<endl;}/// prints all elements in a vector
bool isVowel(char ch){ ch=toupper(ch); if(ch=='A'||ch=='U'||ch=='I'||ch=='O'||ch=='E') return true; return false;}
bool isConsonant(char ch){if (isalpha(ch) && !isVowel(ch)) return true; return false;}

/**Shortcut input function**/
int read_int(){int n;scanf("%d",&n);return n;}
int read_LLD(){LLD n;scanf("%lld",&n);return n;}
inline int buffer_input() { char inp[1000]; scanstr(inp); return atoi(inp); }

/**Direction**/
///int col[8] = {0, 1, 1, 1, 0, -1, -1, -1};int row[8] = {1, 1, 0, -1, -1, -1, 0, 1}; ///8 Direction
///int col[4] = {1, 0, -1, 0};int row[4] = {0, 1, 0, -1}; ///4 Direction
///int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};///Knight Direction
///int dx[]={-1,-1,+0,+1,+1,+0};int dy[]={-1,+1,+2,+1,-1,-2}; ///Hexagonal Direction


/******************************Ajaira Jinish Sesh******************************/

vint nomia,ken;
int main()
{
    #ifdef _ANICK_
    f_input;
    f_output;
    #endif // _ANICK_
    int test=buffer_input();
    for(int t=1;t<=test;t++)
    {
        nomia.clear();
        ken.clear();
        int N=buffer_input();
        for(int i=0;i<N;i++)
        {
            double x;
            cin>>x;
            double X=x*1000000;
            nomia.pb((int)X);
        }
        for(int i=0;i<N;i++)
        {
            double x;
            cin>>x;
            double X=x*1000000;
            ken.pb((int)X);
        }
        Sort(nomia);
        Sort(ken);
        vint Nomia=nomia;
        vint Ken=ken;
        int deciful,war;
        deciful=war=0;
        for(int i=0;i<N;i++)
        {
            int X=nomia[i];
            bool flag=true;
            for(int j=0;j<N;j++)
            {
                if(ken[j]>X)
                {
                    ken[j]=0;
                    flag=false;
                    break;
                }
            }
            if(flag)war++;
        }
        Sort(Ken);
        for(int i=0;i<N;i++)
        {
            int X=Nomia[i];
            bool flag=true;
            for(int j=0;j<N;j++)
            {
                if(X>Ken[j]&&Ken[j]!=0)
                {
                    Ken[j]=0;
                    flag=false;
                    break;
                }
            }
            if(!flag)deciful++;
            else
            {
                for(int j=N-1;j>=0;j--)
                {
                    if(Ken[j]>X&&Ken[j]!=0)
                    {
                        Ken[j]=0;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d %d\n",t,deciful,war);
    }
    return 0;
}
