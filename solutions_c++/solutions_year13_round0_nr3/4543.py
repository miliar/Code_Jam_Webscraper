#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
long long a[1200];
int b[10];
int s(3);
bool check(long long x)
{
	int c[10];
	int i(0);
	bool f;
	while (x!=0) {
		++i;
		c[i]=x % 10;
		x=x/10;
	}
	f=true;
	for (int j=1; j<=i; ++j) {
		if (c[j]!=c[i-j+1]) {
			f=false;
			break;
		}
	}
	return f;
}
void work(int l)
{
	long long x(0);
	for (int i=1; i<=l; ++i) {
		x=x*10+b[i];
	}
	for (int i=l; i>=1; --i) {
		x=x*10+b[i];
	}
	x=x*x;
	if (check(x)) {
		++s;
		a[s]=x;
	}
	for (int j=0; j<=9; ++j) {
		x=0;
		for (int i=1; i<=l; ++i) {
			x=x*10+b[i];
		}
		x=x*10+j;
		for (int i=l; i>=1; --i) {
			x=x*10+b[i];
		}
		x=x*x;
		if (check(x)) {
			++s;
			a[s]=x;
		}
		b[l+1]=j;
		if (l<3) {
			work(l+1);
		}
	}
}
int main()
{
	long long t,l,r,j,k;
	a[1]=1;
	a[2]=4;
	a[3]=9;
	for (int i=1; i<=9; ++i) {
		b[1]=i;
		work(1);
	}
	++s;
	sort(a,a+s);
	cin >> t;
	for (int i=1; i<=t; ++i) {
		cin >> l >> r;
		for (j=1; j<s; ++j) {
			if (a[j]>=l) {
				break;
			}
		} 
		--j;
		for (k=j; k<s; ++k) {
			if (a[k]>r) {
				break;
			}
		}
		--k;
		cout << "Case #" << i << ": " << k-j << endl;
	}
	return 0;
}
