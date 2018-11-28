#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
using namespace std;
#define SZ(a) (int((a).size()))
#define FOR(i,n) for(int _n=(n),i=0;i<_n;++i)
#define FORI(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FORSZ(i,c) FOR(i,SZ(c))
#define SET(t,x) memset((t),(x),sizeof(t))
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define PRINT(x) cout<<#x<<"="<<x<<"\n"
#define PRINTI(x,n) for(__typeof(n)i=0;i<(n);++i)cout<<(x)[i]<<" ";cout<<"\n"
#define PRINTIJ(x,n1,n2) for(__typeof(n1)i=0;i<(n1);++i,cout<<"\n")for(__typeof(n2)j=0;j<(n2);++j)cout<<(x)[i][j]<<" ";cout<<"\n"
#define ALL(c) c.begin(), c.end()
#define RALL(c) c.rbegin(),c.rend()
#define PRESENT(c,x) ((c).find(x) != (c).end())
#define CPRESENT(c,x) (find(ALL(c),x) != (c).end())
#define ABS(a) ( (a) >= 0 ? (a) : (-(a)))
#define PB push_back
#define MP make_pair
#define EPS 1e-11
#define EPS2 1e-9
#define D_EQ(a,b) ((a)>((b)-EPS) && (a)<((b)+EPS))
#define D_LT(a,b) ((a)<((b)-EPS))
#define D_LTEQ(a,b) ((a)<((b)+EPS))
#define D_GT(a,b) ((a)>((b)+EPS))
#define D_GTEQ(a,b) ((a)>((b)-EPS))
#define INF 100000000
typedef long long ll;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;

template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); }
template<class T>vector<T> split(const string& s){vector<T> v;istringstream is(s);T t;while(is>>t)v.PB(t);return v;}
//VS splitStr(const string& s, char delim='\0', bool keepEmpty=false){if(delim=='\0')return split<string>(s);VS v;istringstream is(s);string t;while(getline(is,t,delim))if(keepEmpty || t!="")v.PB(t);return v;}
VS splitStr(const string& s,const string& d="",bool keepEmpty=false){if(d.empty())return split<string>(s);VS v;string t;FOR(i,SZ(s))if(d.find(s[i])!=string::npos){if(keepEmpty||!t.empty()){v.PB(t);t="";}}else t+=s[i];if(!t.empty())v.PB(t);return v;}

enum Symbol
{
	One,
	I,
	J,
	K,
	MinusOne,
	MinusI,
	MinusJ,
	MinusK
};

string DisplayValue[8] = {
	"One",
	"I",
	"J",
	"K",
	"MinusOne",
	"MinusI",
	"MinusJ",
	"MinusK"
};

Symbol Negative[8] = {
	MinusOne,
	MinusI,
	MinusJ,
	MinusK,
	One,
	I,
	J,
	K
};
Symbol _Product[4][4] =
{
	{One, I, J, K},
	{I, MinusOne, K, MinusJ},
	{J, MinusK, MinusOne, I},
	{K, J, MinusI, MinusOne}
};

Symbol Product[8][8];
Symbol CharValue[256];

void Setup()
{
	FOR(i,4)FOR(j,4)Product[i][j]=_Product[i][j];
	FOR(i,4)FORI(j, 4, 7) Product[i][j] = Negative[Product[i][j-4]];
	FORI(i, 4, 7)FORI(j, 0, 7) Product[i][j] = Negative[Product[i-4][j]];

	CharValue['i'] = I;
	CharValue['j'] = J;
	CharValue['k'] = K;
}

Symbol SymbolPow(Symbol x, ll power)
{
	int p = power % 4;  // Any symbol to the power 4 becomes 1. so we only need to calculate the remainder.
	Symbol ret = One;
	FOR(i, p)
	{
		ret = Product[ret][x];
	}
	return ret;
}

Symbol StringValue(const string& s, int start, int end)
{
	Symbol ret = One;
	FORI(i, start, end)
	{
		ret = Product[ret][CharValue[s[i]]];
	}
	return ret;
}

