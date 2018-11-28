#include <iostream>
#include<cmath>
using namespace std;

int main() {
	int t,count=1;
	cin>>t;
	while(t!=0)
	{
		int p,q,i,ans=0;
		char c;
		cin>>p;
		cin>>c;
		cin>>q;
		if(q%2==1)
		{
			cout<<"Case #"<<count<<":"<<" impossible"<<endl;
		}
		else
		{
			float num;
			num=float(p)/q;
			while(num<1)
			{
				num=num*2;
				ans++;
			}
			cout<<"Case #"<<count<<": "<<ans<<endl;
		}
		t--;
		count++;
	}
	return 0;
}