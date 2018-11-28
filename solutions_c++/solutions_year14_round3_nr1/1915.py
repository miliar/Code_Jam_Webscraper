#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int i=1; i<=t ;i++)
	{
		string k;
		cin >> k;
		int a = k.length();
		int b = k.find("/");
		string c = k.substr(0,b);
		string d = k.substr(b+1, a-b-1);
		long int p=0,q=0;
		long int z = 1;
		for(int j=1; j<=b; j++)
		{
			p+= (c[b-j]-'0')*z;
			z=z*10;
		}
		z=1;
		for(int j=1; j<= a-b-1; j++)
		{
			q+= (d[a-b-1-j]-'0')*z;
			z=z*10;
		}
		
		
		long int pow=1;
		for(int j=1; j<=40 ; j++)
		{
			pow=2*pow;
		}
		long int mid = pow/q*p;
		long int l=0;
		bool pos=true;
		long int j = 1;
		while(q>=j)
		{
			j=j*2;
		}
		if(q*2!=j) pos = false;
		else
		/*{
			while(mid>1)
			{
				mid=mid/2;
				l++;
			}
		}
		l=40-l+1;
		*/
		{
			while(q>p)
			{
				q=q/2;
				l++;
			}
		}
		if(pos)	cout << "Case #" << i << ": "<< l << endl;
		else cout << "Case #" << i << ": impossible\n"; 	
	}
}
