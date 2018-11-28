#include<iostream>
using namespace std;
#include<stdio.h>
#include <fstream>

int main()
{
	int t,x,r,c, flag;
	char num;
	ifstream fin("D-small-attempt0.in");
	//ifstream fin("A-large.in");
	//ifstream fin("test.txt");
	//fin >> t;
	ofstream fout("output.txt");

	//fin.get(num);
	fin>>t;
	//t = ((int)num-'0');


	/*for(int r=1; r<=4; r++)
    {
        for(int c=r; c<=4;c++)
        {
            cout<<r<<" "<<c<<": ";
            for(int x=1; x<=4; x++)
            {
                flag =0;

                if((r*c)%x == 0)
                {
                    if(x>2)
                    {
                        if(r>=(x/2+1) && c>=(x/2+1))
                            flag=1;
                    }
                    else
                        flag=1;
                }

                if(flag)
                    cout<<x<<" ";

            }
            cout<<endl;
        }

    }*/


	for(int i=1; i<=t; i++)
    {
        fin>>x;
        fin>>r;
        fin>>c;

        flag =0;


        if((r*c)%x == 0)
        {
            if(x>2)
            {
                if(r>=(x/2+1) && c>=(x/2+1))
                    flag=1;
            }
            else
                flag=1;
        }

        if(flag)
            fout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
        else
            fout<<"Case #"<<i<<": "<<"RICHARD"<<endl;

    }
}
