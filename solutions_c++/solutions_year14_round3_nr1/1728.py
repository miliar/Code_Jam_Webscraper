#include <cstring>
#include <fstream>
#include <iostream>
#include <vector>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <complex>

using namespace std;

#define sz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define cl(t,v) memset((t),(v),sizeof(t))

#define rep(i,n) for(int i=0,_##i=(n);i<_##i;++i)
#define dwn(i,n) for(int i=(n);--i>=0;)
#define repr(i,l,r) for(int i=(l),_##i=(r);i<_##i;++i)
#define dwnr(i,l,r) for(int i=(r),_##i=(l);--i>=_##i;)
#define repi(i,a) for(__typeof((a).begin()) i=(a).begin(),_##i=(a).end();i!=_##i;++i)
#define dwni(i,a) for(__typeof((a).rbegin()) i=(a).rbegin(),_##i=(a).rend();i!=_##i;++i)

class FileReader : public ifstream {
public:
	FileReader( const string& filename ) { open( filename.c_str(), ios_base::in ); }
	int readInt() { int x = 0; *this >> x; return x; }
	vector<int> readInts( int n ) { vector<int> v(n); for ( int i = 0; i < n; i++ ) v[i] = readInt(); return v; }
	string readLine() { char buf[20000]; getline( buf, sizeof(buf) ); return buf; }
	string readString() { string x; *this >> x; return x; }
	vector<string> readStrings( int n ) { vector<string> v; for ( int i = 0; i < n; i++ ) v.push_back( readString() ); return v; }
	__int64 readInt64() { __int64 x; *this >> x; return x; }
};

class FileWriter : public ofstream {
public:
	FileWriter( const string& filename ) { open( filename.c_str(), ios_base::out ); }
};

long long Gcd(long long a, long long b)
{
    if(b == 0)
        return a;
    return Gcd(b, a % b);
}

int main() {
	FileReader fin ("A-small-attempt0.in");
	FileWriter fout ("out.txt");

	int caseCount;
	long long n2[41];
	n2[0]=1;
	repr(i,1,41)n2[i]=n2[i-1]*2;
	fin >> caseCount;
	fin.readLine();
	rep(cc,caseCount) {
		/*input*/
		long long a,b;
		int flag;
		long ans;
		char t;
		fin>>a>>t>>b;
		long c=Gcd(b,a);
		a=a/c;
		b=b/c;
		/*solve*/
		flag=1;
		rep(i,41)if(n2[i]==b){flag=0;break;}
		if(a>b)flag=1;
		if(flag==0){
            long long x=b/a;
            if(b%a>0)x++;
cout<<a<<','<<b<<endl;
            cout<<x<<endl;
            rep(i,41)if(n2[i]>=x){ans=i;break;}
		}
		/*output*/
		stringstream ss;
		ss << "Case #" << cc + 1 << ": ";
		if(flag==1)ss<<"impossible"<<endl;
		else ss<<ans<<endl;
		fout << ss.str().c_str();
		cout << ss.str().c_str();
	}
	return 0;
}
