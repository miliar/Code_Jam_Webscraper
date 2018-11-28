#include <bits/stdc++.h>
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

void negatify(string &str,int s,int t){
    FOR(i,s,t+1){
	str[i] = str[i] == '-' ? '+' : '-';
    }
}

int main(){

    int caseNum;
    cin >> caseNum;
    REP(i,caseNum){
	int c = i+1;
	string s;
	cin >> s;
	int ans = 0;
	RREP(j,s.size()){
	    if(s[j] == '-'){
		int p = -1;
		while(s[p+1] == '+'){
		    p++;
		}
		if(p >= 0){
		    reverse(s.begin(),s.begin()+p+1);
		    negatify(s,0,p);
		    ans++;
		}
		reverse(s.begin(),s.begin()+j+1);
		negatify(s,0,j);
		ans++;
	    }
	}
	printf("Case #%d: %d\n",c,ans);
    }

    return 0;
}


