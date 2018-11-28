#include<iostream>
#include<fstream>

using namespace std;

ifstream inFile("D-small-attempt3.in",ios::in);
ofstream oFile("D-small-attempt3.out",ios::out);

int main()
{
    int t,x,r,c;

    inFile>>t;

    for(int i=1; i<=t; i++)
    {
        inFile>>x>>r>>c;

        oFile<<"Case #"<<i<<": ";

        if(x>r*c)
            oFile<<"RICHARD"<<endl;

        else if(x==1)
            oFile<<"GABRIEL"<<endl;

        else if(x==2)
        {
            if( r%x==0 || c%x==0 )
                oFile<<"GABRIEL"<<endl;
            else
                oFile<<"RICHARD"<<endl;
        }

        else if(x>=3)
        {
            if( (r==x || c==x) && (r>=x-1 && r>=x-2) && (c>=x-1 && c<=x+1) )
                oFile<<"GABRIEL"<<endl;
            else
                oFile<<"RICHARD"<<endl;
        }

    }

    return 0;
}
