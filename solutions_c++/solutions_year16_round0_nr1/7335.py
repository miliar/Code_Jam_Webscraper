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
	
	int ans = 0;
	for (int t = 0; t < T; ++t)
	{
		input >> n;

		bool b[10] = { 0 };

		int need = 10;

		//cin >> n >> s;
		ans = 0;
		if (n != 0)
		{
			while (true)
			{
				ans += n;
				int copy = ans;
				while (copy){
					if (b[copy % 10] == false)
						--need;
					b[copy % 10] = 1;
					copy /= 10;
				}

				if (need == 0)
				{
					break;
				}
			}
		}

		if (ans==0)
			output << "Case #" << t + 1 << ": " << "INSOMNIA" << endl;
		else
			output << "Case #" << t + 1 << ": " << ans << endl;
		//cout << ans;

	}
	//	fclose(input);
	input.close();
	output.close();
	//	system("pause");
	return 0;
}
