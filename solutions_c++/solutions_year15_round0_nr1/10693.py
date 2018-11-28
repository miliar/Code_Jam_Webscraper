#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	string line;
	ifstream infile ("A-small-attempt2.in");
	int T, numberCount, S, ans, sum;
	string str;
	int* ansArray = NULL;
	//cin>>T;
	//int* ansArray = new int[T];
	//for (int i = 0; i<T;i++)
	//{
	//	cin>>numberCount>>str;
	//	ans = 0;
	//	for (int j = 0; j<=numberCount; j++)
	//	{
	//		S = atoi(str.substr(j,1).c_str());
	//		if (S==0)
	//			ans++;
	//	}
	//	ansArray[i] = ans;
	//}

	int countr = -1;
	if (infile.is_open())
	{
		while ( getline (infile,line) )
		{
			if (countr == -1)
			{
				T=atoi(line.c_str());
				ansArray = new int[T];
			}
			else
			{
				numberCount = atoi(line.substr(0, 1).c_str());
				str = line.substr(2);

				ans = 0;
				sum = 0;
				for (int j = 0; j<=numberCount; j++)
				{
					S = atoi(str.substr(j,1).c_str());
					if (sum<j)
					{
						ans++;
						sum++;
					}
					sum+=S;
				}
			ansArray[countr] = ans;
			}
			countr++;
		}
		infile.close();
	}

	ofstream outfile;
	outfile.open ("out.out");
	for (int i = 0; i<T;i++)
	{
		cout<<"Case #"<<i+1<<": "<<ansArray[i]<<endl;
		outfile <<"Case #"<<i+1<<": "<<ansArray[i]<<endl; 
	}
	delete []ansArray;
	outfile.close();
}