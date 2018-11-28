
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <utility>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <queue>
#include <ctime>
#include <fstream>
#include <sstream>
#include <cmath>
#include <limits>


#define abs(x) ((x)>=0? (x):(-x))
#define gc getchar()
#define s(x) scanf("%d",&x)
#define sil(x) scanf("%llu",&x)
#define sd(x) scanf("%ld",&x)
#define in(s) cin>>s
#define FOR(i,a,b) for( typeof(a) i=(a); i<(b); ++i) // exclusive for
#define FORR(i,a,b) for( typeof(a) i=(a-1) ; i>=(b); --i)
#define REP(k,a,b) for(typeof(a) k=(a); k <= (b); ++k) // inclusive for
#define REPR(i,a,b) for( typeof(a) i=(a) ; i>=(b); --i)
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define SZ(x) ((int)((x).size()))
#define SRT(v) std::sort(ALL(v))
#define CTN(x) std::cout<<x<<'\n' //cout with newline
#define CTS(x) std::cout<<x<<" " //cout with space
#define CT(x) std::cout<<x
#define CLR(x) std::memset(x,0,sizeof(x))
#define FILL(x,n) std::fill_n(x,sizeof(x),n)
#define T(t) int t=read<int>();// while(t--)
#define DBGA(x,n) {for(int i=0;i<n;i++) cout<<x[i]<<" "; cout<<"\n";}
#define REC(x) clock_t x=clock()
#define CPS CLOCKS_PER_SEC
#define TM(x,y) CTN(((double)(y-x)/CPS));


typedef std::vector<int> VI;
typedef std::vector<long long int> VL;
typedef std::vector<unsigned long long int> VULL;
typedef std::vector<std::string> VS;
typedef std::map<int,int> MI;
typedef std::pair<int,int> PII;
typedef std::string str;
typedef unsigned long long ull;
typedef long long ll;
typedef long int li;


using namespace std;


int main()
{
	int t;
	int a[4][4],b[4][4];
	int ans1,ans2,temp	;
	s(t);
	temp = t;
	while(t--)
	{

		s(ans1);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				s(a[i][j]);
			}
		}
		s(ans2);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				s(b[i][j]);
			}
		}
		int count =0,ind;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[ans1-1][i]==b[ans2-1][j])
				{
					count++;
					ind =i;
				}
			}
		}
		if(count==1)
		{
			cout<<"Case #"<<temp -t<<": "<<a[ans1-1][ind]<<endl;
		}
		if(count==0)
		{
			cout<<"Case #"<<temp -t<<": Volunteer cheated!"<<endl;
		}
		if(count>1)
		{
			cout<<"Case #"<<temp -t<<": Bad magician!"<<endl;
		}
	}
}
