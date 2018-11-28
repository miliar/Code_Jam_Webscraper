#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>

using namespace std;

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair
typedef long long ll;

set <ll> fair;

void compute(){
	for(ll i =1; i< 10000000001ll; i++){
		stringstream s;
		s << i;
		string str1 = s.str();
		if( equal(str1.begin(), str1.begin() + str1.size()/2, str1.rbegin()) ){		
			ll sq = ll(i*i);
			stringstream ss;
			ss << sq;
			string str = ss.str();
			if( equal(str.begin(), str.begin() + str.size()/2, str.rbegin()) ){
				cout<<i<< " "<<str<<endl;
				fair.insert(sq);
				}
			}
		}
	}
	
int main(){
	
	//compute();
	int T;
	cin>>T;

	fair.insert(1);
	fair.insert(4);
	fair.insert(9);
	fair.insert(121);
	fair.insert(484);
	fair.insert(10201);
	fair.insert(12321);
	fair.insert(14641);
	fair.insert(40804);
	fair.insert(44944);
	fair.insert(1002001);
	fair.insert(1234321);
	fair.insert(4008004);
	fair.insert(100020001);
	fair.insert(102030201);
	fair.insert(104060401);
	fair.insert(121242121);
	fair.insert(123454321);
	fair.insert(125686521);
	fair.insert(400080004);
	fair.insert(404090404);
	fair.insert(10000200001ll);
	fair.insert(10221412201ll);
	fair.insert(12102420121ll);
	fair.insert(12345654321ll);
	fair.insert(40000800004ll);
	fair.insert(1000002000001ll);
	fair.insert(1002003002001ll);
	fair.insert(1004006004001ll);
	fair.insert(1020304030201ll);
	fair.insert(1022325232201ll);
	fair.insert(1024348434201ll);
	fair.insert(1210024200121ll);
	fair.insert(1212225222121ll);
	fair.insert(1214428244121ll);
	fair.insert(1232346432321ll);
	fair.insert(1234567654321ll);
	fair.insert(4000008000004ll);
	fair.insert(4004009004004ll);
	//cout<<fair.size()<<endl;
	REP(i,T){
		ll A,B;
		cin>>A>>B;
		set <ll>::iterator it;
		int ans=0;
		for(it = fair.begin(); it!=fair.end(); ++it){
			if( *it >= A && *it <= B)	ans++;
			}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
		}
	return 0;
	}
