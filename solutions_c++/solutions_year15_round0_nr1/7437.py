#include<iostream>

int main()
{
	int C;
	std::cin >> C;
	for( int testCase = 1; testCase <= C; testCase++ )
	{
		int maxShy;
		std::cin >> maxShy;
		int friends = 0;
		int totalPeople = 0;
		for( int i = 0; i <= maxShy; i++ )
		{
			char n;
			std::cin >> n;
			int people = (int)(n - '0');

//			std::cout << people << " people with '" << i << "' shyness " << std::endl;			

			if( totalPeople+friends < i && people > 0 )
			{
				//std::cout << i-(totalPeople+friends) << " friends required" << std::endl;
				friends += i - (totalPeople+friends);
			}
			totalPeople += people;
		}
		std::cout << "Case #" << testCase << ": " << friends << std::endl;
			
	}
	return 0;
}
