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

int main(){
	ios_base::sync_with_stdio(false);
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T, casee = 1;
	cin >> T;
	for(casee=1;casee<=T;casee++){
		int X, R, C;
		cin >> X >> R >> C;
		cout << "Case #" << casee << ": " ;
		if((R*C) >= X && (R*C) % X == 0){
			if(X == 4){
				if(R <=2 || C <= 2) cout << "RICHARD" <<endl;
				else cout << "GABRIEL" << endl;
			}else if(X == 3){
				if(R <= 1 || C <= 1) cout << "RICHARD" <<endl;
				else cout << "GABRIEL" << endl;
			}else{
				cout << "GABRIEL" << endl;
			}
		}else cout << "RICHARD" <<endl;
	}
	fclose(stdin);
	fclose(stdout);
return 0;	
}

