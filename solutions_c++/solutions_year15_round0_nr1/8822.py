#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int number=1;
	ofstream output;
	output.open("output.txt");
	ifstream input("input.txt");
	int text;
	input>>text;
	while(text--)
	{
		string sent;
		int maxim;
		input>>maxim>>sent;
		int l=sent.size();
		int total=0;
		int totalc=0;
		for(int i=0;i<l;i++)
		{
			if(sent[i]!='0')				
			{
				total += sent[i]-'0';
			}
		else if(sent[i]=='0'&&sent[i+1]!='0')
			{
				if(i+1>total)
				{
				totalc += i+1-total;
				total += i+1-total;
				
				}
			  	
			}
			
		}
		output<<"Case #"<<number<<": "<<totalc<<endl;
		number++;
	}
}
