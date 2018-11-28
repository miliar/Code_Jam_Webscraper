#include <iostream>
#include <fstream>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>

using namespace std;

const double eps=1e-11;
//const double pi=acos(-1.0);
typedef long long ll;
typedef long long int lli;
typedef unsigned long long ull;
typedef long double ld;


#define ff first
#define ss second
#define pb push_back
#define mkp make_pair
#define lpu(i,s,e) for(i=s;i<e;i++)
#define lpd(i,s,e) for(i=s;i>e;i--)
#define lpui(i,s,e) for(i=s;i<=e;i++)
#define lpdi(i,s,e) for(i=s;i>=e;i--)
#define abs(a) (a<0?-(a):a)
#define nl() cout << '\n'
#define nlf() cout << endl

class TimeTracker {
    clock_t start, end;
public:
    TimeTracker() {
        start = clock();
    }
    ~TimeTracker() {
        end = clock();
        fprintf(stderr, "%.3lf s\n", (double)(end - start) / CLOCKS_PER_SEC);
    }
};

inline void swap(int& a,int &b){ a^=b; b^=a; a^=b; }
inline lli min(lli& a,lli &b){ if(a<b) { return a; } else return b; }
inline lli max(lli& a,lli &b){ if(a>b) { return a; } else return b; }

# define getcx getchar
ull fast_inp_ull()//fast input function
{
        ull n=0;
        int ch=getcx();
        while( ch < '0' || ch > '9' )
        {ch=getcx();}
        while( ch >= '0' && ch <= '9' )
        n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
        return n;
}

lli fast_inp_lli()//fast input function
{
        lli n=0;
        int ch=getcx();
        int sign=1;
        while( ch < '0' || ch > '9' )
        {if(ch=='-')sign=-1; ch=getcx();}
        while( ch >= '0' && ch <= '9' )
        n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
        n=n*sign;
        return n;
}

int fast_inp_int()//fast input function
{
        int n=0;
        int ch=getcx();
        int sign=1;
        while( ch < '0' || ch > '9' )
        {if(ch=='-')sign=-1; ch=getcx();}
        while( ch >= '0' && ch <= '9' )
        n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
        n=n*sign;
        return n;
}

void output(lli x)
{
  if(x<0)
    {
      putchar('-');
      x=-x;
    }
  int len=0,data[25];
  while(x)
    {
      data[len++]=x%10;
      x/=10;
    }
  if(!len)
    data[len++]=0;
  while(len--)
    putchar(data[len]+48);
  putchar('\n');
}

#define inp_int fast_inp_int() ;
#define inp_lli fast_inp_lli() ;
#define inp_int fast_inp_int() ;

#ifdef LOCAL
    ofstream fout("out");
#endif

bool check(int k,int m[4][4],int i){
	int j;
	lpu(j,0,4) if(m[i][j]==k) return true;
	return false;
}

int main()
{	
  #ifdef LOCAL
    freopen("in", "r", stdin);
    TimeTracker trk;
  #endif
  
  int t = inp_int;
  int a,b; int i,j;
  int m1[4][4]; int m2[4][4];
  int tp=0;
  std::vector<int> v;

  while(tp<t){
  	v.clear();
    
    a=inp_int; a--;
    lpu(i,0,4) lpu(j,0,4) m1[i][j] = inp_int ;
    b=inp_int; b--;
    lpu(i,0,4) lpu(j,0,4) m2[i][j] = inp_int ;
    
    lpu(j,0,4) if(check(m1[a][j],m2,b)) v.push_back(m1[a][j]);

    if(v.size()==0) fout << "Case #"<< (tp+1) << ": Volunteer cheated!" << endl;
    if(v.size()==1) fout << "Case #"<< (tp+1) << ": " << v[0] << endl;
    if(v.size()>1) fout << "Case #"<< (tp+1) << ": Bad magician!" << endl;

    tp++;	
  }
  return 0;
}
