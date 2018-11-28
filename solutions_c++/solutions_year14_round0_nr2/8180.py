#include<iostream>
#include<cstring>
#include<string>
#include<sstream>
#include<fstream>
#include<iomanip>
//#include"header.h"

using namespace std;

char **readInput(char name[50])
 {
 	char **data1=new char*[110];
 	char temp[50];
	ifstream file;
	file.open(name);
	if (file)
	{
		int i=0;
		while(!file.eof())
		{
			data1[i]=new char[100];
			file.getline(data1[i],50);
			//data[i][0]=temp;
			//cout<<data1[i];
			i++;
		}
		
		data1[i]=new char[1];
		data1[i]="s";
	}
	else
	{
		cout<<"File not found";
	}
	file.close();
	return data1;	
 }


int main()
{
	char name[20]="B-large.in";
	char **data;
	long double input[110][4];
	data=readInput(name);
	//cout<<sizeof(data);
	setprecision(16);
	cout.unsetf (ios::floatfield);
	cout.setf( std::ios::fixed, std:: ios::floatfield );
	int i=0;
	while(strcmp(data[0],"s"))
	{
		
		int j=0;
		string temp=data[0];
		istringstream iss (temp);
		long double ti;
		while(iss>>ti)
		{			
			input[i][j]=ti;
			//cout<<input[i][j]<<"\t";
			j++;
		}
		//cout<<"\n"<<i<<" --";
		data++;
		i++;
	}
	
	ofstream ofile;
	ofile.open("output.txt");
	ofile.setf( std::ios::fixed, std:: ios::floatfield );
	int len=i-1,flag=1;
	//cout<<"\n len "<<len;
	for (i=1;i<len;i++)
	{
		long double c=input[i][0];
		long double f=input[i][1];
		long double x=input[i][2];
		long double time=0,ntime=0,stime=0;
		long double cr=2;
		flag=1;
		while(flag)
		{	
			//cout<<"\n ss"<<c<<"-"<<f<<"-"<<x;
			if (x<c)
			{
				stime=x/2;
				flag=0;	
			}
			else
			{				
				ntime=stime+c/cr+x/(cr+f);
				time=stime+x/cr;
				//cout<<"\naa"<<time<<"-"<<ntime;
				if (ntime>time)
				{
					flag=0;
					stime=time;
				}
				else
				{
					stime=stime+c/cr;
					cr=cr+f;				
				}
			}
		}		
		//cout<<"\n--"<<stime<<"pp";
		
		ofile<<"Case #"<<i<<": "<<stime<<"\n";
	
		
	}
}
