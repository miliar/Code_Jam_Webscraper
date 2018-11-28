#include <bits/stdc++.h>
using namespace std;

#define sz(v)			(int)(v.size())
#define all(v)			v.begin(),v.end()
#define mems(a , i)		memset(a , i , sizeof(a))
#define memc(a , b)		memcpy(a , b , sizeof(a))
#define mp(x , y)		make_pair(x , y)
#define pb(x)			push_back(x)
#define ansy			{cout << "-1" << endl;return 0;}
#define ansn			{cout << "No" << endl;return 0;}
#define IOS				ios_base::sync_with_stdio(0) , cin.tie(0) , cout.tie(0);
#define mod				1000000007
#define PI				3.14159265358979323846
#define fi				first
#define se				second
const double EPS = 1e-8;


int main() {
#ifndef ONLINE_JUDGE
	freopen("/home/momen/Downloads/A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	IOS;
	int t , p;
	cin >> t;
	for(int tt = 1; tt <= t ; tt++){
		priority_queue < pair <int , int> > q;
		cin >> p;
		int cnt = 0;
		for(int i = 0 , k ;i < p ; i++){
			cin >> k;
			cnt += k;
			q.push(mp(k , i));
		}
		string ans = "";
		while(!q.empty()){
			pair <int, int> p = q.top();
			q.pop();
			ans += " " ;
			ans += char(p.se + 'A');
			p.fi -- , cnt--;
			if(p.fi > 0){
				q.push(p);
			}
			if(q.empty())	break;
			p = q.top();
			q.pop();
			if(p.fi > (cnt)/2){
				ans += char(p.se + 'A');
				p.fi -- , cnt--;
			}
			if(p.fi > 0){
				q.push(p);
			}
		}
		cout << "Case #" << tt << ":" << ans << endl;
	}
	return 0;
}
