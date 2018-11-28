#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	// your code goes here
	int t;
	double c,curr=2,sum=0,a,b;
	double f;
	double x;
	cin>>t;
	while(t--)
	{
		curr=2;sum=0;
	cin>>c;
	cin>>f;
	cin>>x;

	while(1)
	{
		a=x/curr;
		b=((c/curr)+(x/(curr+f)));

		if(a<b)
		{
			sum=sum+a; break;
		}
		
		else
		{
			sum+=(c/curr);
		}
		
		curr+=f;
	}
	
	cout << fixed << setprecision(7) << sum <<endl;
	}
	return 0;
}