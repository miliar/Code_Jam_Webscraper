#include<iostream>
using namespace std;
main()
{
	int a,b,c=0,n,d,k,l,i,kk=1;
	int z[]={0,1,2,3,4,5,6,7,8,9};			
	cin>>n;
	do{
					i=0;
			d=0;
		cin>>a;
		if(a==0)
		{	
			cout<<"Case #"<<kk<<": "<<"INSOMNIA"<<endl;
			kk++;
		}
		else
		{
			while(1)
			{
				k=a*i;
				while(k>0)
				{
					b=k%10;
					for(int j=0;j<=9;j++)
					{
						if(z[j]==b)
						{
						z[j]=-1;
						d++;
						}
					}
					k=k/10;
				}
				if(d==10){
					cout<<"Case #"<<kk<<": "<<a*i<<endl;
					kk++;
					break;
					}
			i++;
			}
		}
		for(int w=0;w<=9;w++)
					{
						z[w]=w;
					}
		c++;
	}while(c!=n);
}
