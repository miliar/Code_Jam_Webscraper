#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
using namespace std;

int main(int argc, char const *argv[])
{
	ifstream input("A-large.in");
	ofstream output("A-large.out");
	string s;
	bool flag;
	long unsigned int i,j=1,k,ld,no_of_line,no,n=1;
	getline(input,s);
	no_of_line=stoi(s);
	while(getline(input,s))
	{
		string digit[10];
		i=stoi(s);
		if(i==0)
			output<<"Case #"<<to_string(n)<<": INSOMNIA"<<endl;
		else
		{
			for(j=1;j<101;j++)
			{
				no=k=i*j;
				while(k!=0)
				{
					flag=true;
					ld=k%10;
					k=k/10;
					digit[ld]=to_string(ld);
					for(int x=0;x<10;x++)
					{
						if(digit[x].empty()) flag=false;
						// cout<<no<<" : "<<digit[x]<<endl;
					}
					if(flag==true) break;
				}
				if(flag==true)
				{	output<<"Case #"<<to_string(n)<<": "<<to_string(no)<<endl; break;}
			}
		}
		n++;
	}
	input.close();
	output.close();
	return 0;
}