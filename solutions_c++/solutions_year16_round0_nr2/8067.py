#include <stdio.h>
#include <fstream>
#include <string.h>
using namespace std;
int main()
{
	long n;
	ifstream myfile;
	ofstream myfile1;
	myfile.open ("B-large.in");
	myfile>>n;
	myfile1.open("Output1");
	int t= n;
	while(n--)
	{
		char s[110];
		myfile>>s;
		char temp,tempo;
		int ans=0,flag = 1;
		while(true)
		{
			int i;
			flag =1;
			for(i=0;i<strlen(s);i++)
			{
				if(s[i]=='-')
				{
					flag =0;
				}
			}
			if(flag ==1)
			{
				myfile1<<"Case #"<<(t-n)<<": "<<ans<<endl;
				break;
			}
			else
			{
				temp = s[0];
				if(temp=='-')
				{
					tempo = '+';
				}
				else tempo = '-';
				i=0;
				while(s[i]==temp)
				{
					s[i]=tempo;
					i++;
				}
				ans++;
			}
		}
		
	}	
	myfile1.close();
	myfile.close();
}