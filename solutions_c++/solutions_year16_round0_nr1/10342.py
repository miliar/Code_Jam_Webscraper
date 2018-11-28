#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <algorithm>
#include <iterator>
#include <numeric>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int sumofarray(int arr[])
{
	int sum=0;
	
	for(int i=0;i<10;i++)
	{
		sum = sum + arr[i];
	}
	
	return sum;
	
}
int main(int argc, char **argv) {
  int t;
  long int n,no,tempno;
  int flag,multiplier;
  int sumofarr;
  int mod;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
	cin >> n;
	int arr[] = {0,0,0,0,0,0,0,0,0,0};
	if(n==0)
	{
		cout << "Case #" << i << ": INSOMNIA"<< endl;
	}
	else
	{
		flag=0;
		multiplier = 1;
		while(flag==0)
		{
			no = n * multiplier;
			tempno = no;
			while (tempno > 0)
			{
				mod = tempno%10;				
				if(arr[mod] == 0)
				{
					arr[mod]=1;
				}
			      	tempno = tempno/10;
			}
			sumofarr = sumofarray(arr);
			if(sumofarr==10)
			{
				flag = 1;
				cout << "Case #" << i << ": "<<no<< endl;	
			}
			else
			{
				multiplier++;
				
			}
		}
	}
  }
}
