#include <iostream>
#include <string>
#include <cmath>
#include <math.h>
using namespace std;

long long div[10];
int *bin;
int n;
int count;

bool isPrime(long long n1, int base)
{
    int flag = 0;
    if(n1 % 2 == 0)
    {
    	flag = 1;
		div[base-2] = 2;
    }
    else
    {
	    for (long long i = 3; i <= sqrt(n1); i += 2)
	    {
	    	if(n1 % i == 0)
			{
			  flag = 1;
			  div[base-2] = i;
			  break;
			}
		}
	}
	//cout<< "n= "<< n1 << " flag= "<<flag<< " base= "<<base<<endl;
	if (flag == 0)
	    return true;
	else
		return false;
}

bool isValid(long long num, long long copy_num,int base)
{
	if(!(isPrime(num,base)))
	{
		//cout << "num= "<< num << " copy_num= "<< copy_num <<" isvalid LSB "<< (num & 1)<< " MSB "<< (num &  copy_num)<<endl;
		if((num & 1) == 1 && (num & copy_num) == copy_num)
		{
			return true;
		}
	}
	return false;
}

void binary(long long num)
{
	int x = 0;
	while(num != 0)
	{
		int rem = num % 2;
		num = num / 2;
		bin[x] = rem;
		x++;
	}
}

long long baseconvert(int base)
{
	long long sum =0;
	long long mul = 1;
	for(int i = 0; i < n; i++)
	{
		sum += bin[i] * mul;
		mul = mul * base;
	}
	//cout << "base= "<< base << " value= "<<sum<< endl;
	return sum;
}

int main()
{
	int tc;
	cin >> tc;
	for(int t = 1; t <= tc; t++)
	{
		cin >> n >> count;
		bin = new int[n];
		for(int i = 0; i < n; i++)
		{
			bin[i] = 0;
		}
		cout << "Case #"<< t <<": "<<endl;
		int base = 2;
		long long num = pow(base, n-1);
		long long  copy_num = num;
		long long num1 = pow(base, n) -1;
		while(num <= num1 && count > 0)
		{
			//cout << "Count= "<< count<< " num= "<< num<<endl;
			for(int i = 0; i < 9; i++)
			{
				div[i] = 0;
			}
			//cout << "num= "<< num<< " num1= "<< num1<< " isPrime(num)= "<< isPrime(num, base)<<" isValid(num)= "<< isValid(num,copy_num,base)<<endl;
			int flag = false;
			if(isValid(num, copy_num, base))
			{
				binary(num);
				for(int i = base+1; i <= 10; i++)
				{
					long long num2 = baseconvert(i);
					if((isPrime(num2, i)))
					{
						flag = true;
						break;

					} 					
				} 
				if(flag == false)
				{
					for(int i = n-1; i >= 0; i--)
					{
						cout << bin[i];
					}
					cout <<" ";
					for(int i = 0; i < 9; i++)
					{
						cout << div[i] << " ";
					}
					cout << endl;
					count--;
				}
			}
			//cout<<"out ofisvalid if num= "<<num<<endl;
			num++;
		}
	}
	return 0;
}