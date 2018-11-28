
# include <cstdio>
# include <iostream>
# include <vector>
# include <algorithm>
# include <cmath>
# include <queue>
# include <map>
# include <cstring>
# include <string>
# include <set>

using namespace std;

# define ll long long

const int finalVal = (1<<10) - 1;

int add(ll curr, int mask){
	while(curr != 0){
		int x = curr % 10;
		mask |= (1<<x);
		curr /= 10;
	}
	return mask;
}

int main(){
	
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int ttt;
	cin>>ttt;

	for(int tt = 1; tt <= ttt; tt++){

		ll n;
		cin>>n;

		int mask = 0;
		ll res = -1;

		for(ll mul = 1; mul <= 1000000; mul++){
			ll curr = n * mul;
			mask = add(curr, mask);
			if(mask == finalVal){
				res = curr;
				break;
			}
		}

		cout<<"Case #"<<tt<<": ";
		if(res == -1){
			cout<<"INSOMNIA"<<endl;
		}
		else{
			cout<<res<<endl;
		}

	}

	return 0;
}