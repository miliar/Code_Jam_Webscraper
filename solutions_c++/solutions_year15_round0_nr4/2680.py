#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <tuple>
#include <queue>
#include <map>
#include <algorithm>
#include <utility>

using namespace std;

int main()
{
	ifstream ifile;
	ofstream ofile;
	int test;
	ifile.open("D-small-attempt2.in");
	ofile.open("Output.txt");
	ifile>>test;
	for(int i=0;i<test;i++)
	{
        int x,r,c;
        ifile>>x>>r>>c;
        int val=r*c;
        int num=i+1;
        if((val%x)==0)
        {
            if(val>x || x==1)
            {
                if((( ((x%r)==0 && r<x) || ((x%c)==0 && c<x)) && x>2))
                    ofile<<"Case #"<<num<<": "<<"RICHARD"<<endl;
                else
                    ofile<<"Case #"<<num<<": "<<"GABRIEL"<<endl;
            }
            else if(val==x)
            {
                if(((r==1 || c==1) && x>2) )
                    ofile<<"Case #"<<num<<": "<<"RICHARD"<<endl;
                else if(x<=2)
                    ofile<<"Case #"<<num<<": "<<"GABRIEL"<<endl;
                else
                    ofile<<"Case #"<<num<<": "<<"RICHARD"<<endl;

            }
        }
        else
            ofile<<"Case #"<<num<<": "<<"RICHARD"<<endl;
	}
    ifile.close();
    ofile.close();
	return 0;
}
