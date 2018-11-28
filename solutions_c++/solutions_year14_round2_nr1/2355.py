// Repeater.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>

using namespace std;

string getUniq(string s)
{
	string ret;
	ret.push_back(s.at(0));

	for (int i=1; i<s.length(); i++)
	{
		if (s.at(i) != s.at(i-1))
			ret.push_back(s.at(i));
	}

	//cout<<"\n getting uniq strings: input::"<<s<<"\n output:"<<ret<<endl;

	return ret;
}

int main()
{
	int T,testCounter = 1, maxLength = 110;
	cin>>T;
	while (T--)
	{
		int N;
		string* inputStrings;
		cin>>N;

		inputStrings = new string[N];

		for( int i=0; i<N; i++)
		{
			cin>>inputStrings[i];
		}

		string prevuniqone = getUniq(inputStrings[0]);
		string curruniqone;
		bool flag = false;

		for (int i=1; i<N; i++)
		{
			curruniqone = getUniq(inputStrings[i]);

			//cout<<"\n comparing uniq strings: cur::"<<curruniqone<<"\n prev:"<<prevuniqone<<endl;
			
			if (curruniqone.compare(prevuniqone) != 0)
			{
				//cout<<"compare failed\n";
				flag = true;
				break;
			}
			prevuniqone = curruniqone;
		}

		if (flag)
		{
			printf("Case #%d: Fegla Won\n",testCounter);
		}
		else
		{
			if (N==2)
			{
				int opcounter = 0, occ1 = 0, j=0, occ2 = 0, k=0;
				for (int i=0; i<curruniqone.length(); i++)
				{
					occ1 = 0;
					occ2 = 0;
					while((j < inputStrings[0].length())&& (inputStrings[0].at(j) == curruniqone.at(i)))
					{
						occ1++;
						j++;
					}

					while ((k < inputStrings[1].length())&&(inputStrings[1].at(k) == curruniqone.at(i)))
					{
						occ2++;
						k++;
					}

					opcounter += abs(occ1-occ2);
				}

				printf("Case #%d: %d\n",testCounter, opcounter);
			}
		}

		delete[] inputStrings;

		testCounter++;		
	}

	return 0;
}


