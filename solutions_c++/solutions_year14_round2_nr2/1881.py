#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
#include <cmath>
#include <map>


using namespace std;



int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for (int t = 0; t<T; t++){
		int a,b,k;
		cin>>a>>b>>k;
		int ans = 0;
		for (int i =0; i < a; i++) {
			for (int j = 0; j < b; j++) {
				if ((i&j) < k) ans++;
			}
		}
		cout<<"Case #"<<t+1<<": "<<ans<<endl;
	}
	return 0;
}