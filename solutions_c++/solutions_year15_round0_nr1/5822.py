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
	int ans = 0, cur = 0;
	for ( int t = 0 ; t < T; ++t )
	{
		input >> n >> s;
		//cin >> n >> s;
		ans = 0, cur = 0;
		for ( int i = 0; i < n + 1; ++i )
		{
			if (cur < i)
			{
				ans += (i - cur);
				cur = i;
			}
			cur += s[i] - '0';
		}
		
		output <<"Case #"<<t+1<<": "<< ans << endl;
		//cout << ans;

	}
	//	fclose(input);
	input.close();
	output.close();
	//	system("pause");
	return 0;
}
