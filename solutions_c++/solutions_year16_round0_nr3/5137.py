#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <bitset>
using namespace std;
/*
bool allPlus(string str)
{
	for (int x = 0; x < str.length(); x++)
	{
		if (str[x] == '-')
			return false;
	}
	return true;
}
string flipAndChange(string str, int ePos)
{
	string ns = "";
	//reverse
	for (int j = ePos; j >= 0; j--)
	{
		ns += str[j];
	}
	//cout << "NS: " << ns << endl;
	cout << "NS COUNT: " << ns.length() << endl;
	//change signs
	for (int j = 0; j < ns.length(); j++)
	{
		if (ns[j] == '+')
			ns[j] = '-';
		else
			ns[j] = '+';
	}
	cout << "NS: " << ns << endl;
	cout << "str before: " << str << endl;
	for (int x = 0; x < ns.size(); x++)
	{
		str[x] = ns[x];
	}
	cout << "str after : " << str << endl;
	return str;
}


int countManouvers(string str)
{
	int man = 0;
	while (allPlus(str) == false)
	{
		int ePos = str.length()-1;
		bool minusFlag = false;
		for (int x = 0; x < str.length(); x++)
		{
			//find first plus to activate ePos
			if (str[x] == '-'){
				minusFlag = true;
			}
			if (str[x] == '+' && minusFlag == true){
				ePos = x;
				break;
			}

			
			
			
		}
		str = flipAndChange(str,  ePos);
		man++;
		//break;
	}
	return man;
}
*/

unsigned long long convertToBase(string number, int base)
{
	vector<long long> nums;
	int ctr = 0;
	for (long long x = number.length()-1; x >=0; x--)
	{
		unsigned long long d = -1;
		if (number[x] == '0')
			d = 0;
		else
			d = 1;
		long long digit = (unsigned long long)pow(base, ctr)*d;
		ctr++;
		nums.push_back(digit);
	}
	//now sum over it
	unsigned long long  sum = 0;
	for (int x = 0; x < nums.size(); x++)
	{
		sum += nums[x];
	}
	return sum;
}
bool is_prime(unsigned long long number)
{
	if (number <= 1)
		return false;
	else if (number <= 3)
		return true;
	else if (number % 2 == 0 || number % 3 == 0)
		return false;
	unsigned long long i = 5;
	while (i*i <= number)
	{
		if (number%i == 0 || number % (i + 2) == 0)
			return false;
		i = i + 6;
		
	}
	return true;
}
//make number smallest as you can
unsigned long long div(unsigned long long number)
{
	
	for (unsigned long long x = 2; x <= number; x++){
		if (number%x == 0 )
			return x;
	}
	return -1;
}
bool isJamCoin(string number)
{
	if (number[0] == '1' && number[number.length() - 1] == '1')
		return true;
	return false;
}
vector<string> generateJamCoins(int n,int j)
{
	vector<string> coins;
	int start = 0,end=0;
	int ctr = 0;
	if (n == 6){
		start = 33;
		end = 64;
	}
	else if (n == 16)
	{
		start = 32769;
		end = 65536;
	}
	else if (n == 32){
		start = 2147483649;
		end = 4294967295;
	}
	for (int x = start; x < end; x++)
	{
		string s = bitset< 64 >(x).to_string(); // string conversion
		
		if (isJamCoin(s.substr(64 - n, n)))
		{
			coins.push_back(s.substr(64 - n, n));
			ctr++;
			if (ctr >= j * 2)
				break;
		}
	}
	return coins;
}
int main()
{
	ifstream inFile("C-small-attempt0.in");
	ofstream output("outputSmall.txt");

	int T;

	inFile >> T;
	//cin >> T;
	//cin.ignore();
	for (int x = 0; x < T; x++){
		int N, J;
		//inFile >> n;

		inFile >> N >> J;
		output << "Case #" << x + 1 << ":"  << endl;
		
		
		vector<string> jamCoins = generateJamCoins(N,J);
		int combs = 0;
		//for (int i = 0; i < jamCoins.size(); i++){
		//	cout << jamCoins[i] << endl;
		//}
		
		for (int i = 0; i < jamCoins.size(); i++){
			vector<unsigned long long> results;
			bool primeFound = false;
			string jamCoin = jamCoins[i];
			for (int j = 2; j <= 10; j++){
				unsigned long long number = convertToBase(jamCoin, j);
				if (is_prime(number)){
					primeFound = true;
					break;
				}
				results.push_back(div(number));
				//cout << "n " << n << ": " << number << endl;
			}
			if (primeFound == false)
			{
				output << jamCoin << " ";
				for (int x = 0; x < results.size(); x++){
					output << results[x];
					if (x != results.size()-1)
						output<< " ";
				}
				output << endl;
				combs++;
			}
			
			if (combs == J)
				break;
		}
		//cout << "Case #" << x + 1 << ": " << convertToBase(n,j) << endl;
	}
	return 0;
}

