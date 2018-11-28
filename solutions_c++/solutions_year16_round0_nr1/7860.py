#include<iostream>
#include<stdlib.h>
using namespace std;
int main ()
{
	int i=0,k,f=0,numb,t=0,rep,nf;
	char n[20];
	cin>>rep;
	for (int count=0;count<rep;count++)
	{
		bool n0=false,n1=false,n2=false,
		n3=false,n4=false,n5=false,
		n6=false,n7=false,n8=false,
		n9=false,ok=false;
		cin>>n;	
		numb=atoi(n);
		nf=numb;
		t=0;
		do
		{
		k=0;
			while (n[k])
			{	
				switch (n[k])
				{
				case '0':{n0=true;break;}
				case '1':{n1=true;break;}
				case '2':{n2=true;break;}
				case '3':{n3=true;break;}
				case '4':{n4=true;break;}
				case '5':{n5=true;break;}
				case '6':{n6=true;break;}
				case '7':{n7=true;break;}
				case '8':{n8=true;break;}
				case '9':{n9=true;break;}																	
				}
			k++;
			}
			t++;
			if (n1&&n2&&n3&&n4&&n5&&n6&&n7&&n8&&n9&&n0)
			{
				ok=true;
				break;
			}
			else
				numb=nf*t;
			if (t>1000000)
				break;
			itoa(numb,n,10);
		}while (!(n1&&n2&&n3&&n4&&n5&&n6&&n7&&n8&&n9&&n0));
		i++;
		cout<<"Case #"<<i<<": ";
		if (ok)
			cout<<numb<<endl;
		else
			cout<<"INSOMNIA"<<endl;
	}
	return 0;
}