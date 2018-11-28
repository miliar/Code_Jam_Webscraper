#include <iostream>

using namespace std;

int main()
{
	int T = 0;
	cin >> T;
	for(int t=0;t<T;t++)
	{
		int inner = 0, paint = 0;
		cin >> inner >> paint;

		int circles = 0;
		int x = 1;
		while(1)
		{
			int reqd = (2*inner)+x;
			if(reqd > paint)
				break;
			else
			{
				paint = paint - reqd;
				circles++;
			}
			x = x+4;
		}
/*
		for(int i=inner+1;;i+=2)
		{
			int a = i*i;
			int b = (i-1)*(i-1);
			if(a-b < paint)
			{
				circles++;
				paint = paint - (a-b);
			}
			else
			{
				break;
			}
		}
*/

		cout << "Case #" << (t+1) << ": " << circles << endl;

	}
	return 0;
}
