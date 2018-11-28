#include <iostream>

using namespace std;

int main()
{
	int i, testcases;
	long long r,t;
	long long n, rings, temp, requirepaint;

	cin>>testcases;

	for( i=1; i<=testcases; i++)
	{
		cin>>r>>t;

		rings = 0;
		n = 1;
		temp = (r<<1) - 3;
		do
		{
			requirepaint = (n<<2) + temp;

			t = t - requirepaint;
		
			if ( t >= 0 )
				rings++;

			n++;
		} while(t>0);

		cout<<"Case #"<<i<<": "<<rings<<"\n";
	}
	
	return 0;
}
