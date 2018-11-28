#include <iostream>
#include <string>
using namespace std;

int main(void)
{
	int T;
	int t;
	int count;
	int N[10];
	
	string s;
	
	cin >> T;
	
	for (t=0;t<T;t++)
	{
		for (int i=0;i<10;i++)
		{
			N[i] = 0;
		}
		cin >> s;
		
		count = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == 'Z')
			{
				count++;
			}
		}
		N[0] = count;
		
		count = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == 'W')
			{
				count++;
			}
		}
		N[2] = count;
		
		count = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == 'U')
			{
				count++;
			}
		}
		N[4] = count;
		
		count = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == 'O')
			{
				count++;
			}
		}
		if ( count > N[0] + N[2] + N[4] )
		{
			N[1] = count-N[0] - N[2] - N[4];
		}
		
		count = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == 'F')
			{
				count++;
			}
		}
		if ( count > N[4] )
		{
			N[5] = count-N[4];
		}
		
		count = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == 'X')
			{
				count++;
			}
		}
		N[6] = count;
		
		count = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == 'V')
			{
				count++;
			}
		}
		if ( count > N[5] )
		{
			N[7] = count-N[5];
		}
		
		count = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == 'G')
			{
				count++;
			}
		}
		N[8] = count;
		
		count = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == 'H')
			{
				count++;
			}
		}
		if ( count > N[8] )
		{
			N[3] = count-N[8];
		}
		
		count = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == 'N')
			{
				count++;
			}
		}
		if ( count > N[1] + N[7] )
		{
			N[9] = (count-N[1]-N[7])/2;
		}
		

		
		cout << "Case #" << t+1 << ": ";
		for (int i=0;i<10;i++)
		{
			for (int j=0;j<N[i];j++)
			{
				cout << i;
			}
		}
		cout << endl;
		
	}
		
	return 0;
}