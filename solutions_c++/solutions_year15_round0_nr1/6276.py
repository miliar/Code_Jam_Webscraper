# include <iostream>
# include <vector>
# include <cstring>
# include <string>
# include <cmath>
# include <algorithm>
# include <iomanip>
# include <cstdio>

using namespace std;

# define INF 1000000000
# define MOD 1000000007
# define all(x) x.begin(),x.end()
# define mp make_pair
# define pb push_back
# define pi pair<int,int>

void solve(){

	int n;
	string t;
	cin>>n>>t;
	n++;

	int sum = t[0]-'0';
	int res = 0;
	for (int i = 1; i < n; ++i){
		if(t[i] == '0') continue;
		if(sum < i){
			res += i - sum;
			sum = i;
			sum += t[i]-'0';
		}
		else sum += t[i]-'0';
	}

	cout<<res<<endl;

}

int main(){
	
	freopen("inputAlarge.in","r",stdin);
	freopen("outputAlarge.txt","w",stdout);

	int ttt;
	cin>>ttt;

	for (int tt = 1; tt <= ttt; ++tt){
		cout<<"Case #"<<tt<<": ";
		solve();
	}

	return 0;
}