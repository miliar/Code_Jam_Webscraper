#include <iostream>
#include <bitset>
#include <set>

using namespace std;

typedef long long ll;

int flag = 0;
const int comp = 1023;

void extract(int n){
	while(n != 0){
		flag |= 1 << (n % 10);
		n /= 10;
	}
}

int main(){
	int t;
	cin >> t;
	for(int i = 1; i <= t; i ++){
		set <int> s;
		set <int> :: iterator it;
		flag = 0;
		int n, j = 1;
		cin >> n;
		cout << "Case #" << i << ": ";
		while(flag != comp){
			int m = n * j;
			if(s.find(m) != s.end()){
				cout << "INSOMNIA\n";
				break;
			}
			extract(m);
			s.insert(m);
			j ++;
		}
		if(flag == comp)
			cout << n * (j - 1) << endl;
	}
	return 0;
}

