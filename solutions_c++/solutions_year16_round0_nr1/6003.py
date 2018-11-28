#include <bits/stdc++.h>
using namespace std;
typedef pair<int,bool> ii;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("dp.txt","w",stdout);
	long long x;
	cin>>x;
	long long a,b,c,d;
	for(long long y=1;y<=x;y++)
	{	
		cin>>a;
		cout<<"Case #"<<y<<": ";
		b=a;
		if(a==0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		bool ar[11]={0};
		while(1)
		{
			c=a;
			//if(ar[0] and ar[1]and ar[2]and ar[3]and ar[4]and ar[5]and ar[6]and ar[7]and ar[8]and ar[9])break;
			while(c!=0)
			{
				d=c%10;
				ar[d]=true;
				c=c/10;
			}
			if(ar[0] and ar[1]and ar[2]and ar[3]and ar[4]and ar[5]and ar[6]and ar[7]and ar[8]and ar[9])break;
			a+=b;
		}
		cout<<a<<endl;
	}
}