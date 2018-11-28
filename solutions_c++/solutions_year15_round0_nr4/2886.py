#include <iostream>// q=-1 m=-k n=-j
#include<fstream>
using namespace std;
int main()
{
    int X,R,r,C,caz,o,T,i,smax,s,ss,p,j;
    char c[2000];
    ifstream in("in");
    ofstream out("out");
    in>>T;
    for(caz=1; caz<=T; caz++)
    {
        out<<"Case #"<<caz<<": ";
        r=0;
        in>>X>>R>>C;
        if (X>R&&X>C)
        {
            r=1;
            out<<"RICHARD";
        }
        if (X%2==1)
        {
            if ((X+1)/2>R||(X+1)/2>C)
            {
                if (r==0)
                {
                    out<<"RICHARD";
                    r=1;
                }
            }
        }
        if (X%2==0)
        {
            if (X/2>R||X/2>C)
            {
                if (r==0)
                {
                    out<<"RICHARD";
                    r=1;
                }
            }
        }
        if ((R*C)%X==0&&r==0)
		{
			if (X==4&&C==2)
			{
				out<<"RICHARD";
				r=1;
			}
			if (X==4&&R==2&&r==0)
			{
				out<<"RICHARD";
				r=1;
			}
			if (r==0)
			out<<"GABRIEL";
		}
        else
        {
            if (r==0) out<<"RICHARD";
        }
        out<<endl;
    }
}
