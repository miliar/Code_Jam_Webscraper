#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <list>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <set>
#include <utility>
#include <stack>

#define rep(i,n) for(int i = 0; i < (n); i++)

using namespace std;

void solve();
void runCase();

void runCase()
{
	long long P,Q,A;
	//cin >> P >> >> Q;
	scanf("%I64d/%I64d",&P,&Q);
	A = 1;
	A <<= 40;
	if(A*P%Q) cout << "impossible" << endl;
	else {
		P = A*P/Q;
		int res=1;
		for(int i = 1; i <= 40; i++) {
			if(P>=(1LL<<i)) res = i;
		}
		cout << (40-res) << endl;
	}
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
	getchar();

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
