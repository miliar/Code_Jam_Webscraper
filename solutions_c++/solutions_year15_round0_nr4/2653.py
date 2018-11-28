#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");

	//	FILE * input;
	//	input = fopen("input.txt","r");

	int T;

	//	fread(&n, sizeof(int), 1, input);cout<<n<<endl; char cc=getchar();

	input >> T;// cout<<n<<endl;
	//cin >> T;

	int x,r,c;
	string ans;
	
	for (int t = 0; t < T; ++t)
	{
		input >> x >> r >> c;
		if (x == 1)
			ans = "GABRIEL";
		if (x == 2)
		{
			if (r*c % 2)
				ans = "RICHARD";
			else
				ans = "GABRIEL";
		}
		if (x == 3)
		{
			if (r*c % 3)
				ans = "RICHARD";
			else
			{
				if (min(r, c) == 1)
				{
					ans = "RICHARD";
				}
				else
				{
					ans = "GABRIEL";
				}
			}
		}
		if (x == 4)
		{
			if (r*c % 4)
				ans = "RICHARD";
			else
			{
				if (min(r, c) <= 2)
				{
					ans = "RICHARD";
				}
				else
				{
					ans = "GABRIEL";
				}
			}
		}

		output << "Case #" << t + 1 << ": " << ans << endl;
		//cout << ans;

	}
	//	fclose(input);
	input.close();
	output.close();
	//	system("pause");
	return 0;
}
