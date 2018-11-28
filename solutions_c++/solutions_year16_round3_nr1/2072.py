#include <bits/stdc++.h>
using namespace std;

#define FOR(i, to, from) for(int i=to; i<from; i++)
#define ri(n) scanf("%d", &n)
#define rii(n, m) scanf("%d %d", &n, &m);
#define ms(obj,val) memset(obj, val, sizeof(obj))
#define pb push_back
typedef long long ll;
typedef vector<int> vi;

int C[30];
int N, M;
int c, a;
int T;
int main(){
	cin >>T;
	FOR(t, 1, T+1){
		cin >> N;
		cout <<"Case #"<< t << ":";
		ms(C, 0);
		M=0;
		FOR(i, 0, N) {
			cin>>C[i];
			M+=C[i];
		}
		FOR(i, 0, M){
			if(i==0 || ((M-i)&1)==0) cout << ' ';
			c=0;
			FOR(i, 0, N){
				if(C[i]>c){
					c=C[i];
					a=i;
				}
			}
			cout << (char) (a+'A');
			C[a]--;
		}
		cout << endl;
	}	
}

