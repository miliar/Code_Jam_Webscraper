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

bool check(int k,int m[4][4],int i){
	int j;
	lpu(j,0,4) if(m[i][j]==k) return true;
	return false;
}

//O(NlogN)
int war(vector<double> naomi,vector<double> ken){
	int z = 0;
	while(naomi.size()>0){
		auto ubi = upper_bound(ken.begin(),ken.end(),naomi[naomi.size()-1]);
		if(ubi==ken.end()){
		 	z++;
		 	naomi.pop_back();
			ken.erase(ken.begin());
		}
		else{
			naomi.pop_back();
			ken.erase(ubi);
		}
	}
	return z;
}

int decwar(vector<double> naomi,vector<double> ken){
	int y = 0;
	while(naomi.size()>0){
		auto ubi = upper_bound(ken.begin(),ken.end(),naomi[naomi.size()-1]);
		if(ubi==ken.end()){
		 	y++;
		 	auto nubi = upper_bound(naomi.begin(),naomi.end(),ken[0]);
		 	naomi.erase(nubi);
			ken.erase(ken.begin());
		}
		else{
			naomi.erase(naomi.begin());
			ken.erase(ubi);
		}
	}
	return y;
}

int war2(vector<double> naomi,vector<double> ken){
	int z = 0;
	while(naomi.size()>0){
		auto ubi = upper_bound(ken.begin(),ken.end(),naomi[0]);
		if(ubi==ken.end()) return naomi.size();
		else{
			naomi.erase(naomi.begin());
			ken.erase(ubi);
		}
	}
	return z;
}

int main()
{	
  #ifdef LOCAL
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    TimeTracker trk;
  #endif
  
  int t = inp_int;
  int n,y,z;
  std::vector<double> naomi;
  std::vector<double> ken;
  double d;

  int i,tp=1;
  while(tp<=t){
  	naomi.clear();
  	ken.clear();

  	n=inp_int;
  	lpu(i,0,n) { cin >> d ; naomi.push_back(d); }
  	lpu(i,0,n) { cin >> d ; ken.push_back(d); }
  	
  	sort(naomi.begin(),naomi.end());
  	sort(ken.begin(),ken.end());

  	//for(double dt : naomi) cout << dt << " "; cout << endl;
  	//for(double dt : ken) cout << dt << " "; cout << endl;

  	y = decwar(naomi,ken);
  	z = war(naomi,ken);

  	cout << "Case #" << tp << ": " << y << " " << z << endl;

  	tp++;
  }

  return 0;
}
