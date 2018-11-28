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

int go(char *s,int n,char t) {
	if(n<0) return 0;
	char x = '-';
	if(t==x) x = '+';
	
	if(s[n]==t) {
		return go(s,n-1,t);
	} else {
		return 1 + go(s,n-1,x);
	}
}

void runCase()
{
	char s[101] = {0};
	scanf("%s",s);
	int len = strlen(s);
	printf("%d\n",go(s,len-1,'+'));
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
