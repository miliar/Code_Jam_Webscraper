#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int arrangement1[4][4];
	int arrangement2[4][4];
	int T=0,choice1=0,choice2=0;

	ifstream fin("A-small-attempt1.in");
	ofstream fout("output.txt");
	
	fin>>T;

	int i=1;

	while(i<=T && (T>=1 && T<=100))
	{
		choice1=choice2=0;
		fin.ignore(1);
		while(choice1<1 || choice1>4)
		{	
			fin>>choice1;
			//cout<<"choice1 = "<<choice1<<endl;
			if(choice1<1 || choice1>4)
			{
				fout<<"Opps! wrong row from arrangement 1..."<<endl;
			}
			//system("pause");
		}
		choice1--;
		for(int j=0;j<4;j++)
		{
			fin>>arrangement1[j][0]>>arrangement1[j][1]>>arrangement1[j][2]>>arrangement1[j][3];
		}
		

		while(choice2<1 || choice2>4)
		{ 
			fin>>choice2;
			//cout<<"choice2 = "<<choice2<<endl;
			if(choice2<1 || choice2>4)
			{
				fout<<"Opps!You choose wrong row from arrangement 2..."<<endl;
			}
		}
		choice2--;
		for(int j=0;j<4;j++)
		{
			fin>>arrangement2[j][0]>>arrangement2[j][1]>>arrangement2[j][2]>>arrangement2[j][3];
		}
		
		int count_match=0;
		int match=0;

		for(int m=0;m<4;m++)
		{
			for(int n=0;n<4;n++)
			{
				if(arrangement1[choice1][m]==arrangement2[choice2][n])
				{
					match=m;
					count_match++;
				}
			}
		}

		if(count_match==0)
		{
			fout<<"case #"<<i<<": Volunteer cheated!"<<endl;
		}
		else
			if(count_match>1)
			{
				fout<<"case #"<<i<<": Bad Magician!"<<endl;
			}
			else
				fout<<"case #"<<i<<": "<<arrangement1[choice1][match]<<endl;
		
		i++;
		
	}
	fin.close();
	fout.close();
	return 0;
}