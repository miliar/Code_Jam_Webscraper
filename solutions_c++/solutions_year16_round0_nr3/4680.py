#include <iostream>
#include <unordered_map>
#include <cmath>
using namespace std;

unordered_map<long int, int> listOfPrimes(0);

int isPrime(long int N)
{
 	//returns first divisor or 0 if number is prime
    if(listOfPrimes[N] != 0 && listOfPrimes[N] != 1)
    {
        return listOfPrimes[N];
    }
 	if(listOfPrimes[N] == 1)
 	{
 		return 0;
 	}
    if(N%2 == 0)
    {
        listOfPrimes[N] = 2;
        return 2;
    }
    else if(N%3 == 0)
    {
        listOfPrimes[N] = 3;
        return 3;
    }
	for(int i = 5; i<sqrt(N); i = i+6)
	{
		if(N%i == 0 )
		{
            listOfPrimes[N] = i;
			return i;
		}
        else if(N% (i+2) == 0)
        {
            listOfPrimes[N] = i+2;
            return i+2;
        }
	}
    listOfPrimes[N] = 1;
	return 0;
}

int checkBase(string N, int base)
{
	long int num = 0;
	for(int i = N.size()-1; i>= 0; i--)
	{
		num += ((N[i]-'0') * pow(base, N.size()-1 - i));
	}
    //return num;
	return isPrime(num);
}

void incrementBinary(string& s)
{
	bool changed = false;
	int i;
	for(i = s.size()-1; i> 0; i--)
	{
		if(s[i] == '0')
		{
			s[i] = '1';
			changed = true;
			break;
		}
	}
	for(i = i+1 ; i<s.size()-1; i++)
	{
		s[i] = '0';
	}
}

void findJamCoins(int l, int num)
{
	int numJCoinsFound = 0;
	int arrOfDivisors[11]; //store divisors from 2 through 10. 2 extra wasted spots
	string bin = "1";
	for(int i = 1; i<l-2; i++)
	{
		bin+= "0";
	}
	bin+= "11";
	bool found = false;
	//start with binary representation of 2;
	while(numJCoinsFound<num)
	{
		for(int i = 2; i<= 10; i++)
		{
			int result = checkBase(bin, i);
			if( result == 0)
			{
				found = false;
				break;
			}
			else
			{
				found = true;
				arrOfDivisors[i] = result;
			}
		}
		if(found == true)
		{
			numJCoinsFound++;
			found = false;
			cout<<bin<<" ";
			for(int i = 2; i<= 10; i++)
			{
				cout<<arrOfDivisors[i]<<" ";
			}
			cout<<endl;
		}
		incrementBinary(bin);
	}
}

int main()
{
	int T;
	cin>>T;
	int numStrings;
	int length;
	cin>>length>>numStrings;
	cout<<"Case #1:"<<endl;
	findJamCoins(length, numStrings);
	/*string s = "100001";
	while( s !="111111")
	{
		incrementBinary(s);
		cout<<s<<endl;
	}*/
    
}