
#include<iostream>
#include<stdio.h>
using namespace std;
main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("OminOut.txt", "w", stdout);
    int t,check,temp;
    int X,R,C;
	cin>>t;
	temp=1;
	while(t--)
	{
		cin>>X>>R>>C;

		if((R*C)%X!=0||(X>C&&X>R))
        {

		check=0;

        }

		else
		{
			if((X>2) && (X%2==0) && (R==X/2 || C==X/2) && (X==R || X==C))
			{
				check=0;
			}
			else
			{
			  if(X%2==1)
			  X++;
			  X=X/2;
			  if(X>R||X>C)
			  {
			   check=0;
		      }
			  else
			  {
			    check=1;
		      }
		    }
		}

		if(check==0)
		cout<<"Case #"<<temp<<":"<<" "<<"RICHARD"<<"\n";
		else
		cout<<"Case #"<<temp<<":"<<" "<<"GABRIEL"<<"\n";
		temp++;
	}
}
