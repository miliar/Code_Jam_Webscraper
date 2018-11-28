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

string conv(int num,int len)
{
	string n = to_string(num);
	while(n.size()<len) n='0'+n;
	return n;
	
}


bool satisfy(string & s,int num)
{
	string n = conv(num,s.size());
	if(n.size()>s.size()) return false;
	FR(i,s.size())
	{
		if(s[i]!=n[i] && s[i]!='?') return false;
	}
	return true;
}



int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	//ios::sync_with_stdio(0);
	int T;cin>>T;

	FOR(_,1,T+1)
	{
		cout<<"Case #"<<_<<": ";
		string C,J;cin>>C>>J;
		
		int MIN = INT_MAX,MINc = -1,MINj = -1;

		FR(c,1000)
			FR(j,1000)
			{
				if(satisfy(C,c) && satisfy(J,j))
				{
					if(abs(c-j)<MIN)
						MIN=abs(c-j),MINc=c,MINj=j;
					else if(abs(c-j)==MIN)
					{
						if(c < MINc)
							MINc=c,MINj=j;
					}
				}
			}

		cout<<conv(MINc,C.size())<<" "<<conv(MINj,J.size())<<endl;

	}
}