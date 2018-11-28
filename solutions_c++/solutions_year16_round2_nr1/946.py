#include <bits/stdc++.h>
#define loop(i,n) for(int i = 0;i < (n);i++)
#define range(i,a,b) for(int i = (a);i <= (b);i++)
#define rrep(i,n) for(int i = (n);i >= 0;i--)
#define rran(i,a,b) for(int i = (b);i >= (a);i--)
#define step(i,a,b,d) for(int i = (a);i <= (b); i += d)
#define all(A) A.begin(),A.end()
#define PI acos(-1)
#define pb push_back
#define mp make_pair
#define sz(A) A.size()
#define len(A) A.length()
#define vi vector<int>
#define ll long long
#define pi pair<int,int>
#define point pair<double,double>
#define pl pair<ll,ll>
#define popcnt(x) __builtin_popcount(x)
#define LSOne(x) ((x) & (-(x)))
#define xx first
#define yy second
#define PQ priority_queue
#define print(A,t) cerr << #A << ": "; copy(all(A),ostream_iterator<t>(cerr," " )); cerr << endl
#define prp(p) cerr << "(" << (p).first << " ," << (p).second << ")";
#define prArr(A,n,t)  cerr << #A << ": "; copy(A,A + n,ostream_iterator<t>(cerr," " )); cerr << endl
#define pre() cin.tie(0),cerr.tie(0),ios_base::sync_with_stdio(0)
using namespace std;

string S [] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
pair<char,int> f_ind[5] = {{'G',8},{'U',4},{'W',2},{'X',6},{'Z',0}};
pair<char,int> s_ind[4] = {{'F',5} ,{'H',3} ,{'O',1} ,{'S',7}};

char s[5000];

string solve(){
	vi CTR1(26,0),CTR2(10,0);
	int L = strlen(s);
	loop(i,L) CTR1[s[i] - 'A']++;
	for(auto x : f_ind){
		int i = x.xx - 'A';
		while(CTR1[i]){
			CTR2[x.yy]++;
			for(char c : S[x.yy]) CTR1[c - 'A']--;
		}
	}
	for(auto x : s_ind){
		int i = x.xx - 'A';
		while(CTR1[i]){
			CTR2[x.yy]++;
			for(char c : S[x.yy]) CTR1[c - 'A']--;
		}
	}
	while(CTR1['N' - 'A']){
		CTR2[9]++;
		CTR1['N' - 'A'] -= 2;	
	}
	string ret = "";
	loop(i,10) ret += string(CTR2[i],i + '0');
	return ret;
}

int main(){
	int T;
	scanf("%d",&T);			
	loop(t,T){
		scanf("%s",s);
		printf("Case #%d: %s\n",t + 1,solve().c_str());
	}	


	return 0;
}

