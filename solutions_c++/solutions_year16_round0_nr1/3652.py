#include <iostream>
using namespace std;

int main() {
	long long int T,t,n,b,i,j,a[10],r,check=1,flag,temp;
	cin>>T;
	for(t=1;t<=T;t++)
	{	
		for(i=0;i<10;i++)
			a[i]=100;
		
		check=1;
		i=1;
		cin>>n;
		if(n==0)
		{	flag=0;
			check=0;
			cout<<"Case #"<<t<<": INSOMNIA \n";
		}
			
		while(check==1)
		{
			flag=1;
			b=i*n;
			temp=b;
			//cout<<temp<<endl;
			while(b!=0)
			{
				r=b%10;
				a[r]=r;
				b=b/10;
			}
			for(j=0;j<10;j++)
			{	if(a[j]==100)
					{
						check=1;
						break;
					}
				else check=0;
			}
			i++;
		}
		if(flag==1)cout<<"Case #"<<t<<": "<<temp<<endl;
	}
	return 0;
}