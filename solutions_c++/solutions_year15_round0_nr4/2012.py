/* Cases solved using pen and paper */
#include <iostream>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		int x,r,c;
		bool flag;	//0 gabriel
		cin>>x>>r>>c;
		if(x > r && x > c)
			flag = 1;
		else if(x == 1)
			flag = 0;
		else if(x == 2)
		{
			if((r*c)&1)
				flag = 1;
			else
				flag = 0;
		}
		else if(x == 3)
		{
			if(r*c == 3) //1*3
				flag = 1;
			else if(r*c == 6) //2*3
				flag = 0;
			else if(r*c == 9) //3*3
				flag = 0;
			else if(r*c == 4) //1*4
				flag = 1;
			else if(r*c == 8) //2*4
				flag = 1;
			else if(r*c == 12) //3*4
				flag = 0;
			else if(r*c == 16) //4*4
				flag = 1;
			else
				cout<<"HELLO1"<<endl;
		}
		else if(x == 4)
		{
			if(r*c == 4) //1*4
				flag = 1;
			else if(r*c == 8) //2*4
				flag = 1;
			else if(r*c == 12) //3*4
				flag = 0;
			else if(r*c == 16) //4*4
				flag = 0;
			else
				cout<<"HELLO2"<<endl;
		}
		if(flag)
			cout<<"Case #"<<t<<": RICHARD"<<endl;
		else
			cout<<"Case #"<<t<<": GABRIEL"<<endl;
	}
}