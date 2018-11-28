#include <iostream>
#include <cmath>
using namespace std;
bool checkPalindromes(int x, int counter)
{
	int mid = (counter/2)+1;
	int* xarry = new int [counter+1];
	for ( int i = 1; i < (counter+1) ; ++i)
	{
		xarry[i] = x%10;
		x=x/10;
	}
	for ( int i = 1 ; i < mid ; ++i)
	{
		if (xarry[i] != xarry[counter])
			{
				return false;
			}
		counter--;
	}
	return true;
}
bool checkDigit (int x, int &counter)
{
	counter = 0;
	while (x!=0)
	{
		counter++;
		x=x/10;
	}
	if (counter %2==1)
	{
			return true;
	}
			return false;
}

int main ()
{
	int size;
	cin>>size;
	for (int i = 1 ; i <= size ; i++)
	{
		cout<<"Case #"<<i<<": ";
		int result = 0;
		int x,y;
		cin>>x;
		cin>>y;	
		//Here is to check the number.!
		while (x<=y)
		{
		int counter = 0;
		int counter2=0;
		if (checkDigit(x, counter)== true)
			{
				if (checkPalindromes(x, counter)==true)
				{
					for ( int j = 1 ; j <= sqrt(x) ; j++)
						{ 
							if (j*j ==x)
							{
								checkDigit(j, counter2);
								if (checkPalindromes(j, counter2)== true)
								{
								result++;
								break;
								}
							}
						}
				}
			}
		x++;
		}
		cout<<result<<"\n";
	}
	system("PAUSE");
return 0;
}	