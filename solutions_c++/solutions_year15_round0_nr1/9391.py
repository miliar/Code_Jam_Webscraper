#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int main()
{
	int T,Smax;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		int res=0;
		int current= 0;
		cin >> Smax;
		int ar[Smax+1];
		char temp;
		for(int i=0;i<=Smax;i++)
		{
			cin >>temp;
			ar[i]=temp-'0';
		}
		for(int i=0;i<=Smax;i++)
		{
			//cout << "----------------" << endl;
			//cout << i << " " << current <<" " << ar[i] << " "  << res << endl;
			if( current < i )
			{
				res+= i-current;
				current = i + ar[i];
			}
			else
			{
				current += ar[i];
			}
			//cout << i << " " << current <<" " << ar[i] << " "  << res << endl;
			//cout << "----------------" << endl;
		}
		cout <<  "Case #" <<t <<": "<< res << endl;
	}
	return 0;
}
