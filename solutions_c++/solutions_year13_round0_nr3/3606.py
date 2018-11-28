#include<cstdio>
#include<cmath>
#include<vector>

using namespace std;

int main(){
	unsigned long long o[36] = {1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111};
	vector <unsigned long long> v (o, o + 36);
	unsigned long long T;
	scanf("%lld", &T);
	for (unsigned long long t = 0; t<T; ++t) {
		unsigned long long A,B,a,b;
		scanf("%lld %lld", &A, &B);
		a = sqrt(A);
		if (a*a != A) ++a;
		b = sqrt(B);
		++b;
		vector<unsigned long long>::iterator low,low2;
  		low=lower_bound (v.begin(), v.end(), a);
		low2=lower_bound (v.begin(), v.end(), b);
		a = (unsigned long long)(low-v.begin());
		b = (unsigned long long)(low2-v.begin());
		printf("Case #%lld: %lld\n", t+1, b-a);
	}
	return 0;
}
