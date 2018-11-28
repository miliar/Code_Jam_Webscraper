
#include <iostream>
#include <string>
#include <math.h>
#include <memory.h> 
#include <fstream>
#include <sstream>
using namespace std;

//#define inFile cin
//#define  outFile cout

int judge(long long num, long long &i_inc)
{
	bool flag = true;
	stringstream ss;
	ss<<num;
	string num_s = ss.str();
	if (num_s.length() > 1 )
	{
		if (num_s[num_s.length() - 1] == '3')
		{
			i_inc += 7;
		}
		if (num_s[0] == '3')
		{
			i_inc += pow(10, num_s.length() - 1)*6;
		}
	}
	
	i_inc++;


	if (num_s.length() == 1 ||(num_s[num_s.length() - 1] >= '1' && num_s[num_s.length() - 1] <= '3' && num_s[0] >= '1' && num_s[0] <= '3'))
	{
		for (int i = 0; i != num_s.length()/2; i++)
		{
			if (num_s[i] != num_s[num_s.length() - i - 1])
			{
				//outFile<<num_s[i]<<" "<<num_s[num_s.length() - 1 -i];
				flag = false;
				return 0;
			}
		}
	}
	else
		return 0;

	return 1;
}


int judge2(long long num)
{
	bool flag = true;
	stringstream ss;
	ss<<num;
	string num_s = ss.str();


	for (int i = 0; i != num_s.length()/2; i++)
	{
		if (num_s[i] != num_s[num_s.length() - i - 1])
		{
			//outFile<<num_s[i]<<" "<<num_s[num_s.length() - 1 -i];
			flag = false;
			return 0;
		}
	}


	return 1;
}

int main()
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("C-small-attempt2.in");
	outFile.open("C-small-attempt2.out");

	int num_cases;
	inFile>>num_cases;
	char a;		
	inFile.get(a);
	long long A;
	long long B;
	int count = 0;
	for (int j = 1; j <= num_cases; j++)
	{
		inFile>>A>>B;
		
		int low = sqrt(A);
		if (low*low < A)
		{
			low++;
		}
		for (long long i = low; i*i <= B;)
		{
			long long i_square = i*i;
	
			if(judge(i, i)&&judge2(i_square))
			{
				cout<<i-1<<endl;
				count++;	
			}	
		}
		outFile<<"Case #"<<j<<": ";
		outFile<<count<<endl;
		count = 0;
	}
	return 0;
}


