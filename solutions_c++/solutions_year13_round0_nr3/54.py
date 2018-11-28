#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <ctime>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <functional>
#include <fstream>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>
#include <numeric>
#include <cassert>
using namespace std;
static const double EPS = 1e-10;
typedef long long ll;
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n-1;i>=0;i--)
#define all(a) a.begin(),a.end()
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define SS stringstream
#define DBG1(a) rep(_X,sz(a)){printf("%d ",a[_X]);}puts("");
#define DBG2(a) rep(_X,sz(a)){rep(_Y,sz(a[_X]))printf("%d ",a[_X][_Y]);puts("");}
#define bitcount(b) __builtin_popcount(b)
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)

#define delete(a,n) a.erase(remove(all(a),n),a.end())
template<typename T, typename S> vector<T>& operator<<(vector<T>& a, S b) { a.push_back(b); return a; }
template<typename T> void operator>>(vector<T>& a, int b) {while(b--)if(!a.empty())a.pop_back();}
bool isprime(int n){ if(n<2)return false;  for(int i=2;i*i<=n;i++)if(n%i==0)return false;  return true;} 
ll b_pow(ll x,ll n){return n ? b_pow(x*x,n/2)*(n%2?x:1) : 1ll;}
string itos(int n){stringstream ss;ss << n;return ss.str();}

class bigInteger{
#define DIGITMAX (60) // 4 * n digit
public:
	std::vector<int> value;
 
	bigInteger operator=(bigInteger b){
		this->value = b.value;
		return *this;
	}
	/* O(n) */
	bigInteger operator+(bigInteger b){
		for(int i=0;i<DIGITMAX;i++){
			b.value[i] += this->value[i];
			if(b.value[i]>=10000){
				b.value[i] -= 10000;
				b.value[i+1]++;
			}
		}
		return b;
	}
	/* O(n) */
	bigInteger operator-(bigInteger b){
		for(int i=0;i<DIGITMAX;i++){
			b.value[i] = this->value[i] - b.value[i];
			if(b.value[i]<0){
				b.value[i] = 10000+b.value[i];
				b.value[i+1]++; // b wo oome
			}
		}
		return b;
	}
	/* with bug.. O(n^2) */
	// MiniNum * BigNum
	bigInteger operator*(bigInteger b){
		bigInteger ret;
		for(int i=0;i<DIGITMAX;i++){
			if( this->value[i] == 0 ) continue;
			for(int j=0;j<DIGITMAX;j++){
				if(i+j+1<DIGITMAX){
					ret.value[i+j] += this->value[i]*b.value[j];
					ret.value[i+j+1] += ret.value[i+j]/10000;
					ret.value[i+j] %= 10000;
				}
			}
		}
		return ret;
	}
 
	string str(){
		char tmp[5];
		string retVal = "";
		for(int i=DIGITMAX-1;i>=0;i--){
			sprintf(tmp,"%04d",value[i]);
			retVal += tmp;
		}
		while(retVal[0] == '0' && retVal.length()>=2)retVal = retVal.substr(1);
		return retVal;
	}
 
	bigInteger(){this->value.resize(DIGITMAX);}
	bigInteger(string init){
		vector<int> vi;
		for(int i=init.length()-4;i>-4;i-=4){
			vi.push_back( atoi(init.substr(max(i,0),4+(i<0?i:0)).c_str()) );
		}
		this->value = vi;
		this->value.resize(DIGITMAX);
	}
};

void putCase(){
	static int x = 1;
	cout << "Case #" << x++ << ": ";
}
int isp(string s){
	string t = s;
	reverse(t.begin(),t.end());
	return s == t;
}


vector<string> s;

void dfs(int sum,string r){
	if(sum>=10) return;
	if( r.size() > 52 ) return;
	string t = r;
	reverse(t.begin(),t.end());
	if(r!="")s.push_back(r+t);
	for(int i = 0 ; i < 4 ; i++){
		if( sum + i*i < 10 ){
			s.push_back(r+string(1,'0'+i)+t);
		}
	}
	for(int i = (r=="") ; i < 4 ; i++){
		dfs(sum+2*i*i,r+(char)('0'+i));
	}
}


bool cmp(const string &a,const string &b){
	return a.size() != b.size() ? a.size() < b.size() : a < b;
}
int UB(string x){
	int l = 0 , r = s.size() - 1;
	while(l!=r){
		int m = (l+r) / 2;
		if( cmp(s[m],x) || s[m] == x){
			l = m+1;
		}else{
			r = m;
		}
	}
	return r;
}
int LB(string x){
	int l = 0 , r = s.size() - 1;
	while(l!=r){
		int m = (l+r) / 2;
		if( cmp(s[m],x)){
			l = m+1;
		}else{
			r = m;
		}
	}
	return r;
}
int main(){
	dfs(0,"");
	sort(s.begin(),s.end(),cmp);
	for(int i = 0 ; i < s.size() ; i++){
		bigInteger a(s[i]);
		a = a * a;
		s[i] = a.str();
		//cout << i << endl;
	}
	//cout << s.size() << endl;
	//cout << FF(10) << endl;
	//return 0;
	//cout << F(10000000000000ll) << endl;
	//cout << FF(10000000000000ll) << endl;
	int T;
	cin >> T;
	while(T--){
		string a,b;
		cin >> a >> b;
		bigInteger c(a);
		putCase(); cout << UB(b) - LB(a) << endl;
	}
}