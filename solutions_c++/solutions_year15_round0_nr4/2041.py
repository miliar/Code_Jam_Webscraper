#include <iostream>
#include <fstream>

using namespace std;

int main()
{
   fstream in("D-small-attempt4.in");
ofstream out("D-small-attempt4.out");

int T;
int X, R, C;
in >> T;

for(int i = 1; i<= T; i++)
{
out<<"Case #"<<i<<": ";
in >> X >> R >> C;
if(X==1)
out<<"GABRIEL"<<endl;
else if(X==2)
{
	if((R*C) % 2 ==0)
	out<<"GABRIEL"<<endl;
	else
	out<<"RICHARD"<<endl;	
}
else if(X==3)
{
	if(((R*C) == 6) || (R*C == 12)|| (R*C == 9))
	{
		out<<"GABRIEL"<<endl;
	}
	else
	out<<"RICHARD"<<endl;
}
else
{
		if(((R*C) == 16) || (R*C == 12))
	out<<"GABRIEL"<<endl;	
    else
    out<<"RICHARD"<<endl;
    
}
}
 return 0;   
}

