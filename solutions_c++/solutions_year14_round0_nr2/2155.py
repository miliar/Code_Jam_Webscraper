#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

double C,F,X;
void runCase()
{
	scanf("%lf%lf%lf",&C,&F,&X);
	//printf("%lf,%lf,%lf\n",C,F,X);
	double p,x,t,t1,t2,t3;
	p = 2.0; x = X;
	t1 = x/p;
	t = 0;
	for(;;) {
		//printf("%lf,",C/p);
		t = t + C/p;
		p += F;
		
		t2 = t + X/p;
		if(t2 < t1) {
			t1 = t2;
		} else {
			break;
		}
	}
	
	printf("%.7lf\n",t1);
}

void runSample()
{
	string input;

	char buf[501] = {0};
	cin.getline(buf,501);

	input = buf;


	printf("%s\n",input.c_str());
}

void solve()
{
	int n;
	scanf("%d",&n);
	//getchar();

	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
		//runSample();
	}
}

int main()
{
	solve();
	return 0;
}
