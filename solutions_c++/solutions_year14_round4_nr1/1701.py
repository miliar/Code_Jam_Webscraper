#include <iostream>
#include <algorithm>
using namespace std;

int n, x;
int s[10005];

void pulisci(){
	
}

void solve_testcase(){
	cin >> n >> x;
	
	for(int i=0; i<n; i++) cin >> s[i];
	
	if(n == 1) {cout << 1 << '\n'; return;}
	
	sort(s, s+n);
	
	int placed = 0;
	int used = 0;
	
	int i = 0;
	int j = 1; while(j < n-1 && s[i]+s[j] <= x) j++;
	while(i < j){
		while(j > i && s[i]+s[j] > x) j--;
		if(j > i) placed+=2; else placed++;
		used++;
		i++; j--;
	}
	
	cout << used + n - placed << '\n';
}

int main(){
	int t; cin >> t;
	for(int i=1; i<=t; i++){
		cout << "CASE #" << i << ": ";
		solve_testcase();
	}
	return 0;
}
