#include <iostream>

using namespace std;

int main()
{
	long long t,T,r,T2, temp,count;
	cin>>T;
	T2=T;
	while(T2--)
	{
		count=0;
		cin>>r>>t;
		while(true)
		{
			temp=(r+1)*(r+1)-r*r;
			if(temp>t)
				break;
			t=t-temp;
			r+=2;count++;
		}
		cout<<"Case #"<<T-T2<<": ";
		cout<<count<<endl;
	}
}
