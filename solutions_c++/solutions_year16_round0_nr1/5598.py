// G_CJ_2016_Q.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <string>
#include <bitset>
using namespace std;


int main()
{
	string dir = "C:\\Users\\Eugene\\Documents\\Visual Studio 2015\\Projects\\G_CJ_2016_Q\\Debug\\";
	string name = "large";
	ifstream fin (dir + name + ".in");
	ofstream fout;
	fout.open(dir + name + ".out");

	if (fin.is_open() && fin.is_open())
	{
		string line;
		getline(fin, line);
		int n = stoi(line);

		for (int i = 0; i < n; i++)
		{
			getline(fin, line);
			string result;
			
			int k = stoi(line);

			if (k == 0)
			{
				result = "INSOMNIA";
			}
			else
			{
				bool done = false;
				
				bitset<10> digits(0);
				int K = k;
				while(!digits.all())
				{
					result = to_string(K);
					
					int tmp_k = K;
					while (tmp_k > 0)
					{
						digits.set(tmp_k % 10);
						tmp_k /= 10;
					}

					K += k;
				}
			}

			fout << "Case #" << i + 1 << ": " << result << endl;
		}

		fin.close();
		fout.close();
	}
    return 0;
}

