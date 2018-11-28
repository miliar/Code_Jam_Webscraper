#include <iostream>
#include <fstream>
#include <string>
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

	int n;
	
	long long ans1 = 0, ans2 = 0;
	int M = 0;
	int* m;
	for (int t = 0; t < T; ++t)
	{
		ans1 = 0; ans2 = 0; M = 0;
		input >> n;
		//cin >> n;
		m = new int[n];

		input >> m[0];
		//cin >> m[0];
		for (int i = 1; i < n; ++i)
		{
			input >> m[i];
			//cin >> m[i];

			if (m[i] < m[i - 1])
			{
				ans1 += (m[i - 1] - m[i]);
				if (m[i - 1] - m[i]>M)
				{
					M = m[i - 1] - m[i];
				}
			}
		}

		for (int i = 1; i < n; ++i)
		{
			ans2 += min(m[i - 1], M);
		}

		output << "Case #" << t + 1 << ": " << ans1<<" "<<ans2 << endl;
		//cout  << "Case #" << t + 1 << ": " << ans1 << " " << ans2 << endl;;

		delete[] m;
	}
	//	fclose(input);
	input.close();
	output.close();
	//	system("pause");
	return 0;
}
