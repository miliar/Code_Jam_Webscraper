#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;
const int MNAX = 100;


int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	getchar();

	for (int t=1;t<=test;++t){
		int ans = 0;
		int a,b,k;
		cin>>a>>b>>k;
		for (int i=0;i<a;++i){
			for (int j=0;j<b;++j){
				if ((i&j) < k) ans++;
			}
		}

		cout<<"Case #"<<t<<": "<<ans<<'\n';
	}

	return 0;
}
