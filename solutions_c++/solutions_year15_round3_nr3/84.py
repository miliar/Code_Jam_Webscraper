/*
	In the Name Of GOD
	TRIPLE NARENGIES:)
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

//int arr[400];
ll c,d,v;

/*
bool ok(){
	FOR1(i,v){
		if(arr[i]==0)
			return 0;
	}
	return 1;
}
*/
int main()
{
	ios::sync_with_stdio(false);
	int T; cin>>T;
	int test = 0;
	while(T--)
	{
		test++;
		/*int ans = 0;
		CLR(arr,0);
		cin>>c>>d>>v;
		vi coins;
		FOR(i,d){
			int tmp;
			cin>>tmp;
			coins.PB(tmp);
		}
		Sort(coins);
		arr[0] = 1;
		arr[coins[0]]=1;
		for(int i=1;i<coins.sz;i++){
			for(int j=v;j>=0;j--){
				if(arr[j]==1){
					arr[j+coins[i]]=1;
				}
			}
		}
		while(!ok()){
			int  pos = -1;
			FOR1(i,v){
				if(arr[i]==0){
					pos = i;
					break;
				}
			}
			for(int j=v;j>=0;j--){
				if(arr[j]==1){
					arr[j+pos]=1;
				}
			}
			ans++;

		}*/

		cin>>c>>d>>v;
		vector <ll> coins;
		FOR(i,d){
			ll tmp;
			cin>>tmp;
			coins.PB(tmp);
		}
		Sort(coins);
		ll tedad = 0;
		ll tah = 0;
		ll flag = 0;
		while(tah<v){
			if(flag==coins.sz){
				tah+=(tah+1)*c;
				tedad++;
			}else if(tah>=coins[flag]-1){
				tah+=coins[flag]*c;
				flag++;
			}else{
				tah+=(tah+1)*c;
				tedad++;
			}
		}
		cout<<"Case #"<<test<<": "<<tedad<<endl;
	}
}
