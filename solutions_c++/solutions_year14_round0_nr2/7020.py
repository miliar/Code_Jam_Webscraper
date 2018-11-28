#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int n; cin>>n;
	int cse=1;
	while (cse<=n) {
		double c,f,x; cin>>c>>f>>x;
		double a=2,ans=100000,time=0;

		for (int i = 0; i < 10000001; i++) {
			ans=min(ans,x/a+time);
			time+=c/a;
			a+=f;
		}

		cout<<"Case #"<<cse<<": ";
		printf("%.9lf\n",ans);
		cse++;	
	}
	return 0;
}
