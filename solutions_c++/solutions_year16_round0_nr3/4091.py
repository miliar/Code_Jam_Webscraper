#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
#include <bitset>
#include <vector>
using namespace std;
bool isPrime(long long num,vector <int>& divisors1);


int main()
{

	int N;
	int numCoins=0;
	int test;
	vector <int> divisors;
	int J;
	cin>>test;
	cin >> N >> J;
	int total=pow(2,N-2);
	vector<long long> combinations(total);
	vector<string> mycombinations(total);
	combinations[0]=0b00000000000000;
	mycombinations[0]="00000000000000";
	string JamCoin;
	int print=0;
	cout << "Case #1:" << endl;
		for(int i=0;i<total;i++)
		{	if(i!=0)
			{
			combinations[i]=combinations[i-1]+1;
			stringstream num;
			num <<std::bitset<14> (combinations[i]); 
			//cout <<     num.str() << endl;
			mycombinations[i]=num.str();
			}
		}
		for(int i=0;i<total;i++)
		{
			JamCoin="1";
			//cout << "J" << JamCoin << endl;
			
			JamCoin=JamCoin+mycombinations[i];
			//cout << "J" << JamCoin << endl;
			
			JamCoin=JamCoin+'1';
			//cout << "possible combination" << JamCoin << endl;
			print++;
			//cout << print << endl;
			int temp;
			long long Coin=0;
			int power=JamCoin.length()-1;
			int count=0;


			for(int base=2;base<=10;base++)
			{
				for(int i=0;i<JamCoin.length();i++)
				{
					
					stringstream str;
					str<< JamCoin[i];
					str>>temp;

					Coin=Coin+temp*pow(base,power);
					power--;
				
				}
				//cout << Coin << " " << base << endl; 
				if(isPrime(Coin,divisors)!=true)
				{
					count++;
					//cout << "not prime" << endl;
			
				}
				else
				{	//cout << "is prime" << endl;
					break;
				}
			//	cout << "prime main masla" << endl;
				if(count==9)
				{
					cout << JamCoin << " ";
					for (int i = 0; i < divisors.size(); i++)
					{
						cout << divisors [i] << " ";
					}
					cout << endl;
					numCoins++;
				}

				Coin=0;
				power=JamCoin.length()-1;
				
			}
			divisors.clear();
			if(J==numCoins)
			{
				break;
			}
		}
		

		
	
	return 0;
}

bool isPrime(long long num,vector <int>& divisors1)
{
	for(int i=2;i<=sqrt(num);i++)
	{	//cout << i << " in function" << endl;
		if(num%i==0)
		{	divisors1.push_back(i);
			return false;
		}
	}

/*
	for(int i=sqrt(num);i<=num/2;i++)
	{
		if(num%i==0)
		{	divisors1.push_back(i);
			return false;
		}
	}

*/	return true;
}

