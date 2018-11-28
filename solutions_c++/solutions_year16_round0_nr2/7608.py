#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int check (string a,int size);
void flip(string& a,int size);
bool check2(string& a,int size);

int main ()
{
	string line;
	//ifstream inFile ("input.txt");
	ifstream inFile ("B-large.in");
	ofstream outFile ("output.txt");

	getline (inFile,line);
	int n = std::stoi (line);
	int count,j;

	for(int i=0;i<n;i++)
	{
		count=0;
		getline (inFile,line);
		j=check(line,line.size());
		while(j!=-1)
		{
			if(check2(line,j+1))
			{
				count++;
				continue;
			}
			if(line[0]=='+' && line[j]=='-' )
			{
				line[0]='-';
				count++;
				continue;
			
			}
			flip(line,j+1);
			j=check(line,line.size());
			count++;
		}
		outFile<<"Case #"<<i+1<<": "<<count<<endl;
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	
	outFile.close();
	inFile.close();

	getchar();
}

int check (string a, int size)
{
	for(int i=size-1;i>=0;i--)
	{
		if(a[i]=='-')
			return i;
	}
	return -1;
}

void flip(string& a,int size)
{
	for(int i=0;i<size/2;i++)
	{
		char temp=a[i];
		a[i]=a[size-i-1];
		a[size-i-1]=temp;
	}

	for(int i=0;i<size;i++)
	{
		if(a[i]=='-')
			a[i]='+';

		else
			a[i]='-';
	}
}

bool check2(string& a,int size)
{
	int count1=0,count2=0,i=0;
	char c=a[0];
	while(c=='+')
	{
		count1++;
		
		c=a[++i];
	}

	while(c=='-' && count2<count1)
	{
		count2++;
		if(i+1>=size)
			break;
		c=a[++i];
	}
	if(count1!=0)
	{
		for(int i=0;i<count1;i++)
		a[i]='-';

		return true;
	}
	return false;
}