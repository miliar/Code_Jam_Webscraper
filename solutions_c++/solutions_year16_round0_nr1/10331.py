#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define vvi vector< vector<int> >
#define vi vector<int>
#define All(X) X.begin(),X.end()
#define FOR(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
#define pi 3.14159265359
#define shosu(X) fixed << setprecision(X)
ll gcd(ll a,ll b){return b?gcd(b,a%b):a;}
ll lcm(ll a,ll b){return a/gcd(a,b)*b;}

int main(){
	int t;
	cin >> t;
	REP(i,t){
		ll int n;
		cin >> n;
		cout << "Case #" << i + 1 << ": ";
		if(n == 0){
			cout << "INSOMNIA" << endl;
		}else{
			ll int k = 1;
			ll int tmp = n;
			map<int,int> m;
			while(1){
				tmp = k * n;
				stringstream s;
				s << tmp;
				string str = s.str();
				REP(j,str.size()){
					m[(int)(str[j]-'0')]++;
				}
				k++;
				if(m.size() == 10) break;
			}
			cout << tmp << endl;
		}
	}
}