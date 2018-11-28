#include<iostream>
#include<math.h>
using namespace std;

void printname(string s,int i)
{
	cout<<"Case #"<<i+1<<": "<<s<<endl;
}

int main()
{
	int cases,i=0;
	string s;
	cin>>cases;
	
	while(i<cases)
	{
		int x,row,column,sqroot;
		
		cin>>x>>row>>column;
		sqroot=sqrt(x);
		if(x>2)
		{
			if((row*column)%x==0 && ((row*column)/x) >= sqroot+1)
            {
            	s="GABRIEL";
            	printname(s,i);
            }
				
            
			else
		  	{
            	s="RICHARD";
            	printname(s,i);
            }
		}
		
		else if(x<=2)
		{
            if((row*column)%x==0)
            {
            	s="GABRIEL";
            	printname(s,i);
            }
            
			else
  			{
            	s="RICHARD";
            	printname(s,i);
            }
		}

        i++;
	}
	return 0;
}

