#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

typedef unsigned long long ull;
typedef unsigned int uint;



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


	long double r[2], t[2], c[2], v, x;
	int n;

	output << fixed;
	for (int tt = 0; tt < T; ++tt)
	{
		
		input >> n>>v>>x;
		for (int i = 0; i < n; ++i)
			input >> r[i] >> c[i];
		//cin >> r>>c;


		if (n == 1)
		{
			if (c[0] != x)
				output << setprecision(15) << "Case #" << tt + 1 << ": " << "IMPOSSIBLE" << endl;
			else
				output << setprecision(15) << "Case #" << tt + 1 << ": " << v / (r[0]) << endl;
		}
		else{
			if (c[0] == c[1])
			{
				if (c[0] != x)
					output << setprecision(15) << "Case #" << tt + 1 << ": " << "IMPOSSIBLE" << endl;
				else
					output << setprecision(15) << "Case #" << tt + 1 << ": " << v / (r[0] + r[1]) << endl;
			}
			else
			if (c[0] == x)
			{
				output << setprecision(15) << "Case #" << tt + 1 << ": " << v / (r[0]) << endl;
			}
			else
			if (c[1] == x)
			{
				output << setprecision(15) << "Case #" << tt + 1 << ": " << v / (r[1]) << endl;
			}
			else
			{

				t[0] = v / (r[0] * (c[0] - c[1]) / (x - c[1]));
				t[1] = t[0] * (r[0] * (c[0] - x)) / (r[1] * (x - c[1]));

				if (min(t[0], t[1]) < 0)
					output << setprecision(15) << "Case #" << tt + 1 << ": " << "IMPOSSIBLE" << endl;
				else
				{
					if (min(t[0], t[1]) == -0)
						output << setprecision(15) << "Case #" << tt + 1 << ": " << "IMPOSSIBLE" << endl;
					else
						output << setprecision(15) << "Case #" << tt + 1 << ": " << max(t[0], t[1]) << endl;
				}
			}
		}
		//output << "Case #" << t + 1 << ": " << ans << endl;

	}

	input.close();
	output.close();
	//	system("pause");
	return 0;
}
