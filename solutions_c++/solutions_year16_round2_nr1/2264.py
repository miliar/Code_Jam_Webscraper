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


int main(){
	map<char,int> cnt;
	string s;
	int t;
	inp(t);
	rep(c,1,t){
		cin >> s;
		int dgt[10]={0};
		int n=s.size();
		rep(i,0,n-1) cnt[s[i]]++;
		while(cnt['Z']){
			dgt[0]++;
			cnt['Z']--;
			cnt['E']--;
			cnt['R']--;
			cnt['O']--;
		}	
		while(cnt['W']){
			dgt[2]++;
			cnt['T']--;
			cnt['W']--;
			cnt['O']--;
		}	
		while(cnt['U']){
			dgt[4]++;
			cnt['F']--;
			cnt['O']--;
			cnt['U']--;
			cnt['R']--;
		}	
		while(cnt['R']){
			dgt[3]++;
			cnt['T']--;
			cnt['H']--;
			cnt['R']--;
			cnt['E']--;
			cnt['E']--;

		}	
		while(cnt['G']){
			dgt[8]++;
			cnt['E']--;
			cnt['I']--;
			cnt['G']--;
			cnt['H']--;
			cnt['T']--;
		}	
		while(cnt['O']){
			dgt[1]++;
			cnt['O']--;
			cnt['N']--;
			cnt['E']--;
		}	
		while(cnt['F']){
			dgt[5]++;
			cnt['F']--;
			cnt['I']--;
			cnt['V']--;
			cnt['E']--;
		}	
		while(cnt['V']){
			dgt[7]++;
			cnt['S']--;
			cnt['E']--;
			cnt['V']--;
			cnt['E']--;
			cnt['N']--;

		}	
		while(cnt['X']){
			dgt[6]++;
			cnt['S']--;
			cnt['I']--;
			cnt['X']--;
		}	
		while(cnt['I']){
			dgt[9]++;
			cnt['N']--;
			cnt['I']--;
			cnt['N']--;
			cnt['E']--;
		}
		printf("Case #%d: ",c);	
		rep(i,0,9){
			while(dgt[i]){
				printf("%d",i);
				dgt[i]--;
			}
		}
		printf("\n");
	}
	return 0;




}
