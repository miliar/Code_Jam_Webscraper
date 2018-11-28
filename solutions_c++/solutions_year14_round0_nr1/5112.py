#include<iostream>
#include<fstream>
using namespace std;

int main()
{
  

ifstream in;
in.open("a.txt");
ofstream out;
out.open("output.txt");


int N;
int C;
int I=0;
int a=0;
in>>N;
for(int n=0; n<N; n++)
{
	in>>C;
	C--;
	
	int items[4][4]={0};
	for(int i=0; i<4; i++)
	for(int j=0; j<4; j++)
	{
		in>>items[i][j];
	}
	int choice_row[4]={0};
	for(int k=0; k<4; k++)
	{
		choice_row[k]= items[C][k];	
	}
	
	
	
	in>>C;
	C--;
	
	for(int i=0; i<4; i++)
	for(int j=0; j<4; j++)
	{
		in>>items[i][j];
	}
	
	for(int i=0; i<4; i++)
	{
	for(int k=0; k<4; k++)
	{
		if(items[C][k]==choice_row[i])
		{
		a++;
		I=choice_row[i];
		
		}
		
		
	}
	}
	if(a==1)
	out<<"Case #"<<n+1<<": "<<I<<"\n";
	else if(a>1)
	out<<"Case #"<<n+1<<": Bad magician!\n";
	else if(a==0)
	out<<"Case #"<<n+1<<": Volunteer cheated!\n";
	
	a=0;
}

}	

