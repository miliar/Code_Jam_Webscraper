#include<iostream>
#include<fstream>
using namespace std;
int main(int argc, char const *argv[])
{
	int T,A,B,no1[5][5],no2[5][5],x,y,z;
	ifstream ifs("A-small-attempt2.txt");
	ofstream ofs("output.txt");
	ifs>>T;
	for(int I=1;I<=T;I++)
	{
		ifs>>A;
		for (int i = 1; i < 5;++i)
		{
			for(int j=1;j<5;j++)
			{
				ifs>>no1[i][j];
			}
		}
		ifs>>B;
		for (int i = 1; i < 5;++i)
		{
			for(int j=1;j<5;j++)
			{
				ifs>>no2[i][j];
			}
		}
		x=0;
		for(int i=1;i<5;i++)
		{
			for(int j=1;j<5;j++)
			{
				if(no1[A][i]==no2[B][j])
				{
					x++;
					y=no1[A][i];
					break;
				}
			}
		}
		if(x==1)
			ofs<<"Case #"<<I<<": "<<y<<"\n";
		else if (x>1)
		{
			ofs<<"Case #"<<I<<": Bad magician!\n";
		}
		else
			ofs<<"Case #"<<I<<": Volunteer cheated!\n";
	}




	return 0;
}