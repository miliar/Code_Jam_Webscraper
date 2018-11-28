#include<iostream>
using namespace std;
#include<fstream>
void main()
{
	int nooftest, arrange_1[4][4],arrange_2[4][4],first_ans,second_ans,cheater=0,fool=0,result;            //4 rows and each having four cards
	ifstream fin("A-small-attempt3.in");
	ofstream fout("output.txt");
	fin>>nooftest;
	for(int i=0;i<nooftest;i++)
	{
			cout<<"choose a card and answer me the row of the card";
			fin>>first_ans;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
			{
				fin>>arrange_1[j][k];
			}
		cout<<"now find your card and answer me the row in which it is";
		fin>>second_ans;
		cout<<"second ans"<<second_ans;
	   for(int j=0;j<4;j++)
		   for(int k=0;k<4;k++)
		   {
			   fin>>arrange_2[j][k];
		   }
		   for(int k=0;k<4;k++)
			   for(int j=0;j<4;j++)
			   {
		             if(arrange_1[first_ans-1][k]==arrange_2[second_ans-1][j])
		                { 
			                 cout<<"the card you have chosen have the number"<<arrange_1[first_ans-1][k];
			                 cheater++;
							 result=arrange_1[first_ans-1][k];
			                
		                 }
	             }
	
	if(cheater==0)
	{
	    fout<<"case #"<<i+1<<": Volunteer cheated! \n";
	}
	else if(cheater>1)
	{
		fout<<"case #"<<i+1<<": Bad magician!\n";
	}
	else
	{
		fout<<"case #"<<i+1<<": "<<result<<"\n";
	}
	cheater=0;
	}

	system("pause");
}


		   


	

