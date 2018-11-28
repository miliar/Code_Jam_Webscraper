#pragma comment(linker,"/STACK:268435456")
#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>
#include <sstream>
#include <bitset>
#include <iterator>
#include <list>
#include <ctime>
#include <functional>
#include <numeric>


#define FR(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,c,n) for(int (i)=(c);(i)<(n);(i)++)
#define REP(it,v,cont) for((cont)::iterator (it)=(v).begin();(it)!=(v).end();++(it))
#define CLR(a,c) memset((a),(c),sizeof (a))
#define ALL(v) (v).begin(),(v).end()
#define VCPRINT(v) for(int iii = 0;iii < (v).size();iii++) cout<<(v)[iii]<<" ";cout<<endl;
#define SETPRINT(v,cont) for((cont)::iterator iiit = (v).begin();iiit != (v).end();iiit++) cout<<*iiit<<" ";cout<<endl;

bool ascending (int i,int j) { return (i<j); }
bool descending (int i,int j) { return (i>j); }

typedef long long ll;
typedef unsigned long long ull;
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PULI pair<unsigned long long,int>
#define PIL pair<int,long long>
#define PSI pair<string,int>
#define PSS pair<string,string>
#define PDD pair<double,double>
#define PIB pair<int,bool>
typedef long double ld;
#define PLI pair<ll,int>
using namespace std;


int _count(string & s,string & f)
{
	int occurrences = 0;
	string::size_type start = 0;

	while ((start = s.find(f, start)) != string::npos) {
		++occurrences;
		start += 1;
	}
	return occurrences;
}


int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	int T;cin>>T;
	FOR(_,1,T+1)
	{
		cout<<"Case #"<<_<<": ";
		int K,L,S;
		cin>>K>>L>>S;
		string k,l;cin>>k>>l;
		long double ans = 0.0;
		int mx = 0;
		for(int mask = 0; mask < pow(K,S);mask++)
		{
			int num = mask;
			string t;
			FR(__,S)
			{
				t+=k[num%K];
				num/=K;
			}
			int a = _count(t,l);
			ans += a;
			mx = max(mx,a);
		}
		ans = (pow(K,S)*mx-ans)/pow(K,S);
		cout<<setprecision(8)<<fixed<<ans<<endl;
	}
}