#include <iostream>
using namespace std;

int main() {
	int t,n,i,num,count,cnt,x,j;
	cin>>t;
	for(j=1;j<=t;j++)
	{	
		count=0;i=1;
		int a[10]={0};
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<j<<": INSOMNIA"<<endl;
			continue;
		}
		while((count!=10)&&(n*i<1000000000)){
			
			cnt=count;
			num=n*i++;
			while(num!=0){
				x=num%10;
				//cout<<a[x]<<endl;
				num=num/10;
				if(a[x]==0)
				{	//cout<<"yes";
					a[x]=1;
					count++;
				}
			}
		}
		if(count==10)
		 cout<<"Case #"<<j<<": "<<n*(i-1)<<endl;
		 else
			cout<<"Case #"<<j<<": INSOMNIA"<<endl;
	}
	return 0;
}
