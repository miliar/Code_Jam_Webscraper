#include <iostream>
#include <string>

using namespace std;

int main()
{
	int t;
	int s;
	string shylevel;
	int stand = 0;
	int answer = 0;
	
	cin >> t;
	
	for(int i = 0; i < t; i++)
	{
		stand = 0;
		answer = 0;
		cin >> s >> shylevel;
		
		for(int j = 0; j <= s; j++)
		{
			if(stand < j)
			{
				while(stand < j)
				{
					stand++;
					answer++;
				}
			}
			stand += shylevel[j] - '0';
		}
		
		cout << "Case #" << i + 1 << ": " << answer << "\n";
	}
	
	return 0;
}