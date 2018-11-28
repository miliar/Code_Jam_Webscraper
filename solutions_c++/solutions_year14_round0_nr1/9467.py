#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
	int casenum = 0;
	int answer = 0;
	int firstline[4];
	int secondline[4];
	int result = 0;
	char buffer[256];
	memset(buffer, 0, 256);
	ifstream infile("A-small-attempt1.in");
	ofstream outfile("result.out");
	if(!infile)
	{
		cout << "Unable to open infile" << endl;
		exit(1);
	}
	if(!outfile)
	{
		cout << "Unable to open outfile" << endl;
		exit(1);
	}
	
	infile.getline(buffer, 10);
	sscanf_s(buffer, "%d", &casenum);
	cout<<casenum<<endl;

	for(int i = 1; i <= casenum; i ++)
	{
		result = 0;
		infile.getline(buffer, 10);
		sscanf_s(buffer, "%d", &answer);
		for(int j = 1; j <= 4; j ++)
		{
			infile.getline(buffer, 20);
			if(j == answer){
				sscanf_s(buffer, "%d %d %d %d", &firstline[0], &firstline[1], &firstline[2], &firstline[3]);
			//	cout << firstline[0]<<endl;
			}
		}
		infile.getline(buffer, 10);
		sscanf_s(buffer, "%d", &answer);
		for(int j = 1; j <= 4; j ++)
		{
			infile.getline(buffer, 20);
			if(j == answer){
				sscanf_s(buffer, "%d %d %d %d", &secondline[0], &secondline[1], &secondline[2], &secondline[3]);
			//	cout << secondline[0]<<endl;
			}
		}
		for(int j = 0; j < 4; j ++)
		{
			for(int k = 0; k < 4; k ++)
			{
				if(firstline[j] == secondline[k])
				{
					if(result == 0)
					{
						result = firstline[j];
					}
					else if(result > 0)
					{
						result = -1;//more than one answer
					}
				}
			}
		}
		switch(result)
		{
		case -1:
			outfile<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
			break;
		case 0:
			outfile<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
			break;
		default:
			outfile<<"Case #"<<i<<": "<<result<<endl;
			break;
		}
	}
	infile.close();
	outfile.close();
}