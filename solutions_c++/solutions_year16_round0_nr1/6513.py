#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);
	long long int t,n,j=1,temp,flag,p,o,k;
	cin>>t;
	while(t--)
	{
		cin>>n;
		long int a[10]={0};
		o=n;k=1;p=n;
		temp=0;flag=0;
		while(1)
		{
			if(temp==p){
				flag=1;
				break;
			}
			while(n!=0){
				a[n%10]=1;
				n/=10;
			}
			int i=0;
			for(i=0;i<10;i++)
			{
				if(a[i]==0)break;
			}
			if(i!=10){
				k++;
				n=o*k;
				temp=p;
				p=n;
			}
			else
			if(i==10)break;
		}
	    if(flag==1)cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
	    else
	    if(flag==0)cout<<"Case #"<<j<<": "<<p<<endl;
		j++;
	}
	return 0;
}
