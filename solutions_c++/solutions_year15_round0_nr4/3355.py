#include<iostream>
#include <fstream>
#include<string.h>
using namespace std;
int main()
{int testnum=0;
	ifstream in("D-small-attempt5.in");					//enter file name here
	ofstream out("d-small-5.out");            //output file
		in>>testnum;
 int x,r,c;
 int y;
 int counter=0;
 int a[10][10];
 for(int i=0;i<10;i++)
	 for(int j=0;j<10;j++)
	 {	a[i][j]=-1;	 
	 }

 while(counter<testnum)

	{	in>>x>>r>>c;
		if(x==1)
				out<<"Case #"<<counter+1<<": GABRIEL"<<endl;
			
		else if(x==2)
			{if((r*c)%x==0)
				out<<"Case #"<<counter+1<<": GABRIEL"<<endl;
			else
				out<<"Case #"<<counter+1<<": RICHARD"<<endl;
			
			}
 
		
		else if(x==4)
			{if((r==4&&c==3)||(r==3&&c==4)||(r==4&&c==4))
				out<<"Case #"<<counter+1<<": GABRIEL"<<endl;
			else
				out<<"Case #"<<counter+1<<": RICHARD"<<endl;
			}
		
		else if(x==3)
			{if((r==3&&c==3)||(r==4&&c==3)||(r==3&&c==4)||(r==3&&c==2)||(r==2&&c==3))
				out<<"Case #"<<counter+1<<": GABRIEL"<<endl;
			else
				out<<"Case #"<<counter+1<<": RICHARD"<<endl;
			}
		else
			 y=0;
		counter++;
	}

return 0;
}