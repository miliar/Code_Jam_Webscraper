#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <limits.h>
#include <iostream>

using namespace std;

#define rep(i,a,b) for(int i=(a);i<(b);i++)
#define vi vector<int>
#define pb push_back
#define ll long long int
#define gi(x) scanf("%d",&x)
#define ii pair<int,int>
#define CLEAR(x,val) memset(x,val,sizeof(x))
#define SZ(v) (v).size()
#define MOD 1000000007
#define MAXN 1000009
#define MAXPRIME 109000
#define BASELIMIT 11
#define MAXDIGITS 16

ll p[BASELIMIT][MAXDIGITS];
vector< vector<string> > num;
/*short int prime[MAXPRIME];
int divisor[MAXPRIME];*/
vector< vector<ll> > sol;

void calPowers(){
	rep(i,0,BASELIMIT)	p[i][0] = 1;
	rep(j,0,MAXDIGITS)	p[0][j] = 0;
	rep(i,1,BASELIMIT)
		rep(j,1,MAXDIGITS)	p[i][j] = p[i][j-1]*i;

	/*rep(i,0,10){
		rep(j,0,16)	cout<<p[i][j]<<" ";*/
}

void calComb(){
	std::vector<string> v;
	v.clear();
	v.push_back(""); num.push_back(v);
	v.clear();
	v.push_back("0");	v.push_back("1");
	num.push_back(v);
	rep(i,2,MAXDIGITS-1){
		v.clear();
		int sz = num[i-1].size();
		rep(j,0,sz){
			v.push_back(num[i-1][j]+"0");
			v.push_back(num[i-1][j]+"1");
		}
		num.push_back(v);
	}
}

int getDivisor(ll n){

	if(n==2)	return -1;

	ll sq = sqrt(n);

	if(n%2 == 0)	return 2;

	for(int i=3 ; i<=sq; i+=2){
		if(n%i == 0)	return i;
	}

	return -1;
}

/*
void calPrime(){
	CLEAR(prime,-1);

	prime[0] = 1;	divisor[0] = 0;
	prime[1] = 1;	divisor[1] = 1;

	rep(i,2,MAXPRIME){
		if(prime[i] == -1){
			prime[i] = 1;
			divisor[i] = i;
			for(int j=i+i ; j<MAXPRIME; j+=i){
				prime[j] = 0;
				divisor[j] = i;
			}
		}
	}
}*/

ll getNumber(string s, int base){
	s = "1" + s + "1";
	//cout<<s<<" base - "<<base<<endl;
	int len = s.length()-1;
	int i=0;
	ll n = 0;
	while(len>=0){
		n += p[base][len]*(s[i]=='0' ? 0 : 1);
		len--;	i++;
	}
	//cout<<" , "<<n<<endl;
	return n;
}

void solve(int N, int J){
	sol.clear();
	int sz = num[N].size();
		rep(i,0,sz){
			int base = 2;
			vector<ll> tmp;	tmp.clear();
			tmp.push_back(getNumber(num[N][i],10));
			//cout<<tmp[0]<<endl;
			for( ; base<BASELIMIT ; base++){
				ll nbase = getNumber(num[N][i],base);
				//cout<<"num - "<<num[N][i]<<"nbase -"<<nbase<<endl;

				ll divisor = getDivisor(nbase);

				if(divisor == -1){
					break;
				} else{
					//cout<<"nbase -"<<nbase<<",divisor -"<<divisor<<endl;
					tmp.push_back(divisor);
				}
			}

			if(base == BASELIMIT){
				sol.push_back(tmp);
			}

			if(sol.size() == J){
				break;
			}
		}
}

int main() {

	calPowers();
	calComb();
	//calPrime();

	int t;	cin>>t;
	rep(test,1,t+1){
		int N,J;	cin>>N>>J;

		solve(N-2,J);
		
		cout<<"Case #"<<test<<":\n";
		rep(i,0,sol.size()){
			rep(j,0,10){
				cout<<sol[i][j]<<" ";
			}
			cout<<"\n";
		}	
	}
}