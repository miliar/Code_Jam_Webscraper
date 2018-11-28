#include <iostream>
#include <math.h>
using namespace std;

class JamCoin
{
    private:
            int divisors[9];
	public:
			void createJamCoins(int J, int N);
			void displayJamCoin(int jamCoin[], int N);
			void makeNextJamCoin(int jamCoin[], int N);
			long int decimalConvert(int base, int jamCoin[], int N);
			int checkPrime(long int decimalValue, int base);
			bool isJamCoin(int JamCoin[], int N);
			void displayDivisors();

};


void JamCoin::displayDivisors()
{
        cout << " ";
        for(int i = 0; i < 9; i++)
        {
            cout << divisors[i] << " ";
        }
        cout << endl;
}

bool JamCoin::isJamCoin(int jamCoin[], int N)
{
    bool isJamCoin = true;
    for(int base = 2; base <= 10 && isJamCoin == true; base++)
    {
        if(checkPrime(decimalConvert(base, jamCoin, N), base) == 1)
        {
            isJamCoin = false;
        }
    }
    return isJamCoin;
}
int JamCoin::checkPrime(long int decimalValue, int base)
{

    int isPrime = 1;
    //cout << decimalValue;
    for(int i = 2; i < decimalValue && isPrime == 1; i++)
    {
        if(decimalValue % i == 0)
        {
            isPrime = 0;
            divisors[base - 2] = i;
        }
        if (i > 100)
        {
            return isPrime;
        }
    }
    //cout << "base: " << base << " decimalValue" << decimalValue << " Prime" << isPrime << endl;
    return isPrime;
}

long int JamCoin::decimalConvert(int base, int jamCoin[], int N)
{
    long int decimalValue = 0;
    int position = N - 1;
    for(int i = 0; i < N; i++)
    {
        decimalValue += pow(base, i) * jamCoin[position];
        position--;
    }
    //cout << "converted to decimal" << endl;
    return decimalValue;
}

void JamCoin::makeNextJamCoin(int jamCoin[], int N)
{
			int carry = 1;
			int sum = 0;
			for(int i = 2 ; i < N && carry!= 0; i++)
			{
				//cout << "going into for loop" << endl;
				sum = jamCoin[N-i] xor carry;
				carry = jamCoin[N-i] * carry;
				jamCoin[N-i] = sum;
			}
			    //cout << "exiting for loop" << endl;
}

void JamCoin::displayJamCoin(int jamCoin[], int N)
{

    for(int i = 0; i < N; i++)
    {
        cout << jamCoin[i];
    }
}

void JamCoin::createJamCoins(int J, int N)
{
    //Create first potential target JamCoin
    int jamCoin[N];
    jamCoin[0] = 1;
    jamCoin[N-1] = 1;
    for(int i = 1; i < N - 1; i++)
    {
        jamCoin[i] = 0;
    }

    int count = 0; //For keeping track of the number of JamCoins I find

    while(count < J)
    {
        //cout << "count : " << count << endl;
        //Check whether tit's a JamCoin, and if it is, store the divisors
        if(isJamCoin(jamCoin, N))
        {
            displayJamCoin(jamCoin, N);
            displayDivisors();
            count++;
            //cout << "I'm here" << endl;
        }
        //cout << "making a jam coin" << endl;
        makeNextJamCoin(jamCoin, N);


    }

}



int main()
{
    JamCoin coin;
    int a[2];
    int T, N, J;
	cin >> T;
    cin >> N;
    cin >> J;

	for(int i = 1; i <= T; i++)
	{
		cout << "Case #" << i << ":" << endl;
		coin.createJamCoins(J, N);
	}

	return 0;
}
