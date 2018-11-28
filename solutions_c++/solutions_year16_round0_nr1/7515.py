#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool check(bool* a);

int main ()
{
	string line;
	ifstream inFile ("A-large.in");
	ofstream outFile ("output.txt");

	getline (inFile,line);
	int n = std::stoi (line);

	for(int i=0;i<n;i++)
	{
		getline (inFile,line);
		int x = std::stoi (line);
		int count=2;
		int base=x;
		if(x==0)
		{
			outFile<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		bool buffer[10];
		for(int i=0;i<10;i++)
			buffer[i]=false;

		while(check(buffer)==false)
		{
			int temp=x;
			while(temp!=0)
			{
				buffer[temp%10]=true;
				temp=temp/10;
			}
			x=base*count;
			count++;
		}
		outFile<<"Case #"<<i+1<<": "<<x-base<<endl;
	}

	outFile.close();
	inFile.close();

	getchar();
}

bool check(bool* a)
{
	for(int i=0;i<10;i++)
	{
		if(a[i]==false)
			return false;
	}
	return true;
}