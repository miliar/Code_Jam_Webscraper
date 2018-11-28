#include<iostream>
using namespace std;
int main()
{	


	freopen("A-large.in","r",stdin);
	freopen("A-small123.out","w",stdout);
	
	long long q,t,i,n,d,m,j,p;
 	cin>>t;
 	for(q=0;q<t;q++)
 	{
 		int a[10]={0};
 		int flag=2;
 		cin>>n;p=n;
 		i=1;
 		while(1)
 		{
 		n=p*i;
 		m=n;
 		while(m>0)
 		{
 			d=m%10;
 			a[d]++;
 			m=m/10;
 		}
 		for(j=0;j<10;j++)
 		{
 			if(a[j]==0)
 			{
   			 flag=0;break;
 			}
 			else
 			flag=1;
 		}
 		if(flag==1)
 		break;
 		else
 		{
 			if(n==0)
 			break;
 			i++;
 		}
 			
 		}
 		if(n==0)
 		cout<<"Case #"<<q+1<<":"<<" INSOMNIA"<<endl;
 		else
 		cout<<"Case #"<<q+1<<": "<<n<<endl;
 	}



}

