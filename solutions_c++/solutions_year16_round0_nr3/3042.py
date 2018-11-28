#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define s(n)                        scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%ld",&n)
#define sll(n)                      scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ssp(n)                      scanf("%[^\n]%*c",n)
#define prt(x)        	            printf("%d\n",x);
#define plt(x)				printf("%lld\n",x);

#define INF                   	0x3f3f3f3f
#define EPS                         1e-12

#define bitcount                    __builtin_popcount
#define gcd                         __gcd

#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define rall(a)                     a.rbegin(),a.rend()

#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                   memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
#define dot(a,b)                    ((conj(a)*(b)).X)
#define cross(a,b)                  ((conj(a)*(b)).imag())
#define normalize(v)                ((v)/length(v))
#define rotate(p,about,theta)       ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b)               (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

#define maX(a,b)                     ( (a) > (b) ? (a) : (b))
#define miN(a,b)                     ( (a) < (b) ? (a) : (b))
#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef stringstream ss;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<vector<int> > vvi;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

char *strrev(char *str)
{
      char *p1, *p2;

      if (! str || ! *str)
            return str;
      for (p1 = str, p2 = str + strlen(str) - 1; p2 > p1; ++p1, --p2)
      {
            *p1 ^= *p2;
            *p2 ^= *p1;
            *p1 ^= *p2;
      }
      return str;
}

int a,b,i,j; 
char sa[33]; 
char sb[33];

void rev(char s[]) 
{
      int l=strlen(s);
      for(int i=0; i<l-1-i; i++)
       swap(s[i],s[l-1-i]);
}
void multi(char s[], int k) 
{
      int i, c=0, d;
      for(i=0;s[i];i++)
      {
            d=(s[i]-'0')*k+c;
            c=d/b; 
            d%=b;
            s[i]='0'+d;
      }
      while(c)
      {
            s[i]='0'+(c%b);
            i++;
            c/=b;
      }
      s[i]='\0';
}
void add(char s[], int k) 
{
      int i, c=k, d;
      for(i=0;s[i];i++)
      {
            d=(s[i]-'0')+c;
            c=d/b; 
            d%=b;
            s[i]='0'+d;
      }
      while(c)
      {
            s[i]='0'+(c%b); 
            i++;
            c/=b;
      }
      s[i]='\0';
}
void trans(char s[]) 
{
      int i;
      for(i=0;s[i];i++)
      {
            char& c=s[i];
            if(c>='A' && c<='Z') c='0'+10+(c-'A');
            if(c>='a' && c<='z') c='0'+36+(c-'a');
      }
}
void itrans(char s[]) 
{
      int i;
      for(i=0;s[i];i++)
      {
            char& c=s[i];
            int d=c-'0';
            if(d>=10 && d<=35) c='A'+(d-10);
            if(d>=36) c='a'+(d-36);
      }
}
void conv()
{
      sb[0]='0'; 
      sb[1]='\0';
      trans(sa);
      for(i=0;sa[i];i++)
      {
            multi(sb, a);
            add(sb, sa[i]-'0');
      }
      rev(sb);
      itrans(sb);
}

#define SMALL
//#define LARGE

int main()
{

#ifdef SMALL
      freopen("C-small-attempt0.in","rt",stdin);
      freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
      freopen("C-large.in","rt",stdin);
      freopen("C-large.out","wt",stdout);
#endif

int ce,t,j,ctr;
vector<ll> divisors;
s(t);
forall(w,1,t+1)
{
      s(ce);
      s(j);
      printf("Case #%d:\n",w);
      ll lm=pow(2,ce-2);
      ll num=pow(2,ce-1)+1;
      ctr=0;
      
      forall(k,0,lm)
      {
            bool flag=true;
            sprintf(sa,"%lld",num);
            a=10; b=2;
            conv();

            num++;
            if(num%2==0)
                  num++;
            
            strcpy(sa,sb);
            divisors.clear();

            forall(p,2,11)
            {
                  a=p;
                  b=10;
                  conv();           
                  if(flag)
                  {
                        ll x=0,z;
                        for(i=0;sb[i]!='\0';i++)
                              x=(x*10)+( (int)sb[i]-48 );
                       
                        for(z=2; z<sqrt(x); z++)
                        {
                              if(x%z==0)
                              {
                                    flag=true;
                                    divisors.pb(z);
                                    break;
                              }
                              else
                                    flag=false;
                        }
                  }
            }
            
            if(flag)
            {
                  ++ctr;
                  printf("%s ",sa);
                  forall(v,0,8)
                        printf("%lld ",divisors[v]);
                  printf("%lld\n",divisors[8]);
            }
            if(ctr>=j)
                  break;   
      }
}
return 0;
}