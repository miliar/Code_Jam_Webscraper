#include <bits/stdc++.h>
using namespace std;
int main()
{
	int cas;
	cin>>cas;
	for(int t=1;t<=cas;t++)
	{
		int x,r,c;
		cin>>x>>r>>c;
		if(r>c){int k=r;r=c;c=k;}
		cout<<"Case #"<<t<<": ";
		if(x==1)
		{
			cout<<"GABRIEL"<<endl;
		}
		if(x==2)
		{
			if(r%2==1&&c%2==1)
				cout<<"RICHARD"<<endl;
			else
				cout<<"GABRIEL"<<endl;
		}
		if(x==3)
		{
			if((r==2&&c==3)||(r==3&&c==4)||(r==3&&c==3))
				cout<<"GABRIEL"<<endl;
			else
				cout<<"RICHARD"<<endl;
		}
		if(x==4)
		{
			if((r==3&&c==4)||(r==4&&c==4))
				cout<<"GABRIEL"<<endl;
			else
				cout<<"RICHARD"<<endl;
		}
	}
	return 0;
}
