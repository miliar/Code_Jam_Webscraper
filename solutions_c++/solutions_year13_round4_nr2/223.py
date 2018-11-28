#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <valarray>
#include <vector>

#define EPS 1e-9
#define INF 1070000000LL
#define MOD 1000000007LL
#define fir first
#define foreach(it,X) for(__typeof((X).begin()) it=(X).begin();it!=(X).end();it++)
#define ite iterator
#define mp make_pair
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);i++)
#define pb push_back
#define sec second
#define sz(x) ((int)(x).size())

using namespace std;

struct timer{
	time_t start;
	timer(){start=clock();}
	~timer(){cerr<<1.*(clock()-start)/CLOCKS_PER_SEC<<" secs"<<endl;}
};

typedef istringstream iss;
typedef long long ll;
typedef pair<int,int> pi;
typedef stringstream sst;
typedef vector<int> vi;

ll N,P;

void main2(){
	cin>>N>>P;
	P--;
	
	ll worst=0,n=1,res1=0,pos=0;
	while(1){
		//cout<<pos<<" "<<worst<<" "<<n<<endl;
		if(worst <= P)res1=pos;
		else break;
		if(res1==(1LL<<N)-1)break;
		pos += 1LL<<n;
		pos=min(pos,(1LL<<N)-1);
		worst += 1LL<<N-n;
		worst=min(worst,(1LL<<N)-1);
		n++;
	}
	
	ll best=0,res2=0;
	n=1,pos=0;
	while(1){
		//cout<<pos<<" "<<best<<" "<<n<<endl;
		if(best <= P)res2=pos;
		else break;
		if(res2==(1LL<<N)-1)break;
		pos += 1LL<<N-n;
		best += 1LL<<n-1;
		n++;
	}
	
	cout<<res1<<" "<<res2<<endl;
}

int main(){
	int T;
	cin>>T;
	time_t start=clock(),pre=start;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		main2();
		time_t now=clock();
		cerr<<tc+1<<"/"<<T<<": "<<(double)(now-pre)/CLOCKS_PER_SEC<<endl;
		if(tc==T-1){
			cerr<<"Total: "<<(double)(now-start)/CLOCKS_PER_SEC<<endl;
			cerr<<"  Ave: "<<(double)(now-start)/CLOCKS_PER_SEC/T<<endl;
		}
		pre=now;
	}
}
