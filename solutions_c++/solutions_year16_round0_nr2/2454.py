#include<bits/stdc++.h>
using namespace std;
#define endll           "\n"
#define INIT(n,m)       memset(n,m,sizeof(n))
#define REP(i,n)        for(int i=0;i<n;i++)
#define FOR(i,a,b)      for(int i=a;i<=b;i++)
#define FORD(i,a,b)     for(int i=a;i>=b;i--)
#define PB              push_back
#define IN(a,b)         substr(a,b-a+1)
#define FF              first
#define SS              second
#define LEN(x)          ((int)x.size())
#define MM              1000000007
#define CHECK(x,y)      (((x%=y)+=y)%=y)
#define DEBUG(x)        {cout<<#x<<" = ";cout << (x) << endll;}
#define PR(v)           {cout<<#v<<" = ";for(auto _:v)cout<<_<<' ';cout<<endll;}
#define PRR(a,b,n)      {cout<<#a<<" = ";FOR(_,b,n)cout<<a[_]<<' ';cout<<endll;} 
#define FOREACH(it, c)  for(__typeof((c).begin())it=(c).begin();it!=(c).end();++it)
#define FILE_IO(a,b)    {freopen(a,"r",stdin);freopen(b,"w",stdout);}
struct  IO              {IO(){ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);}}_;
typedef long long ll;
typedef pair<int,int> ii;
int n,m,len,k,t,a,b;

string s;
map<int,int> dp[101];

void flip(int l, int r){
	string temp = s;
	int j = r;
	FOR(i,l,r){
		temp[i] = s[j--];
	}
	FOR(i,l,r){
		s[i] = ((temp[i] == '+')?('-'):('+'));
	}
}

int hashh(string s){
	ll h = 0;
	for(auto cur:s){
		h *= 101;
		CHECK(h,MM);
		h += cur;
		CHECK(h,MM);
	}
	return h;
}

int rec(int h, int las){
	if(las == 0){
		return s[0] == '-';
	}
	
	if(dp[las].count(h)) return dp[las][h];
	
	if(s[las] == '+'){
		int j = las;
		while(j >= 0 && s[j] == '+') j--;
		if(j < 0) return 0;
		return rec(h,j);
	}
	
	
	int minz = MM;
	
	if(s[0] == '-'){
		flip(0,las);
		minz = 1 + rec(hashh(s),las);
		flip(0,las);
		return minz;
	}
	
	FOR(i,0,las-1) if(s[i] == '+'){
		flip(0,i);
		minz = min(minz, 1 + rec(hashh(s),las));
		flip(0,i);
	}
	
	return dp[las][h] = minz;
}

int main(){
	FILE_IO("B-small-attempt0.in","output.out");
	cin >> t;
	REP(tc,t){
		REP(i,101) dp[i].clear();
		cin >> s;
		cout << "Case #" << tc+1 << ": " << rec(hashh(s),LEN(s)-1) << endll;
	}
	return 0;
}
