#include<cstdlib>
#include<fstream>
#include<iostream>
#include<cmath>

using namespace std;

ifstream in ("A-large.in");
ofstream out ("output.txt");

int main()
{
	int t, n, v[10], sum, c, y, x, xmodulo; //passaggio=0
	;
	in>>t;
	
	int risposta[t];
	
	for(int i=0; i<t; i++)
	{
		for(int k=0; k<10; k++)
			v[k]=0;
		
		in>>n;
		risposta[i]=0;
		
		c=n;
		do
		{
			x=n;
			do
			{
				xmodulo=x%10;
				//cout<<xmodulo<<endl;
				//system("PAUSE");
				v[xmodulo]=1;
				x=x/10;
			}while(x>=1);
			
			sum=0;
			
			for(int j=0;j<10; j++)
				sum+=v[j];
			/*
			cout<<endl;	
			for(int p=0; p<10; p++)
				cout<<v[p];
			cout<<endl;
			*/	
			if(sum==10)
				risposta[i]=n;	
			else if(n==0)
				risposta[i]=-1;
			else
			{
				n+=c;
				//cout<<"n,sum"<<n<<" "<<sum<<endl;
				//system("PAUSE");
			}
				
		}while(risposta[i]==0);
		//passaggio++;
		//cout<<"Pass"<<passaggio<<endl<<endl;
	}
	
	for(int i=0;i<t; i++)
	{
		if(risposta[i]==-1)
			out<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		else
			out<<"Case #"<<i+1<<": "<<risposta[i]<<endl;
	}
	
	system("PAUSE");
	return 0;
}
