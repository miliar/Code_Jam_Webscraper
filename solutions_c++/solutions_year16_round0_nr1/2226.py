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
	int n;
	scanf("%d",&n);
	if(n==0) {
		printf("INSOMNIA\n");
		return;
	}
	set<char> cs;
	for(int i = n; ; i+=n) {
		char buf[20]={0};
		sprintf(buf,"%d",i);
		int len = strlen(buf);
		for(int j = 0; j < len; j++) {
			cs.insert(buf[j]);
		}
		if(cs.size()==10) {
			printf("%d\n",i);
			return;
		}
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
