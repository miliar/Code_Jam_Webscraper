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
#define PIC pair<int,char>


using namespace std;


PIC P[10*1000+100];

int sgn[4][4] = {
	{1,1,1,1},
	{1,-1,1,-1},
	{1,-1,-1,1},
	{1,1,-1,-1}
};

char ans[4][4] = {
	{'\0','i','j','k'},
	{'i','\0','k','j'},
	{'j','k','\0','i'},
	{'k','j','i','\0'},
};

int divsgn[4][4] = {
	{1,-1,-1,-1},
	{1,1,1,-1},
	{1,-1,1,1},
	{1,1,-1,1}
};

char divans[4][4] = {
	{'\0','i','j','k'},
	{'i','\0','k','j'},
	{'j','k','\0','i'},
	{'k','j','i','\0'},
};




int ch(char c)
{
	return c=='\0'?0:(int)(c-'i'+1);
}

PIC operator*(const PIC & p1,const PIC & p2)
{
	return PIC(p1.first*p2.first*sgn[ch(p1.second)][ch(p2.second)],ans[ch(p1.second)][ch(p2.second)]);
}

PIC operator/(const PIC & p1,const PIC & p2)
{
	return PIC(p1.first*p2.first*divsgn[ch(p1.second)][ch(p2.second)],divans[ch(p1.second)][ch(p2.second)]);
}


int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	int T;cin>>T;
	FOR(_,1,T+1)
	{
		cout<<"Case #"<<_<<": ";
		int x,r,c;cin>>x>>r>>c;
		if(r<c) swap(r,c);
		if(x>r) cout<<"RICHARD"<<endl;
		else if(r*c % x != 0) cout<<"RICHARD"<<endl;
		else if(x==3 && r==3 && c==1) cout<<"RICHARD"<<endl;
		else if(x==4 && r==4 && c==1) cout<<"RICHARD"<<endl;
		else if(x==4 && r==4 && c==2) cout<<"RICHARD"<<endl;
		//else if(x==4 && r==4 && c==3) cout<<"RICHARD"<<endl;
		//else if(x==4 && r==4 && c==4) cout<<"RICHARD"<<endl;
		else cout<<"GABRIEL"<<endl;
	}
}