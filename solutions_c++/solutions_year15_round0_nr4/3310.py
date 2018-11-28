#include<iostream>
#include<fstream>
using namespace std;
#define cin fin
#define cout fout

int main()
{
	ifstream fin("Hello.in");
	ofstream fout ("out.out");
	int t;
	cin>>t;
	int j=1;
	while(j!=t+1)
	{
		int X,R,C;
		cin>>X;
		cin>>R;
		cin>>C;
		int RC=R*C;
		if(X==1)
		{
			cout<<"Case #"<<j<<": "<<"GABRIEL\n";
            j++;
		}
		else if(X==2)
		{
			if( (RC)%2==0)
			{
				cout<<"Case #"<<j<<": "<<"GABRIEL\n";
				j++;
			}
			else
			{
				cout<<"Case #"<<j<<": "<<"RICHARD\n";	
				j++;
			}
		}
		else if(X==3)
		{
			if((RC)%3!=0)
			{
				cout<<"Case #"<<j<<": "<<"RICHARD\n";
				j++;
			}
			switch(RC)
			{
				case 6:
				case 9:
				case 12: cout<<"Case #"<<j<<": "<<"GABRIEL\n";j++;break;
				case 3 : cout<<"Case #"<<j<<": "<<"RICHARD\n";j++;break;
			}
		}
		else if(X==4)
		{
			if(RC%4!=0)
			{
				cout<<"Case #"<<j<<": "<<"RICHARD\n";
				j++;
			}
			switch(RC)
			{
				case 4:
				case 8: cout<<"Case #"<<j<<": "<<"RICHARD\n";j++;break;
				case 12: 
				case 16 :cout<<"Case #"<<j<<": "<<"GABRIEL\n";j++;break;
			}
		}
	
	}
	return 0;
}

