#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

int reverse(int number);
bool is_square(int n);
string intToString(int number);
int stringToInt(string s);

int main()
{
	ifstream cin;
	cin.open("C-small.in");
	ofstream cout;
	cout.open("C-small_res.txt");

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		int A, B;
		cin >> A >> B;
		int counter = 0;
		for(int i = A; i <= B; i++)
		{
			if(i == reverse(i) && is_square(i))
			{
				int root = (int)sqrt(i);
				if(root == reverse(root)) counter++;
			}
		}

		cout << "Case #" << t << ": " << counter << endl;
	}

	cin.close();
	cout.close();

	return 0;
}

int reverse(int number)
{
	int temp = number;
	int sum = 0;
	while (temp != 0)
	{
		sum *= 10;
		sum += temp % 10;
		temp /= 10;
	}
	return sum;
}

bool is_square(int n)
{
    int temp = floor(sqrt(n));
    return n == temp * temp;
}

string intToString(int number)
{
	ostringstream ss;
	ss << number;
	return ss.str();
}

int stringToInt(string s)
{
	int num;
	istringstream(s) >> num;
	return num;
}
