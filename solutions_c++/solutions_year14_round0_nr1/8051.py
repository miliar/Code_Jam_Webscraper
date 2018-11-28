/*************** Author: sambit1993 ******************/
/* 	Category: UpdateLater          */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <utility>
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
#include <climits>
#include <bitset>
#include <iomanip>
#include <stack>

#ifndef ONLINE_JUDGE
	#define gc getchar
#else
	#define gc getchar_unlocked
#endif

#define s(x) scanf("%d",&x)
#define sil(x) scanf("%llu",&x)
#define sd(x) scanf("%ld",&x)

#define ri(x) x=read<int>()
#define rl(x) x=read<ll>()
#define ru(x) x=read<ull>() 

#define FOR(i,a,b) for( int i=(a); i<(b); ++i)               // exclusive for
#define FORR(i,a,b) for( int  i=(a-1) ; i>=(b); --i)
#define REP(k,a,b) for(int  k=(a); k <= (b); ++k)			// inclusive for
#define REPR(i,a,b) for( int i=(a) ; i>=(b); --i)
#define ALL(c) (c).begin(), (c).end()  
#define PB push_back 
#define MP make_pair 
#define SZ(x) ((int)((x).size()))
#define SRT(v) std::sort(ALL(v))
#define CTN(x) std::cout<<x<<'\n'								//cout with newline
#define CTS(x) std::cout<<x<<" "                                //cout with space
#define CLR(x) std::memset(x,0,sizeof(x))
#define FILL(x,n) std::fill_n(x,sizeof(x),n)
#define T(t) int t; ri(t); while(t--) 
#define DBGA(x,n) {for(int i=0;i<n;i++) cerr<<x[i]<<" "; cerr<<"\n";}
#define REC(x) clock_t x=clock()
#define CPS CLOCKS_PER_SEC 
#define TM(x,y) CTN(((double)(y-x)/CPS))
#define abs(x) ((x)>0?(x):(-(x)))


typedef std::vector<int> VI;
typedef std::vector<long long int> VL;
typedef std::vector<std::string> VS;

typedef std::pair<int,int> PII;
typedef unsigned long long ull;
typedef long long ll;

template <typename T>
inline T read()
{
	register T x=0;
	register char c;
	while((c=gc())<48 || c>'9');
	x=c-'0';
	while((c=gc())>='0' && c<='9')
		x=(x<<3)+(x<<1)+c-'0';
	return x;
}
using namespace std;
/**************************GLOBAL DATA***************************************/
/**************************GLOBAL DATA***************************************/
int main()
{
	//std::ios_base::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
		freopen("in.txt","r",stdin);
	#endif
	int t;cin>>t;

	int cn=1;
	while(t--)
	{
		int r1,r2;cin>>r1;
		VI ini;
		REP(i,1,4)
			REP(j,1,4){
				int num;cin>>num;
				if(i==r1)
					ini.PB(num);

			}
		//DBGA(ini,4);
		cin>>r2;
		int count=0,ans=-1;
		REP(i,1,4)
			REP(j,1,4){
				int num;cin>>num;
				if(i==r2)
				{
					FOR(k,0,SZ(ini))
						{
							if(ini[k]==num) ans=num;
							count+=(int)(ini[k]==num);
						}
				}	
			}

		if(count==0)
			cout<<"Case #"<<cn<<": Volunteer cheated!"<<endl;
		else if(count==1)
			cout<<"Case #"<<cn<<": "<<ans<<endl;
		else 
			cout<<"Case #"<<cn<<": Bad magician!"<<endl;

	cn+=1;
	}
}