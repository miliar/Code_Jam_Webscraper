#include <iostream>
#include <string>
using namespace std;


int main() {
	int a,b,c,d,e,i,j,k,f,g;
	bool ok,cek;
	string x,y,z;
	cin >> a;
	for (i=1;i<=a;i++)
	{
		cout << "Case #" << i << ": ";
		cin >> x;
		y = "";
		for (j=0;j<x.size();j++)
		{
			if (x[j] == '-') y = y + '0';
			else y = y + '1';
		}
		b = 0;
		c = x.size();
		ok = true;
		z = y;
		while (ok)
		{
			z = y;
			cek = false;
			for (j=0;j<z.size();j++)
			{
				if (z[j] == '0') cek = true;
			}
			if(!cek)
			{
				ok = false;
				break;
			}
			if (z[c-1] == '0')
			{
				y = "";
				for (j=0;j<c;j++)
				{
					if (z[j] == '1') y = y + '0';
					else y = y + '1';
				}
			b ++ ;
			}
			c--;
		}
		cout << b << "\n";
	}
}