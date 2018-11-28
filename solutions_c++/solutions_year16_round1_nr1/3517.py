#include<iostream>
#include<string.h>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		char S[1001];
		cin>>S;
		
		int len=strlen(S);
		
		char last[len+1],temp[len+1];

		memset(last,'\0',len+1);
		last[0]=S[0];
		int j;
		for(j=1;j<len;j++)
		{
			

			if(S[j]<last[0])
			{
				last[j]=S[j];
			}
			else if(S[j]>=last[0])
			{
				memset(temp,'\0',len+1);
				strcpy(temp,last);
				memset(last,'\0',len+1);
				last[0]=S[j];
				strcat(last,temp);
			}
		}
		last[j]='\0';
		cout<<"Case #"<<i+1<<": "<<last<<endl;
	}
}
