#include <iostream>

using namespace std;

unsigned long long int CanDraw(unsigned long long int r, unsigned long long int t)
{
	unsigned long long int D = (2*r-5)*(2*r-5)-8*(-2*r+3-t);
	return static_cast<unsigned long long int>((sqrt(D)-(2*r-5.0))/4.0)-1;
}

int main()
{
	int probNum = 0;
	// Problem Num
	cin >> probNum;

	for(int i = 0; i < probNum; ++i)
	{
		unsigned long long int radius = 0;
		unsigned long long int total = 0;
		unsigned long long int ans = 0;
		cin >> radius >> total;
		ans = CanDraw(radius, total);
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
}