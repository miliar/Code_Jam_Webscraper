#include<iostream>
using namespace std;
int main()
{
	int t;
	cin >>t;
	for (int y=0;y<t;y++)
	{
		int x,r,c;
		cin >>x>>r>>c;
		if (x==4)
		{
			if (r==4&&c==4)         cout <<"Case #"<<y+1<<": "<<"GABRIEL";
			else if (r==4&&c==3)    cout <<"Case #"<<y+1<<": "<<"GABRIEL";
			else if (r==3&&c==4)    cout <<"Case #"<<y+1<<": "<<"GABRIEL";
			else                    cout <<"Case #"<<y+1<<": "<<"RICHARD";
		}
		else if (x==3)
		{
			if 		(r==2&&c==3)    cout <<"Case #"<<y+1<<": "<<"GABRIEL";
			else if (r==3&&c==2)    cout <<"Case #"<<y+1<<": "<<"GABRIEL";
			else if (r==3&&c==3)    cout <<"Case #"<<y+1<<": "<<"GABRIEL";
			else if (r==3&&c==4)    cout <<"Case #"<<y+1<<": "<<"GABRIEL";
			else if (r==4&&c==3)    cout <<"Case #"<<y+1<<": "<<"GABRIEL";
			else       				cout <<"Case #"<<y+1<<": "<<"RICHARD";
		}
		else if (x==2)
		{
			if (r%2!=0&&c%2!=0)     cout <<"Case #"<<y+1<<": "<<"RICHARD";
			else                    cout <<"Case #"<<y+1<<": "<<"GABRIEL";
		}
		else if (x==1)              cout <<"Case #"<<y+1<<": "<<"GABRIEL";
		cout <<"\n";
	}
	system ("pause");
    return 0;
}
