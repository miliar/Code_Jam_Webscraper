#include<iostream>
using namespace std;

int main()
{
	char frac[100];
	int t,i,f,j,n2[10]={2,4,8,16,32,64,128,256,512,1024};
	long int g,p,q;
	cin>>t;
	for(i=0;i<t;i++)
	{
		p=0;
		q=0;
		g=0;
		j=0;
		cin>>frac;
		while(frac[j]!='/')
		{
			p=p*10+(frac[j++]-48);
		}
		j++;
		while(frac[j]!='\0')
		{
			q=q*10+(frac[j++]-48);
		}
		
		f=0;
		j=0;
		while(j<10)
		{
			if(n2[j++]==q)
			{
				f=1;
				break;
			}	
		}
		if(f==1)
		while(1)
		{
			if((2*p/q-1)>=0)
			{
				
				g++;
				break;
			}
			else
			{
				g++;
				p*=2;	
			}
		}
		if(g>0)
			cout<<"Case #"<<i+1<<": "<<g<<"\n";
		else
			cout<<"Case #"<<i+1<<": impossible\n";
	}
	return 0;
}
