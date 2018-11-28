#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int main()
{
	int T;
	char form[11];
	memset(form,'\0',10);
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		int N;
		cin>>N;
		cin.ignore();
		if(N<=0)
		{
			cout<<"Case #"<<i<<": INSOMNIA"<<"\n";
			continue;
		}
		int j=1,l=0;
		while(1)
		{
			int UpN=N*j;
			int last=UpN;
			while(UpN>0)
			{
				int present=0;
				int digit = UpN%10;
    			UpN /= 10;
    			char sd=(char)digit+48;
       			for (int k=0;k<strlen(form);k++)
    			{
    				if (form[k]==sd)
    				{
    					present=1;
    					break;
    				}
    			}
    			if(present==0)
    			{
    				form[l]=sd;
    				l++;
    			}
			}
			if(l==10)
			{
				l=0;j=1;
				cout<<"Case #"<<i<<": "<<last<<"\n";
				memset(form,'\0',10);
				break;
			}
			j++;
		}
	}
	return 1;
}