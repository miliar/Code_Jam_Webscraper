#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("E:\\input.txt");
	ofstream out("E:\\output.txt");

	int all[100][100];

	int total;
	in>>total;


	for(int i=0; i<total; i++)
	{
		//each case
		int column,row;
		in>>row;
		in>>column;
		bool success = true;
		// get input
		for(int k=0; k<row; k++)
		{
			for(int j=0; j<column; j++)
			{
			
					in>>all[k][j];
			}
		}

		for(int j=0; j<column; j++)
		{
			for(int k=0; k<row; k++)
			{
				//judge for each point
				bool rowMax = true;
				bool columnMax = true;
				for(int l=0; l<column; l++)
				{
					if(all[k][l] > all[k][j])
					{
						
						rowMax = false;
						//break;
					}
					
				}
				if(rowMax == false)
				{
					for(int m=0; m<row; m++)
					{
						if(all[m][j] > all[k][j])
						{
							columnMax = false;
							success = false;
							//break;
						}
					}
				}
			}
		}
		if(success == true)
		{
			out<<"Case #"<<i+1<<": YES"<<endl;
		}
		else
		{
			out<<"Case #"<<i+1<<": NO"<<endl;
		}


		

	}
	return 0;
}