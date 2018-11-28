#include<bits/stdtr1c++.h>
using namespace std;
typedef long long LL;
int n;
vector<int> v, ov;
const int MX = 25 * 25 * 25 * 25 * 25 *2 +19;
int vis[MX], ans[MX];
int ID;
int get_state() {
	int ret = 0;
	for (int i = 0; i < n; i++) {
		ret *= 25;
		ret += v[i];
	}
	return ret;
}
int get_min() {
	int ret = v[0];
	for (int i = 0; i < n; i++) {
		ret = min(v[i], ret);
	}
	return ret;
}
priority_queue<int, vector<int>, greater<int> > q;
void update()
{
	int mi=get_min();
	for(int i=0;i<n;i++)
	{
		v[i]-=mi;
		if(v[i]==0)
			q.push(i);
	}
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("2.in", "r", stdin);
	freopen("2.out","w",stdout);
#endif // ONLINE_JUDGE
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int tc;
	int ic = 1;
	cin >> tc;
	while (tc--) {
		ID++;
		v.clear();
		cin >> n;
		LL k;
		cin>>k;
		v.resize(n);
		for (int i = 0; i < n; i++)
			cin >> v[i];
		ov = v;
		v.clear();
		v.resize(n,0);
		int t = 0;
		int c = 0;
		while (vis[t] != ID) {
			vis[t] = ID;
			update();
			while (q.size()) {
				int ind=q.top();
				ans[c++] =ind;
				v[ind]=ov[ind];
				q.pop();
			}
			t = get_state();
		}
		c-=n;
		/*cout<<(k-1)%c<<endl;
		cout<<c<<" "<<k<<endl;
		for(int i=0;i<c;i++)
		cout<<ans[i]+1<<" ";
		cout<<endl;*/
		cout << "Case #" << ic++ << ": " <<ans[(k-1)%c]+1<< endl;
	}
	return 0;

}
