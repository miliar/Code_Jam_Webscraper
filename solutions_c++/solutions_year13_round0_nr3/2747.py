#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

bool is(int x) {
	char s[101];
	int l=0;
	while(x) {
		s[l] = x%10;
		x/=10;
		l++;
	}
	for(int i = 0; i < l/2; i++) if(s[i] != s[l-1-i]) return false;
	return true;
	
}

int go(int x) {
	int r = 0;
	for(int i = 1; i*i <= x; i++) {
		if(is(i) && is(i*i)) {
			//cout << i << " " << i*i << endl;
			r++;
		}
	}
	return r;
}

void runCase()
{
	int a,b;
	scanf("%d %d",&a,&b);
	a--;
	printf("%d\n",go(b)-go(a));
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
