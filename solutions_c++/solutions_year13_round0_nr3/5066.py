#include <iostream>
//#include <string>
#include <cmath>
#include <fstream>
using namespace std;
int main()
{
	ofstream fo("output.txt");
    ifstream fi("data.txt");
	int cases;
	int count=0;
	int isPalin(int );
	fi >> cases;
	double min,max;
	for(int i=0;i<cases;++i)
	{
		count =0;
		fi>> min >> max;
		int j=sqrt(min);
		if(min > j*j)
			j++;

		for(j;j<=sqrt(max);++j)
		{
			if((isPalin(j) == 1) && (max >= j*j))
			{
				if(isPalin(j*j))
					count++;
			}
		}
		fo << "Case #" << i+1 << ": " << count << endl;
	}
	return 0;
}
int isPalin(int a)
{
	int ans=0;
	int num=a;
	while(num>0)
	{
		ans = num%10 + ans *10;
		num /= 10;
	}
	return (ans==a);
}
