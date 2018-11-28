#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <cmath>
#include <string>
#include <sstream>

using namespace std;

string convertInt(long long int number)
{
	stringstream ss;
	ss << number;
	return ss.str();
}

bool test(long long int n)
{
	string str;
	long long int temp = 0;
	str = convertInt(n);
	for (int k = 0; k < str.length(); k++)
		{
		temp ^= (str[k] - '0');
		}
	if (str.length()%2 == 1 && temp == (str[str.length()/2]) - '0')
		return true;
	if (str.length()%2 == 0 && temp == 0)
		return true;
	return false;
}

int main()
{
	ifstream inData;
	ofstream outData;
	inData.open("C-small-attempt0.in.txt");
	outData.open("output.txt");
	
	long long int T, A, B, j, k, s, y;
	double temp;
	inData >> T;
	string str;
	for (int i = 0; i < T; i++)
		{
		y = 0;
		inData >> A >> B;
		temp = 0;
		for (j = A; j <= B; j++)
			{
			if (!test(j)) continue;
			temp = sqrt(j);
			if (fmod(temp, 1) != 0) continue;
			if (test(static_cast<long long int>(temp)))
				{
				y++;
				}
			}
		
		
		outData << "Case #" << i + 1 << ": " << y << endl;
		}
	
	inData.close();
	outData.close();
}





