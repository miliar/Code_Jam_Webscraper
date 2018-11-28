#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin;
	ofstream fout;
	fout.open("input.txt");
	fin.open("B-large.in");
	int counter;
	fin>>counter;
	int i=1;
	string strrr;
	getline(fin,strrr);
	while(i<=counter)
	{
	    string str;
		getline(fin,str);
		int j=str.length()-1;
		int c=0;
		while(j>=0)
		{
			if(str[j]=='-')
			{
				int k=j;
				while(k>=0)
				{
				  if(str[k]=='+')
				  {
				  	str[k]='-';
				  	
					  }	
					  else
					  {
					  	str[k]='+';
					  	
					  }
					  k--;
				}
				c++;
			}
			j--;
			}	
			fout<<"Case #"<<i<<": "<<c<<endl;
		i++;
	}
}
