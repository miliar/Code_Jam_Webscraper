//problem1 < input.txt > output.txt

#include <iostream>
#include <vector>

using namespace std;

bool sleepsheep(vector<int>& v);

int main()
{	int tests;
	cin>>tests;
	int testCases[tests];
	for(int l=0;l<tests;l++)
	{
		cin>>testCases[l];
	}

	for(int k=1;k<=tests;k++)
	{
		long long myN=testCases[k-1];
		long long N=myN;
		vector<int>digitsSeen;
		vector<int> check(10);

		//initializing to 0's
		for(int i=0;i<check.size();i++)
		{
			check[i]=0;
		}
		int i=1;
		int number;
		int temp;
		bool sleep;
		int lastnumber;
		bool done=0;
		while(done!=1)
		{	number=N;
			while(number>=10)
			{	temp=number%10;
				digitsSeen.push_back(temp);
				check[temp]=check[temp]+1;
				number=number/10;
				if(number<10)
				{
						digitsSeen.push_back(number);
						check[number]=check[number]+1;
						
				}

				if(sleepsheep(check)==true)
				{
					cout << "Case #" << k << ": "<< N << endl;
					done=1;
					break;
				}
			}

			if(number<10)
			{
				digitsSeen.push_back(number);
				check[number]=check[number]+1;
			}

			if(N==0)
			{	cout << "Case #" << k << ": INSOMNIA" << endl;
				done=1;
			}
			i++;
			N=myN*i;
			
		}

	}


	return 0;
}

bool sleepsheep(vector <int>& v)
{	int count=0;
	for(int i=0;i<v.size();i++)
	{
		if(v[i]>=1)
		{
			count++;
		}
	}

	if(count<10)
	{
		return false;
	}
	else
	{
		return true;
	}
}