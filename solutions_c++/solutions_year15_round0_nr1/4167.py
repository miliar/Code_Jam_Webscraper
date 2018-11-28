#include<bits/stdc++.h>

#define IT(a,it) for(auto it=a.begin(); it != a.end(); it++)
#define REV_IT(a,it) for(auto it=a.rbegin(); it != a.rend(); it++)
#define LL long long
#define LD long double
#define MP make_pair
#define FF first
#define SS second
#define PB push_back
#define INF (int)(1e9)
#define EPS (double)(1e-9)

#ifndef ONLINE_JUDGE
#  define LOG(x) cerr << #x << " = " << (x) << endl
#else
#  define LOG(x) 0
#endif

#define MAXX 500005

using namespace std;

typedef pair <int, int> pi_i;
typedef pair<int, pi_i> pi_ii;

bool cmp(int a, int b){ return a>b; }
template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template<class T> T lcm(T a, T b) { return a * b / gcd(a, b); }

int sm, arr[2000];
string str;

int main(){
	ios_base::sync_with_stdio(false);
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T, casee = 1;
	cin >> T;
	for(casee=1;casee<=T;casee++){
		cin >> sm >> str;
		int prev = 0, ans = 0;
		for(int i=0;i<str.size();i++){
			arr[i] = str[i] - '0';
			int need = i;
			//LOG(prev);LOG(need);
			if(need > prev){
				ans += (need - prev);
				prev += (need - prev);
			}
			prev += arr[i];
		}
		cout << "Case #" << casee << ": " ;
		cout << ans << endl;
	}
	fclose(stdin);
	fclose(stdout);
return 0;	
}

