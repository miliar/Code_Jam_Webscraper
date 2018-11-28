
#include <cstdio>
#include <iostream>
#include <string>
#include <cstdlib>


int main()
{
	int T,S;
	std::string str;
	std::cin >> T;

	for (int j = 0; j < T ;j++)
	{
		std:: cin >> S;
		int amigos[S+1];
		int audiencia[S+1];
		std::cin >> str;
		if (str.size() == S+1)
		{
			for (int i = 0 ; i < str.size(); i++)
			{
				if ( i == 0)
				{ 
					amigos[i] = 0;
					audiencia[0] = str[0]-48;
				}
				else if ( i > audiencia[i-1] && str[i]-48 > 0) 
				{
					amigos[i]    = i - audiencia[i-1] + amigos[i-1];

					audiencia[i] = (str[i] - 48) + amigos[i] + audiencia[i-1] -amigos[i-1];
				}
				else 
				{
					amigos[i] = amigos[i-1];
					audiencia[i] = str[i] - 48 + audiencia[i-1]; 
				}
			}
			printf("Case #%d: %d\n",j+1,amigos[S]);
		}
		else
		{
			printf("Error\n");
		}
	}




	return 0;
}