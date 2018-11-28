#include <iostream>
#include <iomanip>
#include <string>
#include <string.h>
#include <fstream>


using namespace std;
class cards
{
	private:
	int set1[4];
	int set2[4];
	public:
		void setRow1(int ans, int arr[4][4])
		{
			int temp[4];
			for (int i = 0; i < 4; i++)
			{
				set1[i] = arr[ans-1][i];
			}
		}
		void setRow2(int ans, int arr[4][4])
		{
			int temp[4];
			for (int i = 0; i < 4; i++)
			{
				set2[i] = arr[ans-1][i];
			}
		}
		int Compare()
		{
			int flag = 0 ;
			int correct;
			for (int i = 0; i < 4; i++)
			{
				for (int j = 0; j  < 4; j ++)
				{
					if( set1[i] == set2[j]){
						if(flag == 0)correct = set1[i];
						flag += 1;
					}

				}
			}
			if(flag == 0)return 0;//cheated
			else if(flag == 1)return correct;
			else return -1;//bad magician
		}
	
};

int  main()
{
	int firstans = 2, secondans = 3;
	int* firstset;
	int* secondset;

	int arr1[4][4] = { {1, 2, 3, 4},
					{5, 6, 7, 8},
					{9, 10, 11, 12},
					{13, 14, 15, 16}};

	int arr2[4][4] = {{ 1, 2, 5, 4},
					{3, 11, 6, 15},
					{9, 10, 7, 12},
					{13, 14, 8, 16}};

	cards c;


	
	string inpath = "E:\input text.txt";
	string outpath = "E:\output text.txt";
	string temp;

	ifstream inputfile; string input;
	ofstream outputfile; string output;
	
	inputfile.open(inpath);
	outputfile.open(outpath);

	string token;
	if(inputfile.is_open())
	{
		int cases;
		getline(inputfile, input);
		cases = atoi(input.c_str());
		
			getline(inputfile, input);
		for (int i = 0; i < cases; i++)
		{
			firstans = atoi(input.c_str());

			getline(inputfile, input);
			int pos= 0, old = 0;
			
			for (int j = 0; j < 4; j++)
			{
				for (int k= 0; k < 4; k++)
				{
					pos = input.find_first_of(" ", old);
					token = input.substr(old , pos);
					arr1[j][k] = atoi(token.c_str());
					old = pos+1;
				}
				getline(inputfile, input);
				old =0;pos = 0;
			}

			secondans = atoi(input.c_str());
			getline(inputfile, input);
			for (int j = 0; j < 4; j++)
			{
				for (int k= 0; k < 4; k++)
				{
					pos = input.find_first_of(" ", old);
					token = input.substr(old , pos);
					arr2[j][k] = atoi(token.c_str());
					old = pos+1;
				}
				getline(inputfile, input);
				old =0;pos = 0;
			}
			c.setRow1(firstans, arr1);
			c.setRow2(secondans, arr2);
			int out = c.Compare();
			if(out == 0)outputfile << "Case #"<< i+1 << ": " <<"Volunteer cheated!" << endl;
			else if(out < 0)outputfile << "Case #"<< i+1 << ": " <<  "Bad magician!" << endl;
			else outputfile << "Case #"<< i+1 << ": " << out << endl;

			cout << "Case #" << i+1 << ": Done" << endl;
		}
		inputfile.close();
		outputfile.close();
	}else cout << "can not open one of the files" << endl;

	getchar();
	return 0;
}