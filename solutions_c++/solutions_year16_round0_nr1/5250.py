#include <bits/stdc++.h>

using namespace std;

int main(){
	int n;
	long long x;
	set <int> s;
	cin >> n;
	long long a;
	for (int i=0;i<n;i++){
		cin >> a;
		if (a==0){
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		}
		s.clear();
		for (int j=1;j<1000;j++){
			x=a*j;
			while(x>0){
				s.insert(x%10);
				x/=10;
			}
			if (s.size()==10){
				cout << "Case #" << i+1 << ": " << a*j << endl;
				break;
			}
		}
	}
}