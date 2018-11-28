#include<iostream>
#include<algorithm>
#define f first
#define s second
#define mp make_pair
using namespace std;

int ftree[1001];

int fget(int pos) {
	if(pos == 0)
		return 0;
	return ftree[pos] + fget(pos - (pos & (-pos)) );
}

void fadd(int pos) {
	if(pos > 1000)
		return;
	ftree[pos]++;
	fadd(pos + (pos & (-pos)) );
}

int main() {
	int t, n;
	pair<int, int> a[1000];
	cin.sync_with_stdio(false);
	cin >> t;
	
	for(int TCASE=1;TCASE<=t;TCASE++) {
		cin >> n;
		
		for(int i=0;i<n;i++)
			cin >> a[i].f, a[i].s = i+1;
		
		sort(a, a+n);
		reverse(a, a+n);
		int cost=0;
		
		for(int i=0;i<=n;i++)
			ftree[i] = 0;
		
		for(int i=0;i<n;i++) {
			int pos = fget(a[i].s);
			
			cost += min(pos, i-pos);
			fadd(a[i].s);
		}
		
		cout << "Case #" << TCASE << ": " << cost << '\n';
	}
	
	return 0;
}
