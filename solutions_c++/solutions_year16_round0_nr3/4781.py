#include <bits/stdc++.h>

using namespace std;

unsigned long long getDivisor(unsigned long long n)
{
	if (!(n&1)) return 2;

	double lim = sqrt(n);
	for (unsigned long long i=3; i<=lim; i+=2) if (n%i==0) return i;
	return 0;
}

int main()
{
	int t;
	cin>>t;
	printf("Case #1: \n");
	int n, j;
	cin>>n>>j;

	int count=0;
	unsigned long long mid = 0;
	while(count!=j){
		unsigned long long number = 1 + (mid<<1) + (1<<(n-1));
		bool jam = true;
		string divs;
		for (int base=2; base<=10; base++){
			unsigned long long cur = 0;
			for (int i=0; i<n; i++) cur+=(number&(1<<i)) ? pow(base, i) : 0;
			unsigned long long divisor = getDivisor(cur);
			if (divisor==0) {
				jam = false;
				break;
			}
			else {
				stringstream ss;
				ss<<divisor;
				divs+= ss.str();
				if (base!=10) divs+=" ";
			}
		}
		if (jam){
			stack<int> aux;
			for (int i=0; i<n; i++) aux.push((number&(1<<i))>>i);
			while(!aux.empty()) {
				cout<<aux.top();
				aux.pop();
			}
			cout<<" "<<divs<<endl;
			count++;
		}
		mid++;
	}

	return 0;
}