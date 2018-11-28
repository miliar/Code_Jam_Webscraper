#include <iostream>
#include <set>

using namespace std;

#define For(i, od, po) for(int (i) = (od); (i) < (po); (i)++)

void solve(int t){
	int x, res;
	cin >> x;
	set<int> s;
	if(x == 0){
		cout << "Case #" << t << ": INSOMNIA\n";
		return;
	}
	res = x;
	while(s.size() < 10){
		int a = res;
		while(a > 0){
			s.insert(a%10);
			a /= 10;
		}
		res += x;
	}
	cout << "Case #" << t << ": " << res - x << endl;
	return;
}

int main(){
	int T;
	cin >> T;
	For(i, 0, T) solve(i+1);
	return 0;
}