#include <set>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
 
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <cassert>
 
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
// #include <random>
 
using namespace std;
 
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef pair <int, int> ii;
typedef vector <ii> vii;
typedef vector <string> vs;
 
typedef long long LL; //NOTES:int64
typedef unsigned long long ULL; //NOTES:uint64
typedef unsigned uint;
 
const double pi = acos(-1.0); //NOTES:pi
const double eps = 1e-11; //NOTES:eps
const int MAXI = 0x7fffffff;
const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};
const char dz[] = "SENW";
 
#define rep(i,n)        for (int i=0;i<n;i++)
#define loop(i,a,b)     for (int i=(a),_b=(b); i<_b; i++)
#define rloop(i,b,a)    for (int i=(b)-1,_a=(a); i>=_a; i--)
#define Reset(a,b)      memset((a),(b),sizeof(a))
 
#define endline         putchar('\n')
#define space           putchar(' ')
#define EXIT(x)         {cout << x;return 0;}
 
#define fi              first
#define se              second
#define pb              push_back
 
#define S(x)            scanf("%d",&x);
#define input freopen("input.txt","r",stdin);
#define output freopen("output.txt","w",stdout);
#define deb(i,a,n) for(i=0;i<n;i++){cout<<a[i]<<" ";}
#define db(x,y)          printf("%d %d\n",x,y);
#define debug(args...)	{dbg,args; cerr<<endl;}
#define dline			cerr<<endl	
#define INF				(int)1e9
#define LINF			(long long)1e18
#define EPS				1e-9
#define maX(a,b)		((a)>(b)?(a):(b))
#define miN(a,b)		((a)<(b)?(a):(b))
#define abS(x)			((x)<0?-(x):(x))
#define mod             1000000007
 
struct debugger
{
	template<typename T> debugger& operator , (const T& v)
	{	
		cerr<<v<<" ";	
		return *this;	
	}
} dbg;
 
void debugarr(LL * arr,int n)
{
	cout<<"[";
	for(int i=0;i<n;i++)
		cout<<arr[i]<<" ";
	cout<<"]"<<endl;
}

vector<int> v[20];
vector<int> primes;
vector< string > base2Notaions;
bool a[1000010];
int b[20];

int getDivisor(LL n) {
	for(int i=0;i<primes.size() && i<n ;i++) {
		if(n%primes[i]==0) {
			return primes[i];
		}
	}
	return -1;
}
int getTrivialDivisor(int n) {
	for(int i=0;i<primes.size();i++){ 
		if(n%primes[i]==0) {
			return i;
		}
	}

	return -1;
}

string getbase2Notation(int n) {
	string str="";
	while(n>0) {
		if(n&1) {
			str+='1';
		} else {
			str+='0';
		}
		n>>=1;
	}

	reverse(str.begin(), str.end());
	return str;
}

vector<int> getListOfDivisors(string str) {
	LL arr[12];
	for(int i=2;i<11;i++) {
		arr[i]=1;
	}
	LL ans[12];
	Reset(ans,0);
	for(int i=str.size()-1;i>=0;i--) {
		if(str[i]=='1') {
			for(int j=2;j<11;j++) {
				ans[j]+=arr[j];
			}
		}
		for(int j=2;j<11;j++) {
			arr[j]=arr[j]*j;
		}
	}


	vector<int> d;
	vector<int> result;
	for(int i=2;i<=10;i++) {
		int r = getDivisor(ans[i]);
		if(r==-1) return d;
		result.push_back(r);
	}
	// cout<<str<<endl;
	// debugarr(ans,10);
	return result;
}

void calc(int n,int m) {
	int ans=0;
	for(int i=0;i<v[n].size() && ans<m;i++) {
		// cout<<v[n][i]<<"----"<<endl;
		// int r = getTrivialDivisor(v[n][i]);
		string str = getbase2Notation(v[n][i]);
		vector<int> d = getListOfDivisors(str);
		if(d.size()==0) continue;
		cout<<str<<" ";
		ans++;
		for(int j=0;j<d.size();j++) {
			printf("%d ",d[j]);
		}
		printf("\n");
	}
	
}

int main()
{
	#ifndef ONLINE_JUDGE
        input;
        output;
    #endif
    int n,i,j,k,l,m,t,s=2,d;
    //preprocessing
    for(i=2;i<=18;i++) {
    	b[i]=s+1;
    	s<<=1;
    }
    // debugarr(b,19);
    for(i=2;i<=1000;i++) {
    	if(a[i]==1) continue;
    	for(j=i*i;j<=1000000;j+=i) {
    		a[j]=1;
    	}
    }
    int ans=0;
    for(i=2;i<=131072;i++) {
    	if(a[i]==0) {
    		primes.push_back(i);
    		string str = getbase2Notation(i);
    		base2Notaions.push_back(str);
    		ans++;
    	}
    }
    // cout<<ans<<endl;
    j=3;
    for(i=5;i<131072;i+=2) {
    	if(a[i]==0) continue;
    	if(i>=b[j] && i<b[j+1]) {
    		v[j].push_back(i);
    	} else {
    		j++;
    		v[j].push_back(i);
    	}
    }
	S(t);
	while(t--){
 	S(n);S(m);
 	printf("Case #1:\n");
 	calc(n,m);
	}
	return (0);
} 
