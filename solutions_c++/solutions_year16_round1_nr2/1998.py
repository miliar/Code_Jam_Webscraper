#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <array>
#define PR(x) cout<<#x<<"="<<x<<endl
#define READ2(x,y) scanf("%d %d",&x,&y)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define RP(i,a) for(int i=0;i<a;i++)
#define tr(iter,container) for(auto iter = container.begin();iter!=container.end();iter++) 
#define S(x) cin>>x
#define PRARR(x,n) for(int i=0;i<n;i++) cout<<#x<<"["<<i<<"]= "<<x[i]
#define rd(arr,i,n) for(int i=0;i<n;i++) cin>>arr[i]
#define PB push_back
#define SUM(arr,n,sum) {sum=0;for(int i=0;i<n;i++) sum+=arr[i]; }
#define VC vector
#define CLR(arr) memset(arr,0,sizeof(arr))
#define FILL(arr,val) memset(arr,val,sizeof(arr))
using namespace std;

auto solve(vector<vector<int>> values){
	map<int, int> cnt;
	for(int i=0, sz = values.size();i<sz;++i)
	{
		for(int j=0;j<values[i].size();j++)
		{
			++cnt[values[i][j]]; 
		}
	}
	vector<int> result;
	for(auto var : cnt)
	{
		if (var.second & 1) result.push_back(var.first);
	}
	return result;
}

int main(){
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i){
		cout << "Case #"<<i<<": ";
		int N; 
		cin >> N;
		vector<vector<int>> cntr(2*N - 1, vector<int>(N));
		for (int k = 0 ; k < 2*N -1; ++k){
			for (int j = 0; j < N; ++j){
				cin >> cntr[k][j];
			}
		}
		auto res = solve(cntr);
		for (auto v : res){
			cout << v <<" ";
		}
		cout << endl;
	}
}
