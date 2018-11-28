#include<bits/stdc++.h>
using namespace std;
ifstream fin ("in.txt");
ofstream fout ("out.txt");

int main()
{
	long long int t;
	fin >> t;
	
	for(long long int g=1;g<=t;g++)
	{
		string str;
		fin >> str;
		long long int count=0;
		for(long long int i=str.size()-1;i>=0;i--)
		{
			if(str[i]=='-') 
			{
				for(long long int j=0;j<=i;j++)
				{
					if(str[j]=='+') str[j]='-';
					else str[j]='+';
				}
				count++;
			}	
		}
		fout << "Case #" << g << ": " << count << endl;
	}
	return 0;
}
