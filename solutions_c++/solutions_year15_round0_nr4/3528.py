#include <iostream>
using namespace std;
#define ll long long 


int main(){
	int t, i=1;
	cin >> t;
	while(t--)
	{
		ll n, a, b, c=0;
		cin >> n >> a >> b;
		if( ( a * b ) % n == 0)
		{
			if(n==1 || n==2){}
			else if(a*b==n)
				c=1;
			else
			{
				if(a==b && 2*a-1<=n)
					c=1;
				else if(a>b && 2*b-1<n)
					c=1;
				else if(2*a-1<n)
					c=1;
			}
		}
		else
			c=1;
		if(c==0)
			cout << "Case #" << i << ": GABRIEL" << endl;
		else
			cout << "Case #" << i << ": RICHARD" << endl;
		i++;
	}
}
