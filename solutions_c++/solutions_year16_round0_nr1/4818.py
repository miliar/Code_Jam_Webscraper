#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	int T,N,t=1,temp,d,c,num;
	cin>>T;
	while(t<=T)
	{
		cin>>N;
		vector<bool> B(10,false);
		c = 0;
		if(N==0)
		{
			cout<<"Case #"<<t<<": INSOMNIA"<<endl;
		}
		else
		{
			num = 0;
			for(int i=1;i<1000;i++)
			{
				num += N;
				temp = num;
				while(temp>0)
				{
					d = temp%10;
					if(B[d]==false)
					{
						B[d]=true;
						c++;
					}
					temp/=10;
				}
				if(c==10)
					break;
			}
			if(c==10)
				cout<<"Case #"<<t<<": "<<num<<endl;
			else
				cout<<"Case #"<<t<<": INSOMNIA"<<endl;
		}
		t++;
	}
	return 0;
}