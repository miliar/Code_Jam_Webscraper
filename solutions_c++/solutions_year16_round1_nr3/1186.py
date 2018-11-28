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
#include <cassert>


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
#define PBI pair<bool,int>


using namespace std;


int A[11];

int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	//ios::sync_with_stdio(0);
	int T;cin>>T;
	FOR(_,1,T+1)
	{
		cout<<"Case #"<<_<<": ";
		int n;cin>>n;
		FR(i,n){
			cin>>A[i];
			A[i]--;
		}

		int P[11];
		FR(i,n) P[i]=i;
		int MAX = 1;
		do{
			for (int cnt = 2;cnt <= n;cnt++)
			{
				bool flag = true;
				FR(i,cnt)
				{
					if(P[(i-1+cnt)%cnt] == A[P[i]] || P[(i+1)%cnt] == A[P[i]])
						;
					else flag = false;
				}
				if(flag) MAX = max(MAX,cnt);
			}
		}while(next_permutation(P,P+n));
		cout<<MAX<<endl;
	}
}