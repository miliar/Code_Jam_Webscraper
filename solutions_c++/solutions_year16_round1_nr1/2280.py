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



int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	//ios::sync_with_stdio(0);
	int T;cin>>T;
	FOR(_,1,T+1)
	{
		cout<<"Case #"<<_<<": ";
		string s;cin>>s;
		
		vector<pair<char,int> > V;
		for(int i = s.size()-1;i >= 0;i--)
			V.push_back(make_pair(s[i],i));

		sort(V.begin(),V.end());
		reverse(V.begin(),V.end());

		set<int> res;
		string t = "";
		int curind = s.size();
		FR(i,V.size())
		{
			if(V[i].second<curind)
			{
				curind = V[i].second;
				t += V[i].first;
				res.insert(V[i].second);
			}
		}
		FR(i,s.size())
		{
			if(res.find(i)==res.end()) t+=s[i];
		}
		if(t<s) t=s;
		cout<<t<<endl;
		
	}
}