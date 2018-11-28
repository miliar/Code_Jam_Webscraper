#include<iostream>
using namespace std;
int main()
{freopen("input.txt","r",stdin);
freopen("myfile.txt","w",stdout);
	long long n,i,w,d,q,k,p,x;
 	cin>>n;
 	int aa=1;
 	for(x=0;x<n;x++)
 	{
 		int b[10]={0};
 		int flag=2;
 		cin>>w;p=w;
 		i=1;
 		while(1)
 		{
 		w=p*i;
 		q=w;
 		while(q>0)
 		{
 			d=q%10;
 			q=q/10;
 			b[d]++;
 		}
 		for(k=0;k<10;k++)
 		{
 			if(b[k]==0)
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
 			if(w==0)
 			break;
 			i++;
 		}
 			
 		}
 		if(w==0)
 		cout<<"Case #"<<aa<<": "<<"INSOMNIA"<<endl;
 		else
 		cout<<"Case #"<<aa<<": "<<w<<endl;
 		aa++;
 	}



}

