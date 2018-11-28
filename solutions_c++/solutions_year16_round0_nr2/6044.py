#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;
int main()
{
	long long int t_c,i,l,j,op,k,s;
	char str[101],a;
	ifstream input;
	ofstream output;
	input.open("B-large.in");
	output.open("output_pancakes.out");
	input>> t_c;
	for(i=1;i<=t_c;i++)
	{
		input>> str;
		l=strlen(str);
		for(j=0;j<l;j++)
		{
			if(str[j]!='+')
				break;
		}
		op=0;
		if(j!=l)
		{
		while(j!=l)
		{
			k=1;
			
			a=str[0];
			while(a==str[k] && k<l )
			{
				k++;
			}
			for(s=0;s<=k-1;s++)
			{
				if(a=='+')
					str[s]='-';
				else
					str[s]='+';
			}
			
			for(j=0;j<l;j++)
			{
				if(str[j]!='+')
					break;
			}
			op++;
		}	
		output <<"Case #"<<i<<": "<<op<<"\n"; 
		}
		else
			output <<"Case #"<<i<<": "<<op<<"\n";
	
	}

input.close();
output.close();

return 0;
}