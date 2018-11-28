#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int n;
	long double C, F, X;
	long double wynik=0.0;
	long double prod = 2.00;
	cin>>n;
	for(int h = 0 ; h < n ; h++)
	{
		wynik=0.0;
		prod=2.0;
		cin>>C>> F>> X;
		while(1)
		{
			if((C*(prod+F))>(X*F))
			{
				break;
			}
			//cout<<(C/prod)<<" ----> "<<(X/(prod+F))<<" ---> \n";
			wynik+=C/prod;
			prod+=F;
		}
		//cout<<X/prod<<"  ";
		printf("Case #%d: %.7Lf\n",h+1, wynik+(X/prod));
	}
}