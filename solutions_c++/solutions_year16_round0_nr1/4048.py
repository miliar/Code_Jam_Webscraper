// #include "A-small-attempt1.in" 
// #include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <climits>
#include <utility>
#include <set>
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define RFOR(i,a,b) for(int i=(b) - 1;i>=(a);i--)
#define REP(i,n) for(int i=0;i<(n);i++)
#define RREP(i,n) for(int i=n-1;i>=0;i--)

#define PB push_back
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a,c) memset(a,c,sizeof(a))

#define DEBUG(x) cout<<"#x"<<": "<<x<<endl

using namespace std;

typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vl;

const ll INF = INT_MAX/3;
const ll MOD = 1000000007;
const double EPS = 1e-14;
const int dx[] = {1,0,-1,0} , dy[] = {0,1,0,-1};

int main(){

    int caseNum;
    cin >> caseNum;
    REP(i,caseNum){
	int c = i+1;
	ll n;
	cin >> n;
	ll tempn = n;
	int ans = -1;
	set<ll> num;
	bool flg = n != 0;


	while(flg){
	    ll temp= n;
	    while(temp > 0){
		num.insert(temp%10);
		temp /= 10;
	    }

	    if(num.size() == 10){
		ans = n;
		flg = false;
	    }
	    n += tempn;
	}

	printf("Case #%d: ",c);
	if(ans == -1) cout << "INSOMNIA" << endl;
	else cout << ans << endl;
    }

    return 0;
}


