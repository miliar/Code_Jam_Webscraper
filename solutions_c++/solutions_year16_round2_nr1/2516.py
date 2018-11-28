
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

/*******  All Required define Pre-Processors and typedef Constants *******/
#define SCD(t) scanf("%d",&t)
#define SCLD(t) scanf("%ld",&t)
#define SCLLD(t) scanf("%lld",&t)
#define SCC(t) scanf("%c",&t)
#define SCS(t) scanf("%s",t)
#define SCF(t) scanf("%f",&t)
#define SCLF(t) scanf("%lf",&t)
#define MEM(a, b) memset(a, (b), sizeof(a))
#define FOR(i, j, k, in) for (int i=j ; i<k ; i+=in)
#define RFOR(i, j, k, in) for (int i=j ; i>=k ; i-=in)
#define REP(i, j) FOR(i, 0, j, 1)
#define RREP(i, j) RFOR(i, j, 0, 1)
#define all(cont) cont.begin(), cont.end()
#define rall(cont) cont.end(), cont.begin()
#define FOREACH(it, l) for (auto it = l.begin(); it != l.end(); it++)
#define IN(A, B, C) assert( B <= A && A <= C)
#define MP make_pair
#define PB push_back
#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007
#define read(type) readInt<type>()
const double pi=acos(-1.0);
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<PII> VII;
typedef vector<VI> VVI;
typedef map<int,int> MPII;
typedef set<int> SETI;
typedef multiset<int> MSETI;
typedef long int int32;
typedef unsigned long int uint32;
typedef long long int int64;
typedef unsigned long long int  uint64;

/****** Template of some basic operations *****/
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }
/**********************************************/

/****** Template of Fast I/O Methods *********/
template <typename T> inline void write(T x)
{
	int i = 20;
	char buf[21];
	// buf[10] = 0;
	buf[20] = '\n';

	do
	{
		buf[--i] = x % 10 + '0';
		x/= 10;
	}while(x);
	do
	{
		putchar(buf[i]);
	} while (buf[i++] != '\n');
}

template <typename T> inline T readInt()
{
	T n=0,s=1;
	char p=getchar();
	if(p=='-')
		s=-1;
	while((p<'0'||p>'9')&&p!=EOF&&p!='-')
		p=getchar();
	if(p=='-')
		s=-1,p=getchar();
	while(p>='0'&&p<='9') {
		n = (n<< 3) + (n<< 1) + (p - '0');
		p=getchar();
	}

	return n*s;
}
/************************************/


/******** User-defined Function *******/

	// write here your code

/**************************************/

/********** Main()  function *******/
int main()
{

	#ifndef GOOGLE_CODE_JAM
	    freopen("input.txt","r",stdin);
	    freopen("output.txt","w",stdout);
	#endif
    int t;
    t = read(int);
    string s;
    int l,j,x;
    REP(k,t){
    	// write here your code


    	cin>>s;
        l=s.length();
        int a[26]={0};


        for(j=0;j<l;j++)
        {
            a[s[j]-'A']++;
           // cout<<s[j]<<endl;
        }

        int d[10]={0};

        d[0]=a['Z'- 'A'];
        a['Z' - 'A']-=d[0];
        a['E' - 'A']-=d[0];
        a['R' - 'A']-=d[0];
        a['O' - 'A']-=d[0];

        d[2]=a['W'- 'A'];
        a['W' - 'A']-=d[2];
        a['T' - 'A']-=d[2];
        a['O' - 'A']-=d[2];

        d[4]=a['U'- 'A'];
        a['U' - 'A']-=d[4];
        a['F' - 'A']-=d[4];
        a['R' - 'A']-=d[4];
        a['O' - 'A']-=d[4];


        d[6]=a['X'- 'A'];
        a['X' - 'A']-=d[6];
        a['S' - 'A']-=d[6];
        a['I' - 'A']-=d[6];

        d[3]=a['R'- 'A'];
         a['R' - 'A']-=d[3];
        a['T' - 'A']-=d[3];
        a['H' - 'A']-=d[3];
        a['E' - 'A']-=(2*d[3]);


        d[1]=a['O'- 'A'];
        a['O' - 'A']-=d[1];
        a['E' - 'A']-=d[1];
        a['N' - 'A']-=d[1];


        d[5]=a['F'- 'A'];
        a['F' - 'A']-=d[5];
        a['E' - 'A']-=d[5];
        a['V' - 'A']-=d[5];
        a['I' - 'A']-=d[5];


        d[7]=a['S'- 'A'];
        a['S' - 'A']-=d[7];
        a['E' - 'A']-=(2 * d[7]);
        a['V' - 'A']-=d[7];
        a['N' - 'A']-=d[7];


        d[8]=a['T'- 'A'];
        a['E' - 'A']-=d[8];
        a['I' - 'A']-=d[8];
        a['G' - 'A']-=d[8];
        a['H' - 'A']-=d[8];

        d[9]=(a['N'- 'A']/2);

        printf("Case #%d: ",k+1);


        for(j=0;j<=9;j++)
        {
            for(x=0;x<d[j];x++)
            {
                printf("%d",j);
            }
        }

        printf("\n");


    }
	return 0;
}
/********  Main() Ends Here *************/
