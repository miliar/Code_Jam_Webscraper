#include<iostream>
#include<conio.h>
using namespace std;

int main()
{
	int t;
	char s[102];
	cin>>t;
	int x=0;
	while(t--)
	{
	x++;	
	cin>>s;
	int i=0;
	while (s[i]!='\0')
	{
    i++;
	}
	int temp=i,count=0;
	while(i--)
	{
		//cout<<"i:"<<i;
			if(s[i]=='-')
			{
				count++;
						for(int j=0;j<=i+1;j++)
						{
						if(s[j]=='+')
							s[j]='-';
						else
						s[j]='+';
						}
			}
			
	}
cout<<"Case #"<<x<<": "<<count<<endl;
	/*
	char *data=(char*)malloc(i*sizeof(char));

	strcpy(data,s);
	cout<<data<<sizeof(data);
	*/
	}
	getch();
return 0;
}