#include <bits/stdc++.h>
#define isNum(c) c<='9' && c>='0'
#define islettre(c) c<='z' && c>='a'
#define isLETTRE(c) c<='Z' && c>='A'
#define MS0(x) memset(x,0,sizeof(x))
#define MS(x,s) memset(x,s,sizeof(x))
#define rep(i,n) for(i=0;i<n;i++)
#define rev(i,n) for(i=n;i>=0;i--)
#define repv(i,v) for(i=0;i<v.size();i++)
#define repa(i,a,n) for(i=a;i<n;i++)
#define all(c) c.begin(),c.end()
#define rall(c) c.rbegin(),c.rend()
#define NOT_VISITED 0
#define IS_VISITED 1
#define MOD 1000000009
#define INF 1000000009
#define COL 100002
#define trMap(c,i) for(map<char,int>::iterator i = (c).begin(); i != (c).end(); i++)
#define trSet(c,i) for(set< pair <int,char> >::iterator i = (c).begin(); i != (c).end(); i++)
#define PB(val) push_back(val)
#define MP(f,s) make_pair(f,s)
#define abs(i) (i<0)?-i:i
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector< ii > vii;



int main(){
	int T,N,i,j,k;
	cin >> T;
	rep(i,T){
		cin >> N;
		cout << "Case #" << (i+1) << ": ";
		int v[10];
		rep(k,10) v[k] = 0;
		if(!N) cout << "INSOMNIA" << endl;
		else{
			int t = 0;
			long long n;
			j = 1;
			while(!t){
				n = N*((long long)j);
				while(n){
					v[n%10] = 1;
					n /= 10;
				}
				t = 1;
				rep(k,10){
					t &= v[k];
				}
				j++;
			}
			n = N*((long long)(j-1));
			cout << n << endl;
		}
	}
}