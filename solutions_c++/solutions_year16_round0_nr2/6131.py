#include <iostream>
#include <string.h>

using namespace std;

int main()
{
	char** s = new char*[100];
	int count,j,f,T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		s[i] = new char[100];
		cin >> s[i];
	}
	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i+1 << ": ";
			
		count = 0;
		while(1)
		{
			f = 0;
			for(j = 0; j<strlen(s[i]);j++)
				if(s[i][j]=='-')
				{
					f = 1;
					break;
				}
			if(f == 0)
			{
				cout << count << endl;
				break;
			}
			if(s[i][0]=='+')
			{
				j = 0;
				while(s[i][j] == '+')
				{
					s[i][j] = '-';
					j++;
				}
			}
			else
			{
				j = 0;
				while(s[i][j] == '-')
				{
					s[i][j] = '+';
					j++;
				}
			}
			count++;
		}
		
		
	}	
	return 0;
}
