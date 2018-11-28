#include<iostream>
#include<fstream>

using namespace std;

long long count_sheep(long long N)
{
	if(N == 0)
		return -1;

	bool marked[10];

	int i;

	for(i = 0;i < 10;i++)	// if a digit is visited
		marked[i] = false;

	int count = 0;	// digits marked until now

	long long temp;

	i = 1;

	while (count != 10)
	{
		temp = N*i;

		long long quo = temp;
		int rem;

		while(quo > 0)
		{
			rem = quo % 10;
			quo = quo / 10;

			if(marked[rem] == false){
				marked[rem] = true;
				count += 1;
			}
		}

		i += 1;
	}

	return temp;
}

void test_cases(int t)
{
	int i;

	long long input;

	ofstream file;
	file.open("output");

	for(i = 1;i <= t; i++)
	{
		cin >> input;

		file << "Case #" << i << ": ";

		long long output = count_sheep(input);

		if(output == -1)
			file << "INSOMNIA" << endl;
		else
			file << output << endl;
	}
}

int main()
{
	int T;
	cin >> T;

	test_cases(T);

	return 0;
}
