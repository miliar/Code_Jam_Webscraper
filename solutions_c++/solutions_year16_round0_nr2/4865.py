#include<fstream>
#include<iostream>
using namespace std;
int M=0;
int check(char ch[])
{
	for(int i=0;ch[i]!='\0';i++)
	{
			if(ch[i]!='+')
				return 1;			
	}
		return 0;
}
void flip_happy(char ch[])
{
		for(int i=0;ch[i]=='+';i++)
				ch[i]='-';
	
}
void flip_sad(char ch[])
{
		for(int i=0;ch[i]=='-';i++)
				ch[i]='+';
}	
int main()
{
	int T;char ch[10];int j;int m;
	ifstream fin("B-small-attempt0.in",ios::in);
	ofstream fout("Output.txt",ios::app);
	if(!fin)
	{
			cout<<"ERROR!";
	}
	fin>>T;
	for(int i=0;i<T;i++)
	{
		j=0;
		fin>>ch;
  		while(j!=1)
		{
			m=check(ch);
			if(m==1)
			{
				M++;
				if(ch[0]=='+')	{		flip_happy(ch);		}
				else			{		flip_sad(ch);		}
			}
			else
			{
				fout<<"Case #"<<i+1<<": "<<M<<"\n";
				M=0;
				j=1;	
			}	
		}
	}	
	fin.close();
	fout.close();
	return 0;
}
