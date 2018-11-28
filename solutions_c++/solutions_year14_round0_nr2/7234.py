#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;
const int MNAX = 100000;
double farm[MNAX];
double total[MNAX];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	getchar();

	for (int t=1;t<=test;++t){
		double c,f,x,ans=1000000000;
		cin>>c>>f>>x;

		farm[0] = 0;
		total[0] = x / 2;
		ans = x / 2;

		for (int i=1;i<MNAX;++i){
			farm[i] = farm[i-1] + c / (f*(i-1) + 2);
			total[i] = x / (i*f + 2);

			double ans1 = farm[i] + total[i];
			if (ans1 < ans) ans = ans1;
		}

		cout<<"Case #"<<t<<": ";
		cout.precision(7);
		cout<<fixed<<ans;
		cout<<'\n';
	}

	return 0;
}
