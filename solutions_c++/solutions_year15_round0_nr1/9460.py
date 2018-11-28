#include <fstream>
#include <iostream>
using namespace std;

int main()
{
	ifstream input("A-large.in");
	ofstream output("A-large.out");
	try
	{
		// get data
		if (input.is_open())
		{
		// get case number
		int caseNum = 0;
		input>>caseNum;
		// process case

		for (int i=0; i <caseNum; i++)
		{				
			int Smax;
			int S[1000];
			int count=0;
			int result=0;
			char ch;
			input>>Smax;
			for(int j=0; j<=Smax; j++)
			{
				input >> ch;
				S[j] = ch - '0';
			}
			//4 06004
			for(int j=0; j <=Smax; j++)
			{
				if ((j - count) > 0)
				{
					result += (j - count);
					count += (S[j]+(j - count));
				}
				else
					count += S[j];
			}
			if (output.is_open())
			{
				int index = i;
				output<<"Case #"<<++index<<": "<<result<<endl;
				//output.close();
			} 
			else
			{
				throw runtime_error("failed to open file to write");
			}
		}
		}
		else
		{
			throw runtime_error("failed to open file to read");
		}
	}
	catch (runtime_error err)
	{
		cerr<<"runtime error: "<<err.what()<<endl;
	}
	output.close();
/*


	cin >> Smax;
	for(int i=0; i<=Smax; i++)
	{
		cin >> S[i];
	}
	//5 110011
	for(int i=0; i <=Smax; i++)
	{
		if ((i - count) > 0)
		{
			result += (i - count);			
		}
		count += (S[i]+(i - count));
	}
	cout << result << endl;
	system("pause");

	*/
	return 0;
}