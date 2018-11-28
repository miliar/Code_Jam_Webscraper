/*
	In the Name Of GOD
*/
#include <vector>
#include <map>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <complex>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <iomanip>
#include <set>
#include <stack>
#include <stdio.h>

using namespace std;
#define N 10020
#define MAXN 60
#define X first
#define Y second
#define CLR(x,a) memset(x,a,sizeof(x))
#define FOR(i,b) for(ll i=0;i<(b);i++)
#define FOR1(i,b) for(ll i=1;i<=(b);i++)
#define FORA(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORB(i,b,a) for(ll i=(b);i>=(a);i--)
#define sh(x) cerr<<(#x)<<" = "<<(x)<<endl
#define EPS 0.00001
#define ull unsigned long long int
#define ll long long 
#define MP make_pair
#define PB push_back
#define ALL(v) (v).begin(),(v).end()
#define sz size()
#define EXIST(a,b) find(ALL(a),(b))!=(a).end()
#define Sort(x) sort(ALL(x))
#define UNIQUE(v) Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define timestamp(x) printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
//const double PI = acos(-1);
typedef complex<double> point;
typedef pair<int,int> pii;
typedef pair<int, pii> piii;
typedef vector<int> vi;
typedef vector<vi > vii;
typedef vector<pii> vpii;
typedef vector<piii> vpiii;

vector <int> num(16,0);

ll is_prime(ll n){
	for(ll i=2;i*i<=n;i++){
		if(n%i==0){
			return i;
		}
	}
	return 0;
}

void plusplus(){
	num[0]++;
	for(int i=0;i<16;i++){
		if(num[i]==2){
			num[i]=0;
			num[i+1]++;
		}
	}
}

ll get_num(int b){
	ll p = 1;
	ll ans = 0;
	for(int i=0;i<16;i++){
		ans+=num[i]*p;
		p*=b;
	}
	return ans;
}


int main()
{
	int h;
	ios::sync_with_stdio(false);
	cin>>h>>h>>h;
	num[0] = num[15] = 1;
	// cout<<get_num(10)<<endl;
	int cnt=0;
	cout<<"Case #1:"<<endl;
	while(true){
		vector <ll> ans;
		// if(is_prime(get_num(10))==0){
		// 	plusplus();
		// 	continue;
		// }
		ans.PB(get_num(10));
		bool flag = false;
		for(int i=2;i<=10;i++){
			ll x = get_num(i);
			// sh(x);
			if(is_prime(x)!=0){
				ans.PB(is_prime(x));
			}else{
				flag = true;
				break;
			}
		}
		// sh(get_num(2));
		if(!flag){
			for(int i=0;i<ans.sz;i++){
				cout<<ans[i]<<" ";
			}
			cout<<endl;
			cnt++;
		}
		if(cnt==50)
			break;
		plusplus();
		plusplus();
	}
}