// Returns repetition number, and string index.
pair<int,int> IndexOf(const string& s, int start, ll ExtraRepetions, Symbol needle)
{
	int N = SZ(s);
	// The assumption is that we should be able to find i, j, k in 10 repetitons max. In fact we should find it in 3 or 4. 4 repetitons always evaluates to 1.
	int allowedRepetitions = (ExtraRepetions <= 10LL ? ExtraRepetions : 10LL);
	int end = N*(allowedRepetitions+1) - 1;
	//cout <<"IndexOf called with: start="<<start<<" ExtraRepetions="<<ExtraRepetions<<" end="<<end<<endl;
	Symbol currentVal = One;
	FORI(i, start, end)
	{
		currentVal = Product[currentVal][CharValue[s[i%N]]];
		if (currentVal == needle)
		{
			int repetitionNum = i/N;
			int index = i%N;
			return MP(repetitionNum, index);
		}
	}
	
	return MP(-1, -1);
}

void PrintNo(int caseNumber)
{
	cout << "Case #" << caseNumber << ": NO" << endl;
}
void PrintYes(int caseNumber)
{
	cout << "Case #" << caseNumber << ": YES" << endl;
}

int main()
{
	Setup();
	// PRINTIJ(Product, 8, 8);
	int T;
	cin >> T;
	FORI(caseNumber, 1, T)
	{
		int L; ll X;
		cin >> L >> X;
		string s;
		cin >> s;
		//cout << "L="<<L<<" X="<<X<<" s="<<s<<endl;
		int N = SZ(s);
		Symbol inputVal = StringValue(s, 0, N - 1);
		//cout << "inputVal=" << DisplayValue[inputVal] << endl;
		// PopulateValueFromStart(inputS);
		// PopulateValueFromEnd(inputS);

		// Let's look for i.
		int start = 0;
		ll repetitionLeft = X - 1;
		pair<int, int> iIndex = IndexOf(s, start, repetitionLeft, I);
		//cout << "iIndex: (" << iIndex.first << ", " << iIndex.second << ")" << endl;
		if (iIndex.first == -1)
		{
			PrintNo(caseNumber);
			continue;
		}
	
		start = iIndex.second + 1;
		repetitionLeft -= iIndex.first;
		if (start == N)
		{
			start = 0;
			--repetitionLeft;
			if (repetitionLeft < 0)
			{
				PrintNo(caseNumber);
				continue;
			}
		}

		pair<int, int> jIndex = IndexOf(s, start, repetitionLeft, J);
		//cout << "jIndex: (" << jIndex.first << ", " << jIndex.second << ")" << endl;
		if (jIndex.first == -1)
		{
			PrintNo(caseNumber);
			continue;
		}
	
		start = jIndex.second + 1;
		repetitionLeft -= jIndex.first;
		if (start == N)
		{
			start = 0;
			--repetitionLeft;
			if (repetitionLeft < 0)
			{
				PrintNo(caseNumber);
				continue;
			}
		}
		
		pair<int, int> kIndex = IndexOf(s, start, repetitionLeft, K);
		//cout << "kIndex: (" << kIndex.first << ", " << kIndex.second << ")" << endl;
		if (kIndex.first == -1)
		{
			PrintNo(caseNumber);
			continue;
		}
		
		start = kIndex.second + 1;
		repetitionLeft -= kIndex.first;
		Symbol restOfStringValue = One;
		if (start < N)
		{
			restOfStringValue = Product[restOfStringValue][StringValue(s, start, N - 1)];
		}
		if (repetitionLeft > 0)
		{
			restOfStringValue = Product[restOfStringValue][SymbolPow(inputVal, repetitionLeft)];
		}
		
		if (restOfStringValue != One)
		{
			PrintNo(caseNumber);
			continue;
		}
		PrintYes(caseNumber);
	}
    return 0;
}
