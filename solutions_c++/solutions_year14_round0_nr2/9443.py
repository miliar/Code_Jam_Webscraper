#include<iostream>
#include<iomanip>
using namespace std;

long double hmin(long double a,long double b,long double c,long double d){
	if(c/d > ((a/d)+(c/(d+b))))
		return (a/d)+hmin(a,b,c,b+d);
	else
		return c/d;
}

int main()
{
	int n,i;
	cin >> n;
	long double a,b,c;
	for(i=1;i<=n;i++){
		cin >> a >> b >> c;
		cout << "Case #" << i << ": ";
		cout << fixed;
		cout.precision(8);
		cout << hmin(a,b,c,2) << endl;
	}
	return 0;
}