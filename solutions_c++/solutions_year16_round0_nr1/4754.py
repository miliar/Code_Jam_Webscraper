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
int num;

int arr [10];

void reverse(int inum,int &onum);
void getcount(int inum,int & ocount);

long  main()
{
	infile.open ("c:\\temp\\in.txt");
	offile.open("c:\\temp\\out3.txt");

	int testcases;
	infile >> testcases;
	

	for(int i=1;i<=testcases;i++)
	{
		//Re-Initialize array
		for(int ii=0;ii<10;ii++)
			arr[ii]=1;

		int count=0;
		infile >> num;
		if(num >0)
			getcount(num,count);
		
		if(count == 0)
		{
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
			offile << "Case #"<<i<<": "<<"INSOMNIA"<<"\n";	
		}
		else
		{
			cout<<"Case #"<<i<<": "<<count<<endl;
			offile << "Case #"<<i<<": "<<count<<"\n";	
		}
				
	}
	
	getch();
	infile.close(); 
	offile.close();
	return 0;
}


bool checkifSleep(int inum)
{
	while(inum > 0)
	{
		int rem=(inum%10);
		inum=inum/10;
		if( arr[rem] == 0)
			continue;
		else
			arr[rem] = 0;
	}
	if(1 == arr[0] || 1 == arr[1] || 1 == arr[2]  || 1 == arr[3] || 1 == arr[4] || 1 == arr[5] || 1 == arr[6] || 1 == arr[7] || 1 == arr[8] || 1 == arr[9])
		return false;
	else
		return true;
}

void getcount(int inum,int & ocount)
{
	int x=1;
	int num=0;
	while(x>0)
	{
		num=num+inum;
		bool reached = false;
		reached = checkifSleep(num);
		if( reached == true)
		{
			ocount=num;
			break;
		}
		x++;
	}


}