#include<iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output","w",stdout);
	int t;
	cin>>t;
	for(int k=0;k<t;k++)
	{
		int i=1,n,check[10]={0},num,get,o,count=0;
		cin>>n;
		o=n;
		if(n==0)cout<<"Case #"<<k+1<<": INSOMNIA"<<endl;
		else{
		while(i>0)
		{
			num=i*o;
			n=num;
			//cout<<num<<endl;
			get=num;
			while(num>0)
			{
			num=num%10;
				if(check[num]==0)
					{
						count++;
						check[num]=1;
					}
			n=n/10;
			num=n;
				if(count==10)break;
			}
			i++;
			
			if(count==10){
				cout<<"Case #"<<k+1<<": "<<get<<endl;
				break;
			}
		}
		}
	}
	return 0;
}
