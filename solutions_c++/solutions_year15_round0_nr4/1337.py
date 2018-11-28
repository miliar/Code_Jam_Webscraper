#include<cstdio>
#include<iostream>
#include<algorithm>
#include<fstream>
#include<cstdlib>
using namespace std;

int main()
{
    ifstream input;
    input.open("D-small-attempt0.in");
    ofstream output;
    output.open("out.txt");
    char w;
	int tc,X,R,C;
	input>>tc;
	for(int testcase=1;testcase<=tc;testcase++)
	{
	    input>>X>>R>>C;
	    switch(X)
	    {
	        case 1:
	                w='G';
	                break;
	        case 2:
	                if(R==1&&C==1||R==1&&C==3||R==3&&C==1||R==3&&C==3)
	                    w='R';
	                else
	                    w='G';break;
	        case 3:
	                if(R==1||C==1)
	                    w='R';
	                else if(R==3||C==3)
	                    w='G';
	                else
	                    w='R';break;
	        case 4:
	                if(R==4&&C==4||R==4&&C==3||R==3&&C==4)
	                    w='G';
	                else
	                    w='R';
	    }
	    if(w=='G')
	        output<<"Case #"<<testcase<<": "<<"GABRIEL"<<endl;
	    else
	        output<<"Case #"<<testcase<<": "<<"RICHARD"<<endl;
	}
	return 0;
}
