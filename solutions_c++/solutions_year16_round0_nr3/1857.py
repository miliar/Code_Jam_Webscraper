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

void go(long long a,long long b,int n) {
	for(int i = n-1; i >=0; i--) {
		if(a&(1LL<<i)) printf("1");
		else  printf("0");
	}
	printf(" ");
	
	cout << b << " ";
	long long x,y,z;
	for(int i = 3; i <= 10; i++) {
		x = 1; y = 0;
		for(int j = 0; j < 17; j++) {
			if(b&(1<<j)) y += x;
			x *= i;
		}
		cout << y;
		if(i<10) cout << " ";
	}
	cout << endl;
}

void runCase()
{
	int n,j;
	scanf("%d%d",&n,&j);
	
	int a;
	a = n/2;
	
	long long x,y,z,i;
	x = 1LL; x <<= (a-1); x += 1LL;
	
	
	
	printf("\n");
	for(y = 0; y < (1LL << a-2);y++) {
		z = x + (y<<1);
		i = (1<<a); i++;
		go(z*i,i,n);
		j--;
		if(j==0) return ;
		
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
