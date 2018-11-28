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

using namespace std;

multiset<int,greater<int> > S;
int A[100*100+100];
int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	int T;cin>>T;
	FOR(_,1,T+1)
	{
		S.clear();
		int n,x;cin>>n>>x;
		FR(i,n)
			cin>>A[i];
		sort(A,A+n,descending);
		int ret = 0;
		FR(i,n)
		{
			multiset<int>::iterator it = S.lower_bound(x-A[i]);
			if(it==S.end())
				S.insert(A[i]);
			else
				S.erase(it),ret++;
		}
		cout<<"Case #"<<_<<": ";
		cout<<ret+S.size()<<endl;
	}
}