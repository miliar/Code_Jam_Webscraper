#include<iostream>
#include<cstring>
#include<string>
#include<sstream>
#include<fstream>
//#include"header.h"

using namespace std;

char **readInput(char name[50])
 {
 	char **data1=new char*[1100];
 	char temp[50];
	ifstream file;
	file.open(name);
	if (file)
	{
		int i=0;
		while(!file.eof())
		{
			data1[i]=new char[10];
			file.getline(data1[i],50);
			//data[i][0]=temp;
			//cout<<data[i];
			i++;
		}
		
		data1[i]=new char[1];
		data1[i]="s";
	}
	else
	{
		cout<<"File not found";
	}
	return data1;	
 }


int main()
{
	char name[20]="A-small-attempt1.in";
	char **data;
	int input[1100][4];
	data=readInput(name);
	//cout<<sizeof(data);
	int i=0;
	while(strcmp(data[0],"s"))
	{
		
		int j=0;
		string temp=data[0];
		istringstream iss (temp);
		int ti;
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
	
	int len=i-1,m;
	for (i=1,m=1;i<len;i=i+10,m++)
	{
		int count=0,f=i+input[i][0],s=input[i+5][0]+5+i,num=0;
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				if(input[f][j]==input[s][k])
				{
					count++;
					num=input[f][j];
					//cout<<"\n jkjk"<<num<<" "<<count<<f<<s<<input[f][j];
				}	
			}
		}
		if (count==1)
		{
			ofile<<"Case #"<<m<<": "<<num<<"\n";
		}
		else if (count==0)
		{
			ofile<<"Case #"<<m<<": "<<"Volunteer cheated!\n";
		}
		else
		{
			ofile<<"Case #"<<m<<": "<<"Bad magician!\n";
		}
	}
}
