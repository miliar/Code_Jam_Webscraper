#include <bits/stdc++.h>		//ry

using namespace std;

int main()
{
	int test,t,X,R,C;
	char win;
	
	cin>>test;
	
	for(t=1;t<=test;t++)
	{
	    cin>>X>>R>>C;
	    
	    switch(X)
	    {
	        case 1:
	                win='g';break;
	        case 2:
	                if(R==1&&C==1||R==1&&C==3||R==3&&C==1||R==3&&C==3)
	                    win='r';
	                else
	                    win='g';break;
	        case 3:
	                if(R==1||C==1)
	                    win='r';
	                else if(R==3||C==3)
	                    win='g';
	                else
	                    win='r';break;
	        case 4:
	                if(R==4&&C==4||R==4&&C==3||R==3&&C==4)
	                    win='g';
	                else 
	                    win='r';
	    }
	    
	    if(win=='g')
	        
	        cout<<"Case #"<<t<<": GABRIEL\n";
	    else
	        cout<<"Case #"<<t<<": RICHARD\n";
	}
	
	return 0;
}

