#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

#define rep(i,n) for(int i = 0; i < (n); i++)

void runCase()
{
	int n;
	scanf("%d",&n);
	set<int> a,b,_a,_b;
	double x;
	rep(i,n) {
		scanf("%lf",&x); a.insert( x*1000000);
	}
	rep(i,n) {
		scanf("%lf",&x); b.insert( x*1000000);
	}
	_a = a; _b = b;
	
	int r1,r2;
	r1 = 0;
	r2 = 0;
	
	rep(i,n) {
		int A,B;
		A = *(--a.end());
		B = *(--b.end());
		if(B>A) {
			a.erase(--a.end());
			b.erase(--b.end());
		} else {
			a.erase(--a.end());
			b.erase(b.begin());
			r2++;
		}
	}
	a = _a; b = _b;
	
	rep(i,n) {
	
	//	printf("\n");
	//	for(int c:a) printf("%d,",c); printf("\n");
	//	for(int c:b) printf("%d,",c); printf("\n");
		
		int A,B;
		A = *(a.begin());
		B = *(b.begin());
		if(A>B) {
			a.erase(a.begin());
			b.erase(b.begin());
			r1++;
		} else {
			a.erase(a.begin());
			b.erase(--b.end());
		}
		
	}
	
	
	printf("%d %d\n",r1,r2);
	
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
