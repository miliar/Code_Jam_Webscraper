#include<iostream>
using namespace std;

double cwyn, c, f, x;
int mil;

double solve(double time, double prod)
{
	if(mil == 0)return cwyn;
	mil--;
	if(cwyn < (c/prod)+time)return cwyn;
	cwyn = min(cwyn, (x/prod)+time);
	return min(cwyn, solve((c/prod)+time, prod+f));
}

int main()
{
	int n;
	cin >> n;
	cout.precision(7);	
	for(int i = 0; i < n; i++)
	{
		cin >> c >> f >> x;
		cwyn = x/2.0;
		mil = 2000000;
		cout << fixed << "Case #" << i+1 << ": " << solve(0.0, 2.0) << endl;
	}
}
