# include <cstdio>
# include <iostream>
# include <vector>
# include <algorithm>
# include <cmath>
# include <queue>
# include <map>
# include <cstring>
# include <string>
# include <set>

using namespace std;

# define INF 1000000000
# define MOD 1000000007
# define ll long long
# define pb push_back
# define mp make_pair

int main(){
	
	freopen("input.in", "r", stdin);
	freopen("output6.txt", "w", stdout);

	int ttt;
	cin>>ttt;

	for(int tt = 1; tt <= ttt; tt++){

		int n;
		cin>>n;

		vector<pair<int,int>> w;
		int x;

		for(int i = 0; i < n; i++){
			cin>>x;
			w.pb({x, i});
		}

		cout<<"Case #"<<tt<<": ";

		sort(w.begin(), w.end());
		reverse(w.begin(), w.end());

		int sum;
		while(w[0].first != 0){

			sum = 0;
			for(int i = 1; i < w.size(); i++){
				sum += w[i].first;
			}

			if(sum == 1 && w[0].first == 1){
					w[0].first--;
					w[1].first--;
					char a = ('A'+w[0].second);
					char b = ('A'+w[1].second);
					cout<<a<<b<<" ";
			}
			else{
				if(((w[0].first - 1) < (sum)) && (w.size() != 2)){
					w[0].first--;
					char a = ('A'+w[0].second);
					cout<<a<<" ";
				}
				else if((w[0].first - 1) == sum){
					w[0].first--;
					char a = ('A'+w[0].second);
					cout<<a<<" ";
				}
				else
				{
					w[0].first--;
					w[1].first--;
					char a = ('A'+w[0].second);
					char b = ('A'+w[1].second);
					cout<<a<<b<<" ";
				}
			}

			sort(w.begin(), w.end());
			reverse(w.begin(), w.end());

		}

		cout<<endl;

	}

	return 0;
}