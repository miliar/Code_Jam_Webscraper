// G_CJ_2016_1C.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <string>
#include <bitset>
#include <vector>
#include <algorithm>
using namespace std;



int main()
{
	string dir = "C:\\Users\\Eugene\\Documents\\Visual Studio 2015\\Projects\\G_CJ_2016_Q\\Debug\\";
	string name = "A-large";
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
			int k = stoi(line);
			vector<int> m;

			getline(fin, line);

			int start = 0;
			int curr = 0;
			for (int j = 0; j < line.length(); j++)
			{
				if (line[j] == ' ')
				{
					int n = stoi(line.substr(start, curr - start));
					m.push_back(n);
					start = curr + 1;
					curr++;
				}
				else
				{
					curr++;
				}
			}
			m.push_back(stoi(line.substr(start, curr - start+1))); //A-N

			int max = -1;
			int max_id = -1;
			int min = 10000;
			int min_id=-1;

			for (int j = 0; j < k; j++)
			{
				if (m[j] > max)
				{
					max = m[j];
					max_id = j;
				}
			}
			int max2 = -1;
			int max2_id = -1;
				
			for (int j = 0; j < k; j++)
			{
				if (j == max_id)
					continue;
				if (m[j] > max2)
				{
					max2 = m[j];
					max2_id = j;
				}
			}

			for (int j = 0; j < k; j++)
			{
				if (j == max_id || j == max2_id)
					continue;
				if (m[j] < min)
				{
					min = m[j];
					min_id = j;
				}
			}

			string result = "";

			while (m[max_id] > m[max2_id])
			{
				if ( m[max_id] - m[max2_id] > 1)
				{
					result += ('A' + max_id);
					result += ('A' + max_id);
					m[max_id] -= 2;
				}
				else
				{
					if (k > 2)
					{
						result += ('A' + max_id);
						result += ('A' + min_id);
						m[max_id]--;						
						m[min_id]--;
					}
					else
					{
						result += (char)('A' + max_id);
						m[max_id]--;
					}
				}
				result += ' ';
			}
			bool changes = true;

			while (changes)
			{
				changes = false;
				for (int j = 0; j < k; j++)
				{
					if (j == max_id || j == max2_id || m[j]==0)
						continue;
					
					result += (char)('A' + j);
					result += " ";
					m[j]--;
					changes = true;
				}
			}

			while (m[max_id] > 0)
			{
				result += (char)('A' + max_id);
				result += (char)('A' + max2_id);
				m[max_id]--;
				m[max2_id]--;
				if (m[max_id] > 0)
					result += " ";
			}

			fout << "Case #" << i + 1 << ": " << result << endl;
		}

		fin.close();
		fout.close();
	}
	return 0;
}



int main_QB()
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


int main_QA()
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

