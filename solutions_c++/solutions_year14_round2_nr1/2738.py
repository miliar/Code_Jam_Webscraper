#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<iostream>
#include<set>
#include<map>
#include<list>
#include<string>
#include<stack>
#include<queue>
#include<sstream>
using namespace std;

// Template By @li_@kber
typedef long long int ll;
typedef unsigned long long int ull;
const double pi=acos(-1.0);
int parent[100001];
int inf=100000000;
//int row[]={1,0,-1,0};int col[]={0,1,0,-1}; //4 Direction
//int row[]={1,1,0,-1,-1,-1,0,1};int col[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int row[]={2,1,-1,-2,-2,-1,1,2};int col[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int row[]={-1,-1,+0,+1,+1,+0};int col[]={-1,+1,+2,+1,-1,-2}; //Hexagonal Direction

#define ri(N) scanf("%d",&N)
#define rll(N) scanf("%lld",&N)
#define rs(N) scanf("%s",N)
#define eps 1e-9
#define Sort(x) sort(x.begin(),x.end())
#define Reverse(x) reverse(x.begin(),x.end())
#define tonum(c) (c>='A'&&c<='Z'?c-'A' : c-'a'+26)
#define all(X)  X.begin(),X.end()
#define UNIQUE(X)  X.resize(unique(all(X))-X.begin())
#define tr(container,it)  for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
//////////////////////////////////////////////////////////////////////
// Numberic Functions
int day(int y,int m,int d)
  {if(m<3){--y;m+=12;}return 365*y+y/4 - y/100+y/400+(153*m - 457)/5+d - 306;}
ll josephus(ll x) // If the 2nd person is killed always then the last man
  {return 2*(x-pow(2,(ll)log2(x)))+1;}
ll josephus(ll n,ll x) // If the 2nd person is killed always then the x'th man
  {if(n==1&&x==1)return 1;if(n>1&&x==1)return 2;ll res=josephus(n-1,x-1);if(res==n-1)return 1;if(res<=n-2)return res+2;}
ll survivor(ll n,ll k) // If the k'th person is killed always then the last man
  {ll i,s;for(s=0,i=1;i<=n;i++)s=(s+k)%i;return (s+1);}
template<class T> inline T gcd(T a,T b)
  {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)
  {if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> T power(T N,T P)  // a^b
  {return (P==0)? 1: N*power(N,P-1);}
template<class T> inline T mod(T N,T M)  // n%mod
  {if(N<0)N+=(ceil(-N*1.00/M)*M);return N%M;}
template<class T> T bigmod(T a,T b,T mod)  //(a^b)%mod
  {if(b==0)return 1;if(b%2==0){T ret=bigmod(a,b/2,mod);return ((ret%mod)*(ret%mod))%mod;}else return ((a%mod)*(bigmod(a,b-1,mod)%mod))%mod;}
template<class T> inline double distance_point(pair<T,T>P,pair<T,T>Q)
  {T X1,X2,Y1,Y2;X1=P.first,Y1=P.second;X2=Q.first,Y2=Q.second;return sqrt((X1-X2)*(X1-X2)+(Y1-Y2)*(Y1-Y2));}
// String conversion
template<class T> ll stoi(T Str){stringstream ss(Str);ll N;ss>>N;return N;}
template<class T> string itos(T N){stringstream ss;ss<<N;string Str;Str=ss.str();return Str;}
template<class T> vector<int> vstoi(T Str){stringstream ss(Str);vector<int>A;for(int N;ss>>N;A.push_back(N));return A;}
vector<string> split(string str,string Separator)
  {vector<string>answer;string temp;for(int i=0;i<str.length();i++){bool isSeparator=false;for(int j=0;j<Separator.length();j++)if(str[i]==Separator[j])isSeparator=true;if(!isSeparator){temp+=str[i];continue;}if(temp!="")answer.push_back(temp);temp="";}if(temp!="")answer.push_back(temp);return answer;}
// Working with bit
ll check_bit(ll N,int POS){return (N & (1LL<<POS));}
ll on_bit(ll N,int POS){return N | (1LL<<POS);}
ll off_bit(ll N,int POS){return N & ~(1LL<<POS);}
int find_parent(int x)
  {if(parent[x]!=x)parent[x]=find_parent(parent[x]);return parent[x];}
string from_decimal_to(ll n, int b)  // Upto base 20
  {if(n==0)return "0";string chars="0123456789ABCDEFGHIJ";string result="";while(n>0){result=chars[n%b]+result;n/=b;}return result;}
#define pb push_back
#define ff first
#define ss second
#define MP make_pair
#define ii pair<int,int>
#define pp1 pair<int,pair<int,int> >
#define pp2 pair<pair<int,int>,int >
#define pq(xx) priority_queue<xx,vector<xx>,greater<xx> >
//////////////////////////////////////////////////////////////////////

int main()
{
    freopen("A-small-attempt6.in","r",stdin);
    freopen("A-small-attempt6.out","w",stdout);
    int i,j,k,l,m,n,t,kase=1;
    ri(t);
    while(t--)
    {
        vector<string>v;
        string str;
        ri(n);
        for(i=0;i<n;i++)
        {
            cin>>str;
            v.push_back(str);
        }
        set<char>st;
        str=v[0];
        for(i=0;i<str.size();i++)
            st.insert(str[i]);
        for(i=0;i<n;i++)
        {
            set<char>temp;
            for(j=0;j<v[i].size();j++)
                temp.insert(v[i][j]);
            if(st==temp)
                continue;
            else
                break;
        }
        if(i<n)
        {
            printf("Case #%d: Fegla Won\n",kase++);
            continue;
        }
        vector<char>ch;
        str=v[0];
        for(i=1;i<=str.size();i++)
        {
            if(str[i]!=str[i-1])
                ch.push_back(str[i-1]);
        }
        m=ch.size();
        vector<int>total(m+1,0);
        int state[n+1][m+1];
        memset(state,0,sizeof(state));
        int cond=1;
        for(i=0;i<n;i++)
        {
            str=v[i];
            int pos=0;
            for(j=0;j<m;j++)
            {
                while(ch[j]==str[pos])
                {
                    state[i][j]++;
                    pos++;
                }
                if(state[i][j]==0)
                    cond=0;
            }
            if(pos<str.size())
                cond=0;
        }
        if(cond==0)
        {
            printf("Case #%d: Fegla Won\n",kase++);
            continue;
        }
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
                total[i]+=state[j][i];
            total[i]=total[i]/n;
        }
        int cnt=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                int temp=abs(total[j]-state[i][j]);
                cnt+=temp;
            }
        }
        printf("Case #%d: %d\n",kase++,cnt);
    }
return 0;
}
