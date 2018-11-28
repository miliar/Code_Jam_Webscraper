// G_CJ_2016_Q.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <string>
#include <bitset>
using namespace std;

long long get_num(long n, int base)
{
	long long res = 0;
	long long mult = 1;

	while (n > 0)
	{
		res += (n % 2)*mult;
		mult *= base;
		n /= 2;
	}
	return res;
}

long long get_factor(long long n)
{
	long long nsqrt = sqrt(n);
	for (int i = 2; i < nsqrt; i++)
	{
		if (n%i == 0)
			return i;
	}

	return -1;
}

int main()
{
	string dir = "C:\\Users\\Eugene\\Documents\\Visual Studio 2015\\Projects\\G_CJ_2016_Q\\Debug\\";
	string name = "C-small";
	ofstream fout;
	fout.open(dir + name + ".out");

	if (fout.is_open())
	{
		string line;

		int N = 16;
		int J = 50;

		fout << "Case #1:" << endl;

		long N2 = 1+ (1 << N-1 );

		for (int i = 0; i < J; i++)
		{
			bool found = false;
			while (!found)
			{
				long long num[11];
				found = true;
				num[0] = get_num(N2, 10);
				for (int j = 2; j <= 10; j++)
				{
					long long m_tmp = get_num(N2, j); 					
					long long mult_tmp = get_factor(m_tmp); 
					if (mult_tmp < 0) 
					{ 
						found = false;
						break; 
					}
					else
					{
						num[j] = mult_tmp;
					}
				}
				if (found)
				{
					fout << num[0] << " ";
					for (int i = 2; i < 10; i++)
						fout << num[i] << " ";
					fout << num[10] << endl;
				}
				N2 += 2;
			}
		}

		fout.close();
	}
	return 0;
}


int main_B()
{
	string dir = "C:\\Users\\Eugene\\Documents\\Visual Studio 2015\\Projects\\G_CJ_2016_Q\\Debug\\";
	string name = "B-large";
	ifstream fin(dir + name + ".in");
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
			int result=0;

			char prev = '+';
			for (int i = line.size()-1; i >=0; i--)
			{
				if(line[i] != prev)
				{ 
					result++;
					prev = line[i];				
				}
			}

			fout << "Case #" << i + 1 << ": " << result << endl;
		}

		fin.close();
		fout.close();
	}
	return 0;
}


int main_A()
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

