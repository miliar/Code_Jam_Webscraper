#include <iostream>
#include <fstream>
#include <cstdlib>
#include<string>
#include<vector>
#include<cmath>
#include <sstream>

using namespace std;
int char2int(char c);

int cases = 0;
long long N;
string num;
long long temp;
int check[9];

bool done;

std::string::size_type sz = 0;
int main()
{


	freopen("a.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> cases;
	//cin.ignore();

	
	for (int i = 0; i < cases; i++)
	{
		for (int k = 0; k < 10; k++)
		{
			check[k] = 0;
		}
		
		cin >> num;		//cin >> N;
						istringstream buffer(num);
						buffer >> N;
		if ( num == "0")
		{
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
		}
		else
		{
			for (int z = 2;;z++) {
				for (int a = 0; a < num.length(); a++)
				{
					temp = char2int(num[a]);

				}
				temp = (check[0] * check[1] * check[2] * check[3] * check[4] * check[5] * check[6] * check[7] * check[8] * check[9]);
				if (temp == 1)
				{
					cout << "Case #" << i + 1 << ": " << num << endl;
					break;
				}

				//istringstream buffer(num);
				//buffer >> N;
				temp = N * z;
				stringstream ss;
				ss << temp;
				num = ss.str();

			}
		}

	}



	return 0;
}


int char2int(char c)
{
	//cout << check(c);
	switch (c)
	{
	case '0':
		check[0] = 1;
		return 0;
	case '1':
		check[1] = 1;
		return 1;
	case '2':
		check[2] = 1;
		return 2;
	case '3':
		check[3] = 1;
		return 3;
	case '4':
		check[4] = 1;
		return 4;
	case '5':
		check[5] = 1;
		return 5;
	case '6':
		check[6] = 1;
		return 6;
	case '7':
		check[7] = 1;
		return 7;
	case '8':
		check[8] = 1;
		return 8;
	case '9':
		check[9] = 1;
		return 9;
	default:
		return -2;
	}
}