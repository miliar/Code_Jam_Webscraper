#include <iostream>
#include <fstream>
#include <string>

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

	int n;
	string s;

	int ans = 0;
	int ar[100] = { 0 };
	for (int t = 0; t < T; ++t)
	{
		input >> s;
		for (int i = 0; i < s.length(); ++i)
			ar[i] = (s[i] == '+' ? 0 : 1);
		
		ans = 0;

		for (int i = s.length()-1; i >= 0; --i)
		{
			if ((ar[i] + ans) % 2)
				++ans;
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
