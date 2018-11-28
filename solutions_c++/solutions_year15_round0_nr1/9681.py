#include<iostream>

using namespace std;

int check(int* st,int n)
{int sum=0;
	for(int i=0;i<n;i++)
	{
		sum=sum+st[i];
	}
	return sum;
}
int maxi(int x,int y)
{
 if(x>y)return x;
 else return y;
}

int main()
{
	int t;
	cin>>t;
	int q=1;
	while(q<=t)
	{
		int max;
		int add=0;
		cin>>max;
		char s[max+1];
		for(int i=0;i<max+1;i++)
		cin>>s[i];
		int st[max+1];
		for(int i=0;i<max+1;i++)
		{
			st[i]=s[i]-48;
		}
		//cout<<check(st,max+1);
		if(max==0)
		cout<<"Case #"<<q<<" : 0"<<endl;
		else
		{
			for(int i=0;i<max+1;i++)
			{add=maxi(add,i-check(st,i));}
			if(add<0)add=0;
			cout<<"Case #"<<q<<": "<<add<<endl;
		}
	q++;
	}
	return 0;
}

			

