#include<cstdio>
#include<iostream>
using namespace std; 
int main() 
{

	freopen("input.txt","r",stdin);
	freopen("answer.txt","w",stdout);
	long i,X,R,C,w,t;
	cin>>t;
	for(i=0;i<t;i++)
	{
	    cin>>X>>R>>C;
	    if(X==2)
		{
		      if(R==1&&C==3||R==1&&C==1||R==3&&C==3||R==3&&C==1)
	              w=2;
	          else
	              w=1;
		}
		else if(X==3)
		{
			  if(R==1||C==1)
	                    w=2;
	                else if(R==3||C==3)
	                    w=1;
	                else
	                    w=2;
		}
		else if(X==4)
		{
			  if(R==4&&C==4||R==3&&C==4||R==4&&C==3)
	              w=1;
	          else 
	              w=2;
	    }
	    else
	    	  w=1;
	    if(w==1)
	        cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
	    else
	        cout<<"Case #"<<i+1<<": RICHARD"<<endl;
	}
	return 0;
}


