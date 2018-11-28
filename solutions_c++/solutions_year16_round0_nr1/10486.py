#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin >> t;
	while(t--){
		static int cas = 1;
		printf("Case #%d: ",cas++);
		long long x;
		cin >> x;
		if(x == 0)
			cout << "INSOMNIA" << endl;
		else{
			long long y = x;
			set<int>arr;
			while(arr.size() < 10){
				long long z = x;
				while(z){
					arr.insert(z%10);
					z/=10;
				}
				x+=y;
			}
			cout << x - y << endl;
		}
	}
	return 0;	
}