#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <fstream>
#include<math.h>

using namespace std;

bool CheckBal(int num)
{
	int n, digit, rev = 0;
	n = num;
	do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);

	 if (n == rev)
		 return true;
	 else
		 return false;
}

bool isperfect(int n)
{
    double xp=sqrt((double)n);
    if (floor(xp) == xp)
		return true;
	else
		return false;
}

int main()
{

	int count;
	ifstream cin("C-small-attempt0.in");
	ofstream cout("output.txt");

	cin>>count;
	
	for(int i=0;i<count;i++)
	{
		int a,b;cin>>a>>b;
		int count = 0;
		for(int j=a;j<=b;j++)
		{
			if(isperfect(j))
			{
				if(CheckBal(j) && CheckBal(sqrt(j)))
				{
					count++;
				}
			}

		}

		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
}