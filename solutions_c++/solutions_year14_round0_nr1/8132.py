#include<iostream>
#include<fstream>
using namespace std;


int main()
{
 ifstream myfile;
  myfile.open("A-small-attempt4.in");
  ofstream output;
  output.open("output.txt");
 int T;
 myfile>>T;
 int t=1;
 int n1;
 int n2;
  
 int first[4][4],second[4][4];
 while(t<=T)
	{
	 myfile>>n1;
	 n1--;
	 for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			myfile>>first[i][j];
	 myfile>>n2;
	 n2--;
 	 for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			myfile>>second[i][j];
	 int found;
	 int c=0;
	 for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(first[n1][i]==second[n2][j])
				{
				 c++;
				 found=first[n1][i];
				}
	 if(c>1)
		output<<"Case #"<<t<<": Bad magician!"<<endl;
	 else if(c==1)
		output<<"Case #"<<t<<": "<<found<<endl;
	 else 	
		output<<"Case #"<<t<<": Volunteer cheated!"<<endl;
	 t++;
	}
 return 0;
}
