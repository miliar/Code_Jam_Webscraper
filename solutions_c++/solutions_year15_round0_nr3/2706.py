#include<bits/stdc++.h>
#include <unistd.h>

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

string s, ss;
int L, X;

int table[5][5];
int value1[20000], mi1[20000], value3[20000], mi3[20000];

pi_i get(string s1, int vv){
	int minus = 0;
	int curr = 0;
	for(int k=0;k<s1.size();k++){
		int v = 0;
		if(s1[k] == 'i') v = 2;
		else if(s1[k] == 'j') v = 3;
		else v = 4;
		if(curr == 0){ curr = v;continue; }
		
		int val = table[curr][v];
		if(val < 0){
			if(minus == 0) minus = 1;
			else minus = 0;
			curr = -1*val;
		}else{
			curr = val;
		}
	}
	return MP(curr, minus);
}


pi_i nextVal(int curr, int minus, int v){
	if(curr == 0) return MP(v, 0);
	
	int val = table[curr][v];
	if(val < 0){
		if(minus == 0) minus = 1;
		else minus = 0;
		curr = -1*val;
	}else{
		curr = val;
	}
	return MP(curr, minus);
}

int main(){
	ios_base::sync_with_stdio(false);
	
	freopen("in.txt","r",stdin);
	freopen("out1.txt","w",stdout);
	
	table[1][1] = 1;table[1][2] = 2;table[1][3] = 3;table[1][4] = 4;
	table[2][1] = 2;table[2][2] = -1;table[2][3] = 4;table[2][4] = -3;
	table[3][1] = 3;table[3][2] = -4;table[3][3] = -1;table[3][4] = 2;
	table[4][1] = 4;table[4][2] = 3;table[4][3] = -2;table[4][4] = -1;
	
	int T, casee = 1;
	cin >> T;
	for(casee=1;casee<=T;casee++){
		cin >> L >> X;
		cin >> s;
		ss = "";
		for(int i=0;i<X;i++){
			ss += s; 
		}
		bool ans = false;
		
		int curr = 0, minus = 0;
		for(int i=0;i<ss.size();i++){
			//for(int j=0;j<=i;j++) temp1 += ss[j];
			int v = 0;
			if(ss[i] == 'i') v = 2;
			else if(ss[i] == 'j') v = 3;
			else v = 4;
			pi_i pp = nextVal(curr, minus, v);
			value1[i] = pp.FF;curr = pp.FF;
			mi1[i] = pp.SS;minus = pp.SS;
		}
		
		pi_i total = get(ss, 0);
		//cout << total.FF << " " << total.SS << endl;
		
		if(total.FF == 1 && total.SS == 1){
			bool found = false;
			for(int i=0;i<ss.size()-1;i++){
				if(found == false && value1[i] == 2 && mi1[i] == 0) found = true;
				else if(found == true && value1[i] == 4 && mi1[i] == 0) ans = true;
			}
		}
		
		cout << "Case #" << casee << ": " ;
		if(ans == true) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
	fclose(stdin);
	fclose(stdout);
return 0;	
}

