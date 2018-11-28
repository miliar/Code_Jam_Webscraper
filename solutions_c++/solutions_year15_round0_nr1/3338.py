#include <iostream>
#include <vector>
#include <string>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <cstdio>
#define infin 2147483647
#define pb push_back
#define rs resize
#define mp make_pair
#define sz(x) int((x).size())
#define vv(x) vector<vector<x> >
#define all(x) (x).begin(), (x).end()
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;

int main(){		// 
	int tests;
	cin>>tests;
	for(int t=0; t<tests; t++){
		int n, sum = 0, svar = 0;
		string a;
		cin>>n>>a;
		for(int i=0; i<=n; i++){
			if(sum < i) svar++, sum++;
			sum += (a[i]-'0');
		}
		cout<<"Case #"<<t+1<<": "<<svar<<endl;
	}
}