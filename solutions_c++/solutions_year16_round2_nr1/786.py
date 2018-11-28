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

string num[] = {
	"SIX",
	"TWO",
	"ZERO",
	"EIGHT",
	"FOUR",
	"FIVE",
	"THREE",
	"ONE",
	"SEVEN",
	"NINE"
};

int nums[] = { 6,2,0,8,4,5,3,1,7,9
};



int hist[30];


int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	//ios::sync_with_stdio(0);
	int T;cin>>T;

	map<char,int> chist[10];
	map<char,int>::iterator it;
	FR(i,10) FR(j,num[i].size()) chist[i][num[i][j]]++;


	FOR(_,1,T+1)
	{
		cout<<"Case #"<<_<<": ";
		string s;cin>>s;
		CLR(hist,0);
		FR(i,s.size()) hist[s[i]-'A']++;
		string ret = "";
		FR(i,10)
		{
			bool flag = true;
			while(flag){
				for(it = chist[i].begin();it != chist[i].end();it++)
				{
					flag = flag && hist[it->first-'A']>=it->second;
				}
				if(flag)
				{
					for(it = chist[i].begin();it != chist[i].end();it++)
						hist[it->first-'A']-=it->second;
					ret += '0'+nums[i];
				}
			}
		}
		FR(i,30) assert(hist[i]==0);
		sort(ret.begin(),ret.end());
		cout<<ret<<endl;


	}
}