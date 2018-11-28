#include <bits/stdc++.h>
typedef long long int llu;
using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	llu tt,n;
	cin >> tt;
	for(llu i=1; i<=tt; ++i){
		set <llu> s;
		cin >> n;
		if(n == 0){
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
			continue;
		}
		for(llu j=1; ; ++j){
			llu temp = n*j;
			while(temp != 0){
				s.insert(temp%10);
				temp /= 10;
			}
			if(s.size() == 10){
				cout << "Case #" << i << ": " << n*j << endl;
				break;
			}
		}
	}
	return 0;
}
