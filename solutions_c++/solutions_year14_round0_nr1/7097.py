#include<iostream>
#include<fstream>
#include<string>
using namespace std;
void main()
{
	int testnum=0;
	int istch=0,secch=0;
	int first[4][4];
	int sec[4][4] ;
	ifstream myfile ("A-small-attempt2.in");
					ofstream out ("output.txt",ios::out);
	if (myfile.is_open())
	{
		myfile>>testnum;
			int nn=0;
		while(testnum>0)
		{ 
			nn++;
			myfile>>istch;
			for(int j=0;j<4;j++)
			{
				for(int k=0;k<4;k++)
				{
					myfile>>first[j][k];
				}
			}
			myfile>>secch;
			for(int j=0;j<4;j++)
			{
				for(int k=0;k<4;k++)
				{
					myfile>>sec[j][k];
				}
			}

			int mat=0, n=0;
			for(int x=0;x<4;x++)
			{
				for(int y=0 ; y<4 ; y++){
					if(first[istch-1][x]==sec[secch-1][y])
					{
						n=first[istch-1][x];
						mat++;
						break;
					}
				}
			}

			if(mat>1)
			{
				out<<"Case #"+to_string(nn)+": Bad magician!"<<endl;
			}
			else if(mat==0)
			{
				out<<"Case #"+to_string(nn)+": Volunteer cheated!"<<endl;
			}
			else
			{
				out<<"Case #"+to_string(nn)+": "+to_string(n)<<endl;
			}
			testnum--;
		}
	}

}