
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <stack>
#include <queue>
#include <cctype>
#include <complex>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <cassert>
#include <iomanip>

using namespace std;

#define dump(x)  cout << " "<< #x << " = " << (x) << endl;
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
typedef long long ll;
typedef complex<int> P;
typedef pair<int,int> pii;
const double EPS = 1e-10;
const double PI  = acos(-1.0);




bool solve(){
	int n;
	cin>> n;
	vector<double> a(n), b(n);
	for(int i=0;i<n;i++) cin>> a[i];
	for(int i=0;i<n;i++) cin>> b[i];
	sort(all(a));
	sort(all(b));
	int ans[2] = {0};
	
	for(int k=0;k<2;k++){
		vector<vector<int> > dp(n+1,vector<int>(n+1,0));
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j]);
				if(b[i] < a[j]){
					dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1);
				}
			}
		}
		ans[k] = dp[n][n];
		swap(a,b);
	}
	ans[1] = n - ans[1];
	
	cout<< ans[0]<< " "<< ans[1]<< endl;
	
	return true;
}

int main(){
	cout.setf(ios::fixed);
	cout.precision(10);
	
	int n;
	cin>> n;
	for(int i=0;i<n;i++){
		cout<< "Case #"<< i+1<< ": ";
		solve();
	}
	return 0;
}

 