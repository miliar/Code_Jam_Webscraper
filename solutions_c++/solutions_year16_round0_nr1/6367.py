#include <iostream>
#include <set>
using namespace std;

int main(){
	ios::sync_with_stdio(false); cin.tie(0);\
	int n,t;
	set<int> s;
	cin >> t;
	int k = 1;
	while(t--){
	cin >> n;
	if(n == 0){
		
		cout << "Case #"<<k++<< ": " <<"INSOMNIA" << endl;
		continue;
	}
	s.clear();
	int i = 1;
	while(true){
		int a = n*i;
		int ans = n*i;
		while(a > 0){
			int x = a % 10;
			a /= 10;
			s.insert(x);
		}
		i++;
		if(s.size() == 10){
			cout << "Case #"<<k++<< ": " <<ans<< endl;
		
			break;
		}
	}
	}
	return 0;
}
