#include <iostream>
#include<vector>
#include<cmath>
#include<string>
#include<set>
#include<ctime>

using namespace std;

int power(int x, unsigned int y, int p)
{
	int res = 1;    
	x = x % p;  
	while (y > 0)
	{        
		if (y & 1)
			res = (res*x) % p;
		y = y>>1; 
		x = (x*x) % p;
	}
	return res;
}

bool miillerTest(int d, int n)
{

	int a = 2 + rand() % (n - 4);

	int x = power(a, d, n);

	if (x == 1  || x == n-1)
		return true;


	while (d != n-1)
	{
		x = (x * x) % n;
		d *= 2;

		if (x == 1)      return false;
		if (x == n-1)    return true;
	}

	return false;
}

bool isPrime(int n, int k)
{
	if (n <= 1 || n == 4)  return false;
	if (n <= 3) return true;

	int d = n - 1;
	while (d % 2 == 0)
		d /= 2;

	for (int i = 0; i < k; i++)
		if (miillerTest(d, n) == false)
			return false;

	return true;
}

vector<unsigned long long > any2Dec(string str)
{
	vector<unsigned long long> result;
	for(int base=2;base<11;base++)
	{
		unsigned long long genNum=0;
		for(int pos = 0 ; pos < str.size() ; pos++ )
		{
			genNum += ( (  (int) (str[str.size() -1 - pos]-'0')  ) * pow(base,pos) );		
		}
		result.push_back(genNum);
	}
	return result;
}

string genCoin(int size,unsigned long long &last)
{
	unsigned long long temp = last;
	string coin(size,'0');
	coin[0] = '1';
	coin[coin.size()-1] = '1';
	//unsigned long long random = rand() ;
	//cout<<random<<endl;
	for(int i = size - 2 ; i >=1  ; i--)
	{
		coin[i] = (char) ( (temp % 2) + '0' );
		temp /=2;
	}
	last++;
	return coin;
}

vector<int> validateCoin(string coin){

	vector<unsigned long long> numDifVal = any2Dec(coin);
	vector<int> factors;
	for(int i = 0 ; i < numDifVal.size() ; i++ )
	{
		if( isPrime( numDifVal[i], 4))
		{			
			return vector<int>();
		}
		for(int j = 2 ; j < sqrt(numDifVal[i]) ; j++ )
		{
			if( numDifVal[i]%j == 0)
			{
				factors.push_back(j);
				break;
			}
		}
	}
	return factors;
}

int main()
{	
	srand (time(NULL));
	int t;
	cin>>t;
	for(int a=0 ; a < t; a++)
	{
		int b,c;
		cin>>b;
		cin>>c;
		unsigned long long last = 0;
		cout<<"Case #"<<a+1<<":"<<endl;

		set<string>validCoins;	
		while( validCoins.size() <c )
		{
			string coin = genCoin(b,last);
			vector<int> factors;
			while (validCoins.find(coin) == validCoins.end() )
			{
				factors = validateCoin(coin);
				if( factors.size() == 9 )
				{
					validCoins.insert(coin);	
					cout<<coin;
					for(int factor : factors)
					{
						cout<<" "<<factor;
					}
					cout<<endl;
					break;
				}
				else			
				{
					coin = genCoin(b,last);								
					factors = validateCoin(coin);
				}
			} 
		}

	}

	return 0;
}