#include<iostream>
using namespace std;

int main()
{
	int a[16],b[16],X,Y,T,i,co;
	cin>>T;
	int ans[T];
	i=0;
	while(i<T)	
	{	
		co=0;
		cin>>X;
		cin>>a[0]>>a[1]>>a[2]>>a[3];
		cin>>a[4]>>a[5]>>a[6]>>a[7];
		cin>>a[8]>>a[9]>>a[10]>>a[11];
		cin>>a[12]>>a[13]>>a[14]>>a[15];
		
		cin>>Y;
		cin>>b[0]>>b[1]>>b[2]>>b[3];
		cin>>b[4]>>b[5]>>b[6]>>b[7];
		cin>>b[8]>>b[9]>>b[10]>>b[11];
		cin>>b[12]>>b[13]>>b[14]>>b[15];
		
		X*=4;
		Y*=4;
		X-=4;
		Y-=4;
		for(int q=X;q<X+4;q++)
		{
			for(int w=Y;w<Y+4;w++)
			{	
				if(a[q]==b[w] && co!=0)
				{
					co=99;
					ans[i]=99;
				}
				if(a[q]==b[w] && co==0)
				{
					ans[i]=a[q];
					co=1;
				}
			}
		}
		if(co!=99 && co!=1)
		{
			ans[i]=999;
			
		}
		i++;
	}
	i=0;
	
	while(i<T)
	{
		cout<<"Case #"<<i+1<<": ";
		if(ans[i]<17 && ans[i]>0)
			cout<<ans[i];
		else if(ans[i]==99)
			cout<<"Bad magician!";
		else if(ans[i]==999)
			cout<<"Volunteer cheated!";
		cout<<endl;
		i++;
	}
	return 0;
}

