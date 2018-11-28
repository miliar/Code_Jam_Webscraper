#include <iostream>
using namespace std;

int main() {
	int a,b,k,t,x,i,j;
	cin >> t;
	for(int test=1;test<=t;++test)
	{
		cin >> a >> b >> k;
		x = 0;
		for(i=0;i<a;++i)
		{
			for(j=0;j<b;++j)
			{
				if((i&j)<k)
					++x;
			}
		}
		cout << "Case #" << test << ": " << x << endl;
	}
	return 0;
}
