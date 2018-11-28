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


int fun(string a,string b){
	return a.length()>b.length();
}
int optCost(int ar[],int n)
{
	vector<int> best(101);
	for(int i=0;i<101;i++)
		best[i]=0;
	for(int i=0;i<n;i++)
		for(int j=1;j<101;j++)
			best[j]+= abs(ar[i]-j);
	
	sort(all(best));
	return best[1];
}

int main(int argc,char *argv[])
{
ifstream fin(argv[1]);
ofstream fout("output.txt");
	int t;
	fin>>t;
	for(int i=1;i<=t;i++){
		fout<<"Case #"<<i<<": ";
			int n;
			fin>>n;
			vector<string> str(n);
			for(int i=0;i<n;i++)
				fin>>str[i];
			int cur[101];
			for(int i=0;i<101;i++)
				cur[i]=0;
			int impossible=0;
			int totalCost=0;
			sort(all(str),fun);
			while(cur[0]<str[0].length()){
				char curChar=str[0][cur[0]];
				int cunt[n];
				for(int i=0;i<n;i++){
					cunt[i]=0;
					while(str[i].length()>cur[i] && str[i][cur[i]]==curChar){
						cunt[i]++;
						cur[i]++;
					}
					if(cunt[i]==0){
						impossible=1;
						break;
					}
				}
				if(impossible)break;
				totalCost+= optCost(cunt,n);
			}
			
			if(impossible)
				fout<<"Fegla Won"<<endl;
			else 
				fout<<totalCost<<endl;
	}
fin.close();
fout.close();
return 0;
}


