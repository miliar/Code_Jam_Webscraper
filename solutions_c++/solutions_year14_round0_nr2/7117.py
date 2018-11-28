#include <iostream>
using namespace std;
int main(){
	long long n;
	cin >> n;
	cout.precision(7);
	for (int m = 0; m < n; ++m)
	{
		long double speed=2,c,f,x,second=0;
		cin >> c >> f >> x;
		for (long long i = 0; i < x; ++i)
		{
			if(x/speed<((c/speed)+(x/(speed+f)))){
				i=x;
				second+=x/speed;
				speed+=f;}
			else{
				second+=c/speed;
				speed+=f;
			}
		}
		cout << "Case #" << m+1 << ": "<< fixed << second << endl;
	}
}
