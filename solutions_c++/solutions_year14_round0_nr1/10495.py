#include <iostream>
#include <unordered_set>
#include <vector>

int main(int argc, char const *argv[])
{
	using namespace std;
	freopen("Input.txt", "r", stdin);
	freopen("Output.txt", "w", stdout);
	int testCases;
	cin>> testCases;
	for(int testCase = 1; testCase <= testCases; testCase++)
	{
		unordered_set<int> rowCardsHash;
		vector<int> resultSet;
		for(int k = 0; k < 2 ; k++)
		{
			int userRow ;
			cin>> userRow; 
			for(int i = 0; i < 4; i++)
			{
					
				for(int j = 0; j < 4; j++)
				{
					int dumpData;
					if(i != userRow - 1)
					{
						cin>>dumpData;
						continue;
					}

					register int rowCard;
					cin>>rowCard;
					std::pair<std::unordered_set<int>::iterator,bool> ret =  rowCardsHash.insert(rowCard);
					if(!ret.second)
					{
						resultSet.push_back(rowCard);
					}
				}
			}	
		}

		if(resultSet.size() == 1)
		{
			cout<<"Case #"<<testCase<<": "<<resultSet[0]<<endl;
		}
		else if(resultSet.size() == 0)
		{
			cout<<"Case #"<<testCase<<": "<<"Volunteer cheated!"<<endl;
		}
		else
		{
			cout<<"Case #"<<testCase<<": "<<"Bad magician!"<<endl;
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}