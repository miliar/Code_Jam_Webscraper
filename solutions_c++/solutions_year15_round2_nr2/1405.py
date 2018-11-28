#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int r, c;
void print(vector<vector<int> > b){
	for(int i = 0; i < b.size(); ++i){
		for(int j = 0; j < b[i].size(); ++j)
			cout<<b[i][j]<<" ";
		cout<<endl;
	}

}
bool valid(int i, int j){
	return (i>= 0 && i <= r && j >= 0 && j <= c);

}
map<pair<vector<vector<int>>,int>, int> dp;
int solve(vector<vector<int> > b, int x, int y, int p){
	//cout<<p<<endl;
	//print(b);
	if(p == 0) return 0;
	if(dp.count({b, p}) > 0) return dp[{b, p}];
	int sol = 2e9;
	for(int i = x; i < r; ++i)
		for(int j = y; j < c; ++j){
			if(b[i][j]) continue;
			int k = 0;
			vector<vector<int>> bx = b;
			bx[i][j] = 1;
			if(valid(i-1, j) && b[i-1][j] == 1) ++k;
			if(valid(i+1, j) && b[i+1][j] == 1) ++k;
			if(valid(i, j+1) && b[i][j+1] == 1) ++k;
			if(valid(i, j-1) && b[i][j-1] == 1) ++k;
			if(j < c-1){
				sol = min(sol, solve(b, i, j+1, p));
				sol = min(sol, k + solve(bx, i, j+1, p - 1));}
			else {
				sol = min(sol, solve(b, i+1, 0, p));
				sol = min(sol, k + solve(bx, i+1, 0, p - 1));}
		}			
	return dp[{b, p}] = sol;
}
int main (int argc, char const* argv[])
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int t; cin>>t;
	for(int i = 0; i < t; ++i){
		dp.clear(); 
		int n;
		//vector<vector<int> >b;
		cin>>r>>c>>n;
		vector<vector<int>> b(r+1, vector<int>(c+1));
		for(int i = 0; i < r; ++i){
			for(int j = 0; j < c; ++j) b[i][j] = 0;}

		cout<<"Case #"<<(i+1)<<": "<<solve(b, 0, 0, n)<<"\n";
	}
	return 0;
}
