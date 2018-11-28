#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
#include <string.h>
#include <fstream>
#include <queue>
#include <hash_map>
using namespace std;

void loadFile(int & N, int &j)
{
	int total = 0;
	string line, parsing="";
	ifstream myfile("small_input.txt");
	int i = 0;
	size_t ss;


	if (myfile.is_open())
	{
		while (!myfile.eof())
		{
			getline(myfile, line);

			if (line == "")
				continue;
			if (i != 0)
			{
				for (int index = 0; index < line.size(); index++)
				{
					if (line[index] == ' ')
					{
						N=stoi(parsing);
						parsing.clear();
					}

					else
					{
						parsing.push_back(line[index]);
					}
				}

				j = stoi(parsing);
			}
			i++;
		}
		myfile.close();
	}
}

void saveFile(vector<string> & out, int j)
{
	ofstream myfile("small_output.txt");

	if (myfile.is_open())
	{
		myfile << "Case #1:\n";
		for (int i = 0; i < out.size(); i++)
		{
			myfile << out[i];
			if (i == out.size() - 1 || i==(j-1))
			{
				break;
			}
			myfile << endl;
		}
		myfile.close();
	}

}

int getDivisor(long long int a)
{
	/*for (int i = 2; i < sqrt(value)+1; i++)
	{
		if ((value%i) == 0)
		{
			return i;
		}
	}

	return -1;*/

	long long int answer = 2;
	int c = sqrt(a) + 1;
	while (answer < c)
	{

		if (a%answer == 0)
		{
			return answer;
		}
		answer++;
	}
	return -1;
}

long long int getDecimalfromBase(int base, string number)
{
	long long int value=0;


	for (int i = number.size() - 1, j=0; i >= 0; i--, j++)
	{
		long long int temp=(pow(base, j)*(number[i]-48));
		value += temp;
	}


	return value;
}

vector<string> getCombinations(string coin)
{
	vector<string> answers;
	
	int size = pow(2,coin.size() - 2);

	for (int i = 0; i < size; i++)
	{
		answers.push_back(coin);
	}

	int myCounter = 0;
	char bit = '0';

	for (int i = coin.size() - 2, k=0; i > 0 ; i--, k++)
	{
		myCounter = 0;
		bit = '0';

		for (int j = 0; j < size; j++)
		{
			
			if (myCounter == pow(2,k))
			{
				myCounter = 0;
				
				if (bit == '0')
					 bit = '1';

				else bit = '0';
			}
			myCounter++;
			answers[j][i] = bit;
			
		}

	}
	
	return answers;
}

string doit(string s)
{
	string ans = "";
	vector<int> divs;

	for (int i = 2; i <= 10; i++)
	{
		long long int num=getDecimalfromBase(i, s);
		int d = getDivisor(num);

		if (d == -1)
			return "";

		else divs.push_back(d);
	}

	ans += s;
	for (int i = 0; i < divs.size(); i++)
	{
		ans += " " + to_string(divs[i]);
	}

	return ans;
}

vector<string> getRow(int N, int j)
{
	vector<string> allAnsTemp;
	vector<string> allCombs;
	string jamcoin = "";

	for (int i = 0; i < N; i++)
	{
		if (i == 0)
		{
			jamcoin.push_back('1');
		}

		else if (i == N - 1)
		{
			jamcoin.push_back('1');
		}

		else
		{
			jamcoin.push_back('0');
		}
	}

	//first get all the combinations possible
	allCombs = getCombinations(jamcoin);

	int stupidCounter = 0;
	//iterate through all of them to get the jamCoins.
	for (int i = 0; i < allCombs.size() ; i++)
	{	

		string reply = doit(allCombs[i]);
		if (reply == "")
		{
			//not a jamcoin
		}
		else
		{
			
			if (stupidCounter == (j))
				break;
			stupidCounter++;
			allAnsTemp.push_back(reply);
		}
	}

	return allAnsTemp;
}

int main()
{
	int N, j;
	vector<string> allAns;	
	loadFile(N,j);

	allAns = getRow(N, j);
	saveFile(allAns,j);

	return 0;
}
