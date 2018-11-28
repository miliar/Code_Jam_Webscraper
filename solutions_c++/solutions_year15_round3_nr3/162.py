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


ll A[110];
ll B[30];

bool is[110];
bool coin[110];

int main()
{
	ios::sync_with_stdio(0);
	ifstream cin("a.in");
	ofstream cout("a.out");
	int T;cin>>T;
	FOR(_,1,T+1)
	{
		cout<<"Case #"<<_<<": ";
		ll C,D,V;
		cin>>C>>D>>V;		
		FR(i,D){
			cin>>A[i];
		}

		
		ll sum = 0;

		ll ind = 0;
		ll ans = 0;
		while(sum < V)
		{
			if(ind < D && A[ind] <= sum+1){
				sum+=A[ind]*C;
				ind++;
			}
			else{
				sum += (sum+1)*C;
				ans ++;
			}
		}
		cout<<ans<<endl;

	}
}