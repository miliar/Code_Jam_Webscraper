#include<iostream>
#include<cstdio>
#include<algorithm>
#include<set>
using namespace std;

double a[1002],b[1002];
int n, T, ans1, ans2;
set<double> wjj;

int main(){
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);	
	cin >> T;
	for (int h=1; h<=T; h++){
		cout << "Case #" << h << ": ";
		cin >> n;
		for (int i=0; i<n; i++) cin >> a[i];
		for (int j=0; j<n; j++){
			cin >> b[j];
			wjj.insert(b[j]);
		}
		sort(a, a + n); sort(b, b + n);
		ans1 = 0; ans2 = 0;
		for (int temp=n-1, i=n-1; i>=0; --i)
			if (a[temp] > b[i]){
				temp--; ans1++;
			}
		cout << ans1 << " ";
		for (int i=0; i<n; i++)
			if (wjj.upper_bound(a[i]) != wjj.end()){
				wjj.erase(wjj.upper_bound(a[i]));
			} else { 
				wjj.erase(wjj.begin()); ans2++;
			}
		cout << ans2 << endl;
	}
	return 0;
}
