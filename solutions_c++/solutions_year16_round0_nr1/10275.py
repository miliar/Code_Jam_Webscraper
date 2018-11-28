#include <iostream>
#include <bitset>
using namespace std;

int main()
{
	int t,n;
	cin>>t;
	for(int cnt=1;cnt<=t;cnt++)
	{
		cin>>n;
		std::bitset <10> ar;
		ar.reset();
		int c=1,num=n;
		while(c!=1000)
		{
			int last = num;
			while(num!=0)
			{
				ar.set(num%10,1);
				num=num/10;
			}
			if(ar.all())
			{
				cout<<"Case #"<<cnt<<": "<<last<<endl;;
				break;
			}
			else
			{
				c++;
				num=c*n;
			}
		}
		if(c==1000)
			cout<<"Case #"<<cnt<<": INSOMNIA"<<endl;
	}
	return 0;
}
