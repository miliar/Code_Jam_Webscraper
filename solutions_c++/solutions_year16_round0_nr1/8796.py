#include<bits/stdc++.h>
using namespace std;
int main()
{
	unsigned long long int n,i,j,x;
	int t,d,y[10],k,flag,test;
	cin>>test;
	i=1;
	for(i=1;i<=test;i++)
	{
		cin>>n;
		flag=1;
		for(j=0;j<10;j++)
			y[j]=0;
		if(n==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		}
		else
		{
			for(j=1;j<=500;j++)
			{
				x=n*j;
				t=x;
				flag=1;
				while(t!=0)
				{
					d=t%10;
					t/=10;
					switch(d)
					{
						case 0:
							y[0]+=1;
							break;
                 				case 1:
							y[1]+=1;
							break;
						case 2:
                                                        y[2]+=1;
							break;
						case 3:
                                                        y[3]+=1;
							break;
						 case 4:
                                                        y[4]+=1;
							break;
						 case 5:
                                                        y[5]+=1;
							break;
						 case 6:
                                                        y[6]+=1;
							break;
						 case 7:
                                                        y[7]+=1;
							break;
						 case 8:
                                                        y[8]+=1;
							break;
						 case 9:
                                                        y[9]+=1;
							break;
					}
				}
				
				for(k=0;k<10;k++)
				{
					if(y[k]==0)
					{	flag=0;
						break;
					}
				}
				if(j==500 && flag==0)
				{
					cout<<"Case #"<<i<<": INSOMNIA"<<endl;
				}				
				if(flag)
				{
					cout<<"Case #"<<i<<": "<<x<<endl;
					break;
					
				}
			}


		}
	
	}
	return 0;	
}
				
