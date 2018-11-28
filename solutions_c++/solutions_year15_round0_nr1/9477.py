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
			int Smaxim;
			int S [1000] ;
			int count = 0;
			int result = 0;
			char ch;
			input>>Smaxim;
			for(int j=0; j<=Smaxim; j++)
			{
				input >> ch;
				S[j] = ch - '0';
			}
			//0 1
			for(int j=0; j <=Smaxim; j++)
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


	cin >> Smaxim;
	for(int i=0; i<=Smaxim; i++)
	{
		cin >> S[i];
	}
	//5 110011
	for(int i=0; i <=Smaxim; i++)
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