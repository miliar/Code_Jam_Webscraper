#include<iostream>	//------------------------------------------------------------//
#include<cstdio>    //  ___  ___ _____ ______                                     //
#include<algorithm> //  |  \/  |/  ___|| ___ \     This C++ Template Belongs to   //
#include<cmath>     //  | .  . |\ `--. | |_/ /        Manish Singh Bisht          //
#include<vector>    //  | |\/| | `--. \| ___ \       http://fb.me/manish05        //
#include<set>       //  | |  | |/\__/ /| |_/ /    Email: manish05@facebook.com    //
#include<map>       //  \_|  |_/\____/ \____/                                     //
#include<functional>//------------------------------------------------------------//
#include<string>
#include<cstring>
#include<bitset>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>

#include<stack>
#include<cstdio>
#include<ctime>
         

using namespace std;
#define gc getchar_unlocked
#define MEM(a,b) memset(a,(b),sizeof(a))
#define FOR(i,n) for(int i=(0);i<(n);i++)
#define TR(v,it) for(typeof(v.begin()) it(v.begin()) ; it != v.end() ; it++)
#define SZ(v) (int)sizeof(v)
#define CLEAR(a) memset((a),0,sizeof(a))
#define S(n) scanf("%d", &n)
#define P(k) printf("%d\n", k)
#define pb push_back
#define mp make_pair
#define ll long long
#define VI vector<int>
#define PII pair<int, int>
#define ft first
#define sd second
#define all(a) a.begin(),a.end()
#define lb lower_bound
#define ub upper_bound
#define inf (1<<30)
#define PNL printf("\n")
#define md 1000000007
#define bigger(a,b) (a>b?a:b)
#define smaller(a,b) (a<b?a:b)
#define positive(a) (bigger(a,-a))
ll modPow(ll a,ll b)
{ll x;
    for(x=1;b>0;b/=2,a=(a*a)%md)
        if(b%2==1)
                x=(x*a)%md;
  return x%md;
}

string convertInt(int number){stringstream ss;ss << number;return ss.str();}
int convertString(string s){int num;stringstream sstr(s);sstr>>num;return num;}
int gcd(int a, int b){ return b?gcd(b,a%b):a; }

unsigned int hash(const char* s,unsigned int seed = 0)
{
	unsigned hash = seed;while(*s)
    {
        hash = hash * 101  +  *s++;
    }
    return hash;
}


int main(int argc,char *argv[])
{
ifstream fin(argv[1]);
ofstream fout("output.txt");
	int t;
	fin>>t;
	for(int i=1;i<=t;i++){
		fout<<"Case #"<<i<<": ";
				int a,b,k;
				fin>>a>>b>>k;
				int ways=0;
				for(int i=0;i<a;i++)
					for(int j=0;j<b;j++)
						if( (i&j) <k)ways++;
				
		fout<<ways<<endl;
	}
fin.close();
fout.close();
return 0;
}


