#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int t,i,j,c=0,k=0,l=1,cf,m,ct=0;
	char pan[100000],tmp;
	ofstream myfile;
     myfile.open ("output.txt");
	cin>>t;
	while(t--)
	{
		cin>>pan;
		cf=0;
		c=0;
		while(c==0)
		{
			i=0;
			k=0;
			c=1;
			while(pan[i]!='\0')
			{
				if(pan[i]=='-')
					c=0;
				k++;
				i++;
			}
			i=0;
			tmp=pan[0];
			while(pan[i]!='\0')
			{
				if(pan[i]==tmp)
				{
					ct++;
				}
				else
				{
					break;		
				}
				i++;
			}
			i=0;
			for(m=0;m<ct;m++)
			{
				if(tmp=='+')
					pan[m]='-';
				else if(tmp=='-')
					pan[m]='+';		
			}
			cf++;
			ct=0;
		}
		myfile<<"Case #"<<l<<": "<<cf-1<<endl;
		l++;
	}
	myfile.close();
	return 0;
}
