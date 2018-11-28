#include<bits/stdc++.h>

#define getcx getchar_unlocked
#define putcx putchar_unlocked
#define ll long long int
#define ull unsigned long long int
#define MOD 1000000007
#define INF INT_MAX
#define _INF INT_MIN
#define STRING_SIZE 100005
#define pb push_back
#define mp make_pair
#define pi pair<int,int>
#define vpi vector<pi >
#define vvpi vector<vpi >
#define vi vector<int>
#define vvi vector<vi >
#define F first
#define S second
#define B begin
#define E end
#define dbg(x) cout << "x = " << x << endl

#define rep(i,s,e) for(int i=s;i<=e;i++)

using namespace std;

// faster input for integers, use scanf real numbers
template <typename T>
inline void inp(T& n){
	n=0;
	bool neg=false;
	register char ch=getcx();
	while(ch<33){
		ch=getcx();
	}
	while(ch>32){
		if(ch!='-'){
			n=(n<<3)+(n<<1)+ch-'0';
		}
		else {
			neg=true;
		}
		ch=getcx();
	}
	if(neg){
		n=-n;
	}
}
// faster input for c++ strings
inline void inps(string& s){
	ios::sync_with_stdio(false);
	cin >> s;
}

// faster input for c strings
inline void inps(char *s){
	fgets(s,STRING_SIZE,stdin);
	s[strcspn(s,"\n")]=0; // to remove the traling newline
}

// use printf or cout for printing, the difference is negligible

bool cmp(const pair<char,int> &a, const pair<char,int> &b){
	return a.S < b.S;
}
int main(){
	int t,n,p;
	inp(t);
	rep(c,1,t){
		inp(n);
		vector<pair<char,int> > cnt;
		rep(i,0,n-1){
			inp(p);
			cnt.pb(mp('A'+i,p));
		}
		sort(cnt.begin(),cnt.end(),cmp);
		printf("Case #%d: ",c);
		while(n>2){
			while(cnt[n-1].S > cnt[n-2].S){
				printf("%c ",cnt[n-1].F);
				cnt[n-1].S--;
			}
			while(cnt[n-2].S > cnt[n-3].S){
				printf("%c%c ",cnt[n-1].F,cnt[n-2].F);
				cnt[n-1].S--;
				cnt[n-2].S--;
			}
			while(cnt[n-1].S){
				printf("%c ",cnt[n-1].F);
				cnt[n-1].S--;
			}
			n--;
		}
		while(cnt[1].S > cnt[0].S){
			printf("%c ",cnt[1].F);
			cnt[1].S--;
		}
		while(cnt[1].S > 0){
			printf("%c%c ",cnt[1].F,cnt[0].F);
			cnt[1].S--;
			cnt[0].S--;
		}
		printf("\n");
	}
	return 0;
		
		
		


}
