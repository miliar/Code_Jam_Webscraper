#include <iostream>
#include <string>

using namespace std;

int main()
{
	std::ios::sync_with_stdio(false);

	int T, iT, Smax, standing, friends;
	string audience;

	cin >> T;

	iT = 0;
	while(iT++ < T)
	{
		cin >> Smax >> audience;
		friends = standing = 0;
		for(int i = 0; i <= Smax; i++)
		{
			if(standing >= i)
			{
				standing += (audience[i] - '0');
			}
			else
			{
				friends += i - standing;
				standing = i + (audience[i] - '0');
			}
		}

		cout << "Case #" << iT << ": " << friends << endl;
	}
	
    return 0;
}
