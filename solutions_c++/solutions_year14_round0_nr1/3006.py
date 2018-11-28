#include <iostream>
#include <fstream>
using namespace std;

int count(int* first, int* second)
{
	int cou=0;
	int num=0;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(first[i]==second[j])
			{
				cou++;
				num=first[i];
			}

		}

	}
	if(cou == 1)
		return num;
	else if(cou == 0)
		return 0;
	else return -1;
}
int main(int argc,char* argv[])
{
	std::ifstream infile(argv[1]);
	int T;
	infile >> T; //no of testcases

	// variables for each testcase
	int roew; 
	int result;
	int first[4];
	int second[4];
	int temp;


	for (int i=0;i<T;i++)
	{
		//variable intioalization for each testcase
		result = 0;
		infile >> roew;
		for (int j=0; j<16;j++)
		{
			infile >> temp;
			if (j>=(roew-1)*4 && j<roew*4)
				first[j%4]=temp;
		}
		infile >> roew;
		for (int j=0; j<16;j++)
		{
			infile >> temp;
			if (j>=(roew-1)*4 && j<roew*4)
				second[j%4]=temp;
		}

		result = count(first,second);
		switch(result){
			case 0:
				cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
				break;
			case -1:
				cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
				break;
			default :
				cout << "Case #" << i+1 << ": " << result << endl;

		}
	}
	return 0;
}

