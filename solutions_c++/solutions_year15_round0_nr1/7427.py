#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

unsigned int InvitePeople(string input);

void main(){
	string line;
	ifstream inputfile("D:\\input.txt");
	if(inputfile.is_open())
	{
		getline (inputfile,line);
		unsigned int num_cases = atoi(line.c_str());
		vector<unsigned int> result;

		while (! inputfile.eof() )
		{
			getline (inputfile,line);
			unsigned int invited_people = 0;

			//process each case
			invited_people = InvitePeople(line);

			result.push_back(invited_people);
		}
		inputfile.close();

		//output
		ofstream outputfile("D:\\output.txt");
		for(unsigned case_index=1; case_index<=num_cases;case_index++)
		{
			outputfile << "Case #"<<case_index<<": "<<result[case_index-1]<<endl;
		}
	}
	else
		cout<<"Unable to open the file\n";

	system("pause");
}

unsigned int InvitePeople(string input)
{
//	cout << input << endl;
	unsigned int neededpeople = 0;
	unsigned int highestShyness = 0;
	vector<unsigned int> num_people_at_each_shyness_level;

	istringstream iss (input);
	string word;
	
	iss >> word;
	highestShyness = atoi(word.c_str());

	iss >> word;
//	cout<<highestShyness<<": ";
	for(unsigned int i=0;i<=highestShyness;i++)
	{
		num_people_at_each_shyness_level.push_back((unsigned int)(word[i]-48));
//		cout <<" "<<num_people_at_each_shyness_level[i];
	}
//	cout << endl;

	//process the case
	if(highestShyness==0)
		neededpeople=0;
	else
	{
		unsigned int sn = num_people_at_each_shyness_level[0];
		for(unsigned int j=1; j<=highestShyness;j++)
		{
			if(sn >= j)
				sn = sn + num_people_at_each_shyness_level[j];
			else
			{
				neededpeople = neededpeople + j - sn;
				sn = j + num_people_at_each_shyness_level[j];
			}
		}
	}
	return neededpeople;
}