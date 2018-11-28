#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int compare(int *A,int *B);


int main()
{
	int t,type;
	int row;
	int A[4][4];
	int B[4][4];
	int A1[4];
	int B1[4];
	ifstream myfile;
	myfile.open("A-small-attempt0.in");
	ofstream out;
	out.open("jam1output.txt");
	myfile>>t;
	for(int u=0;u<t;u++)
	{	
		int n;
		myfile>>row;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				myfile>>A[i][j];

		for(int i=0;i<4;i++)
			A1[i]=A[row-1][i];

		myfile>>row;
		for(int i=0;i<4;i++)
                	for(int j=0;j<4;j++)
               			myfile>>B[i][j];

                for(int i=0;i<4;i++)
               		 B1[i]=B[row-1][i];

		type=compare(A1,B1);
		if(type>0)
		out<<"Case #"<<u+1<<": "<<type<<'\n';
		else if(type==-1)
		out<<"Case #"<<u+1<<": Bad magician!\n";
		else
		out<<"Case #"<<u+1<<": Volunteer cheated!\n";
	}
	return 0;
}

int compare(int *A ,int *B)
{
	int n=-1;
	bool flag=false;
	int count=0;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(A[i]==B[j])
			{
				n=A[i];
				count++;
			}
	if(count==1)
	return n;
	else if(count==0)
 	return -2;
	else
	return -1;
}
			

		

	
