#include <iostream>
using namespace std;

int main() {
	unsigned long long int t,n;
	cin>>t;
	bool check[10];
	unsigned long long int y=1,copy;
	unsigned long long int sec;
	while(t--)
	{	for(int i=0;i<10;i++)
		{
			check[i]=false;
		}
		cin>>n;
		copy=n;
		sec=n;
		bool fin=false;
		int count=0;
		int d;
		while(!fin && n!=0)
		{	copy=n;
			while(copy>0)
		{
			d=copy%10;
			if(!check[d])
			{	count++;
				check[d]=true;
			}
			copy/=10;
			if(count==10)
				fin=true;
		}
		n+=sec;
		}
		n-=sec;
		if(n==0)
			cout<<"Case #"<<y<<": INSOMNIA"<<endl;
		else
			cout<<"Case #"<<y<<": "<<n<<endl;
		y++;	
	}
	return 0;
}