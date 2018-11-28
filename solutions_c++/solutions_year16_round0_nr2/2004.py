#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;



int main()
{
	int T;
	ifstream fin("B-large.in");
	ofstream fout("B.large.out");

	fin>>T;
	for(int n=1;n<=T;n++)
	{
		char str[101];
		fin>>str;
		int l=strlen(str);
		if(l<=0)
		{
			fout<<"Case #"<<n<<": 0"<<endl;
			continue;
		}
		int count=0;
		while(true)
		{
			int i;
			for(i=l-1;i>=0;i--)
			{
				if(str[i]=='-')
					break;
			}
			if(i<0)
			{
				break;
			}
			if(str[0]=='-')
			{
				int j;
				for(j=0;j<=i;j++)
				{
					if(str[j]=='+')
						break;
				}
				for(int k=0;k<j;k++)
				{
					str[k]='+';
				}
				count++;
			}
			else
			{
				int j;
				for(j=0;j<=i;j++)
				{
					if(str[j]=='-')
						break;
				}
				for(int k=0;k<j;k++)
				{
					str[k]='-';
				}
				count++;
			}
		}
		fout<<"Case #"<<n<<": "<<count<<endl;
	}
	fout.close();
	fin.close();

	return 0;
}