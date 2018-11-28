// Template v2
#define pb push_back
#define mp make_pair
#define first x
#define second y
#define l(x) x<<1
#define r(x) x<<1 | 1
#define lsb(x) x & -x
#include<bits/stdc++.h>
#include <bitset>
using namespace std;
 
typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef pair<double, double> PKK;
// primes less than 100
const int PRIM[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
const int CMAX = 10005;
const int MOD = 700001;
const int CIUR = 100000000;
const int NMAX = 10666;
const short INF16 = 32000;
const int INF = 2*1e9 + 6661369;
const LL INF64 = LL(1e18);
const LD EPS = 1e-9, PI = acos(-1.0);

ifstream fin("jam.in");
ofstream fout("jam.out");
string s;
int n,t;
void read()
{
	fin>>t;
	for(int tt=1; tt<=t; ++tt){
		fout<<"Case #"<<tt<<": ";
		fin>>s;
		n=1;
		for(int i=1; i<s.size(); ++i)
			if(s[i] != s[i-1])
				n++;
		if(s[s.size()-1]=='+')
			n--;
		fout<<n<<"\n";
	}	
    
}
 
int main(){
	cin.sync_with_stdio(false);
    read();
    return 0;
}