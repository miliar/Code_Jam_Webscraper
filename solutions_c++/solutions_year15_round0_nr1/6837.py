#include<iostream>
#include<string>


using namespace std;



int main()
{
	int T = 0;
	string str;
	int n = 0;
	int frnds = 0;
	int people = 0;
	cin >> T;

	for (int  i = 1; i <=T; i++)
	{
		frnds = 0;
		people = 0;
		str = "";
		cin >> n;
		cin >> str;

		for (int j = 0; j <= n; j++)
		{
			
			if (people < j)
			{
				while (true)
				{
					frnds++;
					people++;
					if (people >= j)
						break;
				}
			}
			people += str[j] - '0';

			//cout << people << endl;
		}

		cout << "Case #" << i << ": " << frnds<<"\n";
	}

	return 0;
}