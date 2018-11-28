#include<iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
ifstream fin("ind3.in");
ofstream fout("ot.out");
	int tc,t,X,R,C;
	char win;
	fin>>tc;
	for(t=1;t<=tc;t++)
	{
	    fin>>X>>R>>C;
	    switch(X)
	    {
	        case 1:
	                win='g';break;
	        case 2:
	                if(R==1&&C==1||R==1&&C==3||R==3&&C==1||R==3&&C==3)
	                    win='r';
	                else
	                    win='g';break;
	        case 3:
	                if(R==1||C==1)
	                    win='r';
	                else if(R==3||C==3)
	                    win='g';
	                else
	                    win='r';break;
	        case 4:
	                if(R==4&&C==4||R==4&&C==3||R==3&&C==4)
	                    win='g';
	                else
	                    win='r';
	    }
	    if(win=='g')
	        fout<<"Case #"<<t<<": GABRIEL\n";
	    else
	        fout<<"Case #"<<t<<": RICHARD\n";
	}
	return 0;
}
