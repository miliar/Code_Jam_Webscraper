#include <iostream>
#include <vector>

using namespace std;

bool solve(){
	int n; cin>> n;
	n++;
	vector<int> a(n);
	int in; cin>> in;
	for(int i=n-1;i>=0;i--){
		a[i] = in % 10;
		in /= 10;
	}

	int ans = 0;
	for(int i=0;i<n;i++){
		if(i == 0) continue;
		if(a[i-1] < i){
			ans += i - a[i-1];
			a[i-1] = i;
		}
		a[i] += a[i-1];
	}

	cout<< ans<< endl;
	return true;
}

int main(){
	cout.setf(ios::fixed); cout.precision(10);
	int n;
	cin>> n;
	for(int i=0;i<n;i++){
		cout<< "Case #"<< i+1<< ": ";
		solve();
	}
	return 0;
}
