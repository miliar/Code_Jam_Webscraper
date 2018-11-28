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
	freopen("output.txt", "w", stdout);

	int ttt;
	cin>>ttt;

	for(int tt = 1; tt <= ttt; tt++){
		string s;

		cin>>s;

		string res;

		res += s[0];

		for(int i = 1; i < s.size(); i++){
			if(s[i] >= res[0])
				res = s[i] + res;
			else res += s[i];
		}

		cout<<"Case #"<<tt<<": "<<res<<endl;
	}

	return 0;
}