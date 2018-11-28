#include<iostream>
#include<fstream>
#include<string>

int main()
{
	std::ifstream in;
	std::ofstream out;
	in.open("input.txt");
	out.open("output.txt");

	int t, n, i, j, ans=0;
	std::string input;

	in >> t;

	for (i = 0; i < t; ++i)
	{
		in >> input;
		for (j = input.size() - 1; j >= 0; --j)
		{
			if (input[j] == '-')
			{
				for (int k = j; k >= 0; --k)
				{
					if (input[k] == '-')
						input[k] = '+';
					else if (input[k] == '+')
						input[k] = '-';

				}
				ans++;
			}
			else
				continue;
		}
		out << "Case #" << i + 1 << ": " << ans << std::endl;
		ans = 0;
	}

	in.close();
	out.close();
	return 0;
}



/*
int main()
{
	std::ifstream in;
	std::ofstream out;
	in.open("input.txt");
	out.open("output.txt");

	int t, n, temp, ans, k=0, i, j;
	bool x[10] = { false, };

	in >> t;
	for ( i = 0; i < t; ++i)
	{
		in >> n;
		temp = n;
		k = 1;
		for (int i = 0; i < 10; ++i)
		{
			x[i] = false;
		}
		if (n == 0)
		{
			out << "Case #" << i+1 << ": INSOMNIA" << std::endl;
			continue;
		}
		while (1)
		{
			temp = n*k;
			while (temp > 0)
			{
				x[temp % 10] = true;
				temp /= 10;
			}
			for ( j = 0; j < 10; ++j)
			{
				if (x[j] == false)
					break;
			}
			if (j == 10)
			{
				out << "Case #" << i+1 << ": " << n*k <<  std::endl;
				break;
			}
			k++;
		}

	}

	in.close();
	out.close();
	return 0;
}


*/