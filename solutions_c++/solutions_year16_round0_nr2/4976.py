#include <iostream>
#include <fstream>
#include <vector> 

using namespace std;

bool check(string pancake);
int main()
{	
	int tests;
	cin>>tests;
	vector<string> testcases(tests);

	for(int l=0;l<tests;l++)
	{
		cin>>testcases[l];
	}
	//cout << "done" << endl;
	string pancake;
	for(int j=0;j<testcases.size();j++)
	{
		pancake=testcases[j];
		
			int minus=0;
			int plus=0;
			int flips=0;
		while(check(pancake)!=true)
		{
			//cout << pancake << endl;
			for(int i=0;i<pancake.length();i++)
			{
				if(pancake[i]=='-') //consecutive minus
				{
					minus++;
				}
				else
				{
					break;
				}
			}

			for(int i=0;i<minus;i++)
			{
				pancake[i]='+';
			}
			if(minus!=0)
			{
				flips++;
			}
			if(check(pancake))
			{
				break;
			}
			//cout << pancake << endl;
			minus=0;
			
			
			for(int i=0;i<pancake.length();i++)
			{
				if(pancake[i]=='+') //consecutive plus
				{
					plus++;
				}
				else
				{
					break;
				}	
			}
			for(int i=0;i<plus;i++)
			{
				pancake[i]='-';
			}
			//cout << pancake << endl;
			
			if(plus!=0)
			{
				flips++;
			}
		plus=0;

		}


		cout << "Case #" << j +1<< ": "<< flips <<endl;
	}





	return 0;
}

bool check(string pancake)
{
	bool happy=false;
	int count=0;
	for(int i=0;i<pancake.length();i++)
	{
		if(pancake[i]=='+')
		{
				count++;
		}
	}

	if(count==pancake.length())
	{
		return true;
	}
	else
	{
		return false;
	}

}