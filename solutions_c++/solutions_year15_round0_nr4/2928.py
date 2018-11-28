#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main() 
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);

	int t1=0,t,X,R,C;
	char win;
	cin>>t;
	while(t1++<t)
	{
		cin>>X>>R>>C;
		if(X==1)
		{
			win='g';
		}
		else if(X==2)
		{
			if(R==1&&C==1||R==1&&C==3||R==3&&C==1||R==3&&C==3)
	            win='r';
	        else
	            win='g';
		}
		else if(X==3)
		{
			if(R==1||C==1)
	            win='r';
	        else if(R==3||C==3)
	            win='g';
	        else
	            win='r';
		}
		else
		{
			if(R==4&&C==4||R==4&&C==3||R==3&&C==4)
	            win='g';
	        else 
	            win='r';
		}
	    if(win=='g')
	    	cout<<"Case #"<<t1<<": "<<"GABRIEL"<<endl;   
	    else
	        cout<<"Case #"<<t1<<": "<<"RICHARD"<<endl;
	}
	return 0;
}

