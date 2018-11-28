#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <ctime>
using namespace std;
#include <conio.h>


ifstream infile;
string STRING;
ofstream offile;
string pattern;

int arr [100][100];
unsigned long long int count[100];
void getcount(int k,int c,int s,int &size);


long  main()
{
	infile.open ("c:\\temp\\in.txt");
	offile.open("c:\\temp\\out3.txt");

	int testcases;
	infile >> testcases;
	

	for(int i=1;i<=testcases;i++)
	{
		
		//init
		for(int kk=0;kk<=99;kk++)
			count[kk]=-1;

		//Init arry
		for(int ii=0;ii<=99;ii++)
		{
			for(int jj=0;jj<=99;jj++)
			{
				arr[ii][jj]=-1;
			}
		}

		int k,c,s;
		int size=0;
		infile >> k;
		infile >> c;
		infile >> s;
		if(s!=k)
		{
			cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
			offile<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<"\n";
			continue;
		}

		getcount(k,c,s,size);
				
		cout<<"Case #"<<i<<": ";
		offile << "Case #"<<i<<": ";
		for(int i=0;i<size;i++)
		{
			if((i+1) == size)
			{
				offile<<count[i];
				cout<<count[i];
			}
			else
			{
				offile<<count[i]<<" ";
				cout<<count[i]<<" ";
			}
		}
		offile <<"\n";
		cout<<endl;
				
	}
	
	getch();
	infile.close(); 
	offile.close();
	return 0;
}


void getcount(int k,int c,int s,int &size)
{
	unsigned long long int numoftile=k;
	for(int i=1;i<c;i++)
	{
		numoftile=numoftile*k;
	}
	if(c==1)
	{
		size=k;
		for(int yy=0;yy<k;yy++)
		{
			count[yy]=yy+1;
		}
		
	}
	/*else if(k == 2)
	{
		size=1;
		count[0]=2;

	}*/
	else if ( k == 1)
	{
		size=1;
		count[0]=1;
	}
	else
	{
		size=k-1;
		int y=1;
		int test = 0;
		for(int s=(size-1);s>=0;s--)
		{
			count[s]= numoftile-(y*k) - test;
			y++;
			test++;
		}
		/*count[0]=2;
		count[1]=numoftile-k;	*/

	}

	/*}*/
}

