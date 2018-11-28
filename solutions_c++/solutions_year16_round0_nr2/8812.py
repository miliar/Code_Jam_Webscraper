#include<iostream>
#include<cstring>
using namespace std;
main()
{
	int a,b,c=0,n,k,d,e,kk=1;		
	cin>>n;
	do{
		d=0;
		string z;
			cin>>z;
		a=z.length();
		if(a>=2){
		while(1)
		{
			e=0;
			for(int l=0;l<a;l++)
			{
				if(z[l]=='+')
				{
					e++;
				}
			}
			for(int i=0;i<a;i++)
			{
				if(z[i]=='-')
				{
					k=i;
				}
			}
			if(e==a)
			{
				cout<<"Case #"<<kk<<": "<<d<<endl;
				kk++;
				break;
			}
			else
			{
				for(int j=0;j<=k;j++)
				{
					if(z[j]=='+')
					{
						z[j]='-';
					}
					else
					{
						z[j]='+';
					}
				}
				d++;
			}
		}
	}
	else{
			if(z[0]=='-')
			{	
				cout<<"Case #"<<kk<<": "<<a<<endl;
				kk++;
			}
			else
			{
				cout<<"Case #"<<kk<<": "<<a-1<<endl;
				kk++;
			}
		}
		c++;
	}while(c!=n);
}
