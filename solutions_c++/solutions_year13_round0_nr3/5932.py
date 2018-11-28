#include <iostream>
#include <vector>

using namespace std;

bool ispallin(long long int n)
{
	long long int r=1;
	while ((r*10)<=n) {
		r = r*10;
	}
	while (n) {
		if ((n/r)!=(n%10)) {
			return false;
		}
		n=n%r;
		n = n/10;
		r = r/100;
	}
	return true;
}

int main()
{
	int test_cases;
	scanf("%d",&test_cases);
	vector<bool> pallins(1001,false);
	for (int i=1; (i*i)<=1000; i++) {
		if (ispallin(i)&&ispallin(i*i)) {
			pallins[i*i] = true;
		}
	}
	for (int test_case=1; test_case<=test_cases; test_case++) {
		int a,b;
		scanf("%d %d",&a,&b);
		int res=0;
		for (int i=a; i<=b; i++) {
			if (pallins[i]) {
				res++;
			}
		}
		printf("Case #%d: %d\n",test_case,res);
	}
	return 0;
}
