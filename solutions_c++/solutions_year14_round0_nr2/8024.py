//-------------include
#include<cstdio>
#include<string>
#include<iostream>
#include<cstring>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<climits>
#include<vector>
#include<list>
#include<deque>
#include<functional>
#include<sstream>

//-------------define
#define ALL(a)  (a).begin(),(a).end()
#define PB push_back
#define MP make_pair
#define SORT(c) sort((c).begin(),(c).end())
#define DUMP(x)  cerr << #x << " = " << (x) << endl;
#define CLR(a) memset((a), 0 ,sizeof(a))
#define rep(i,n) for(int i=0;i<(int)n;i++)
#define fi first
#define se second

//-------------namespace
using namespace std;

//-------------inline
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//-------------typedef
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;

//-------------var
int dx[]={0,-1,0,1,1,1,-1,-1},dy[]={1,0,-1,0,1,-1,1,-1};

double mint(double a,double b)
{
	double ret;
	ret = a/b;
	return ret;
}

int main()
{
	int t;
	cin >> t;

	for(int cn=0;cn<t;cn++){
		double c,f,x;
		cin >> c >> f >> x;

		double ups=2.0;
		double mt=mint(c,ups);
		double ans=mint(x,ups);
		for(int i=1;i<=(int)ceil(x);i++){
			ups+=f;
			double _mt=mt+mint(c,ups);
			double _ans=mt+mint(x,ups);
			if(ans>_ans){
				mt=_mt;
				ans=_ans;
			}else{
				break;
			}
		}

		cout << "Case #" << cn+1 << ": ";
		printf("%.7lf",ans);
		cout << endl;
	}

	return 0;
}