#include <iostream>
#include <stack>
#include <set>
#include <vector>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>

#define inf (1 << 30)
#define INF (1<<45LL)
#define pb push_back
#define mp make_pair
using namespace std;

typedef pair<int, int> pi;
typedef long long ll;

/*
 * 
 * 		PUCMM PROGRAMMING FORCE
 * 
 * */


int main(){

	ios_base::sync_with_stdio(false);
	
	int t; cin >> t;
	int c = 1;
	while(t--){
		
		
		int ans = 0;
		
		int n;
		string w;
		
		cin >> n >> w;
		
		int sum = 0;
		
		for(int i=0; i <= n; i++){
			
			int act = w[i] - '0';
			
			if(i){
				if(sum < i){
					ans += i - sum;
					sum += i - sum;
				}
			}
			
			sum += act;
			
		}
		
		cout << "Case #" << c++ << ": " << ans << endl;
	}
	return 0;
}
