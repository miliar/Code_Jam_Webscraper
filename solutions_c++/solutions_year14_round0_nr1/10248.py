#include<iostream>
#include<fstream>
using namespace std;

void showCards(int myCards[4][4])
{

	for(int i=0; i<4;i++)
	{
		for(int j=0; j<4;j++)
		{
			cout<<myCards[i][j]<<" ";
		}
		cout<<endl;
	}

}

int main()
{
	int myCards[4][4];
	int k=1;
	for(int i=0; i<4;i++)
	{
		for(int j=0; j<4;j++)
		{
	//		myCards[i][j]= k+i+j;
	//		cout<<myCards[i][j]<<" ";
		}
	//	cout<<endl;
		k += 3;
	}

	int noOfTestCases, Ans1,Ans2, Row1[4],Row2[4];
	ifstream Read("A-small-attempt0.in");
	ofstream Write("Output.txt");

	if(Read.is_open())
	{
//		while(!Read.eof())
		{
			Read>>noOfTestCases;
			cout<<"Total test Cases: " <<noOfTestCases<<endl;

			for(int A=1; A<= noOfTestCases; A++)
			{
				Read>>Ans1;
				cout<<Ans1<<endl;

				for(int i=0; i<4;i++)
				{
					for(int j=0; j<4;j++)
					{
						Read>>myCards[i][j];
						cout<<myCards[i][j]<<" ";
					}
					cout<<endl;
				}

				cout<<"\n ROW1: ";
				i=Ans1-1;
				for(int j=0; j<4;j++)
				{
					Row1[j] = myCards[i][j];
					cout<<Row1[j]<<" ";
				}
				cout<<endl;

				Read>>Ans2;
				cout<<Ans2<<endl;

				for(i=0; i<4;i++)
				{
					for(int j=0; j<4;j++)
					{
						Read>>myCards[i][j];
						cout<<myCards[i][j]<<" ";
					}
					cout<<endl;
				}
				cout<<"\n ROW2: ";
				i=Ans2-1;
				for(j=0; j<4;j++)
				{
					Row2[j] = myCards[i][j];
					cout<<Row2[j]<<" ";
				}
				cout<<endl;
				cout<<endl;

				int counter=0;
				for(i=0; i<4;i++)
				{
					for(int j=0; j<4;j++)
					{
						if(Row1[i]==Row2[j])
						{
							Ans1= Row1[i];
							counter++;
						}
					}
				}

				if(counter==1)
				{
					Write<<"Case #"<<A<<": "<<Ans1<<endl;
				}
				else if(counter>1)
				{
					Write<<"Case #"<<A<<": "<<"Bad Magician!"<<endl;
				}
				else if(counter==0)
				{
					Write<<"Case #"<<A<<": "<<"Volunteer Cheated!"<<endl;
				}




			}
		}

	}

return 0;
}