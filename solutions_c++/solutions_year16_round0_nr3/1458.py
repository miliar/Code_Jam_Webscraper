#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <complex>
#include <iterator>
#include <set>
#include <bitset>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <fstream>
#include <ctime>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
typedef vector<VI> VVI;
typedef vector<LL> VLL;
typedef vector<double> VD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define PF push_front

ofstream jamali;
int n;
LL a,b,c,k;
__int128 tab[11];
int maska[17];
int kejs=1;
int main()
{
	n=32;
	jamali.open("jam_coins.txt");
	maska[0]=1;
	maska[n-1]=1;
	int rbit=n-2;
	int lbit=1;
	for(LL i=0; i<(1LL<<(n-2)); i++)
	{
		cerr<<"#i"<<i<<endl;
		LL nr=i;
		FOR(p,1,14)
		{
			maska[p]=nr%2;
			nr/=2;
		}
		LL base;
		//LL num=1;
		__int128 pot=1;
		FOR(p,2,10)
		{
			tab[p]=0;
			
			base=p;
			pot=1;
			FOR(z,0,n-1)
			{
				tab[p]+=pot*maska[z];
				pot*=base;
			}
		}
		VI ans;
		ans.clear();
		bool jest=false;
		//cerr<<"szukanie dzielnika"<<endl;
	//	clock_t begin = clock();

  //code_to_time();

  
  //double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
		FOR(p,2,10)
		{
			jest=false;
			LL lim;
			/*
			if(tab[p]>100000000000000000LL)
			{
				lim=((LL)((1e16)))+10;
			}
			else
			{
				lim=sqrt(LL(tab[p]));
			}
			*/
			lim=(1000006); //1e6
			for(LL z=2; z<lim; z++)
			{
				
				if(tab[p]%z==0)
				{
					ans.PB(z);
					jest=true;
					break;
				}
			}
			if(!jest)
			break;
		}
		if(jest)
		{
			//jamali<<"Case #"<<kejs<<": ";
			cerr<<"jest juz:"<<kejs++<<endl;
			FORD(p,n-1,0) // fml
			{
				jamali<<maska[p];
			}
			jamali<<" ";
			REP(p,9)
			{
				jamali<<ans[p]<<" ";
			}
			jamali<<endl;
			//
			/*
			FOR(p,2,10)
			{
				jamali<<"#"<<((LL)(tab[p]))<<" ";
			}
			jamali<<endl;
			*/
			
		}
	}
	cerr<<"koniec"<<endl;
}






