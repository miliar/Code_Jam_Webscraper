#include <iostream>
#include <math.h>
using namespace std;

bool prime(long int n){
	int stop = 0;
	if(n==1)
		return false;
	else if(n==2)
		return true;
	else{
		for (int i = 2; i <= (int)sqrt(n) && stop == 0; i++)
		{
			if(n%i==0){
				stop = 1;
			}
		}
	}
	if(stop == 1)
		return false;
	return true;
}

long int BaseNtoDec (long int n, int base){
	long int result = 0;
	for (int i = 0; n ; ++i)
	{
		int remaindr = n%10;
		result += remaindr*pow(base,i);
		n /= 10;
	}
	return result;
}

long int DecToBinary(int dec)
{
	long int rem,i = 1,sum = 0;
	do
    {
        rem=dec%2;
        sum=sum + (i*rem);
        dec=dec/2;
        i=i*10;
    }while(dec>0);
    return sum;
}

bool checkJamCoin(long int n){
	int stop = 0;
	for (int i = 2; i <= 10 && stop == 0; ++i)
	{
		long int x = BaseNtoDec(n,i);
		if(prime(x) == true)
			stop = 1;
	}
	if (stop == 1)
		return false;
	return true;
}

long int non_trivial_div(long int n){
	long int result;
	int stop = 0;
	for (int i = 2; i < n && stop == 0; ++i)
	{
		if (n%i==0){
			result = i;
			stop = 1;
		}
	}
	return result;
}

int main(){
	int test_case;
	cin >> test_case;
	int n,j1;
	cin >> n >> j1;
	n = 16;
	j1 = 50;
	cout << "Case #1:" << endl;

	long int init_bin = 1000000000000001;
	//long int init_bin = 100001;
	long int start = BaseNtoDec(init_bin,2);

	for (int i = 0; i < j1 ; start = start + 2)
	{
		long int bin = DecToBinary(start);
		if(checkJamCoin(bin) == false){
			continue;
		}
		else{
			cout << bin << " ";
			for (int j = 2; j <= 10; ++j)
			{
				long int temp = BaseNtoDec(bin,j);
				if(j == 10)
					cout << non_trivial_div(temp) << endl;
				else
					cout << non_trivial_div(temp) << " ";
			}
			i++;
		}
	}

	return 0;
}