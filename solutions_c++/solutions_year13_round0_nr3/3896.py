/*
ID: rohamhe1
PROB: proximity
LANG: C++
*/
#include<iostream>
#include<cstring>
#include<iomanip>	
#include<vector>
#include<map>
#include<cmath>
#include<algorithm>
#include<fstream>
#include<set>
#include<complex>
#include<queue>
#include<utility>

using namespace std;

//typedef complex<long double> point;
#define pb push_back
#define mk make_pair
#define x first
#define y second
#define error(x) cout << #x << " : " << (x) << endl;
typedef long long LL;
typedef long double LD;
//#define cin fin
//#define cout fout

LL n , m , k;
const int maxn = 110;

bool pal(int a)
{
	int q = 0;
	int p = a;
	while(p)
	{
		q*=10;
		q+=p%10;
		p/=10;
	}
	if(q == a)
		return true;
	else
		return false;
}

int main()
{
	int T = 1;
	int t;
	cin >> t;
	while(t--)
	{
		int  a, b;
		cin >> a >> b;
		int ans = 0;
		for(int i=sqrt(a) ; i<=sqrt(b) ; i++)
		{
			if(pal(i) == false)
				continue;
			int q = i*i;
			if(q < a || q > b)
				continue;
			if(pal(q) == true)
			{
				//error(i);
				ans++;
			}
		}
		cout << "Case #"  << T << ": " << ans << endl;
		T++;
	}
}
