#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;
int main()
{
	ifstream infile;
	infile.open("B-large.in");
	int T;
	infile>>T;
	ofstream outfile;
	outfile.open("large-pancake1.in");
	for(int l=1;l<T+1;)
	{
		char str[100];
		infile>>str;
		fflush(stdin);
		int i;
		for(i=0;;i++)
		{
			if(str[i]=='\0')
				break;
		}
			int ans=0;
			for(int j=i-1;j>=0;j--)
			{
				if(str[j]=='-')
				{
					ans++;
					for(int k=0;k<j;k++)
					{
						if(str[k]=='-')
						{
							str[k]='+';
						}
						else
						{
							str[k]='-';
						}
					}
				}
			}
		outfile<<"Case #"<<l++<<": "<<ans<<endl;
	}
}
