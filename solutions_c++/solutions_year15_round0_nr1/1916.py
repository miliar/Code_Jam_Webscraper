#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	string line;
  	ifstream infile ("example.txt");
  	ofstream outfile ("output.txt");
  	if ((infile.is_open())&&(outfile.is_open()))
  	{
   		int T;
   		int casecurrent=1;
   		infile>>T;
    	while ( casecurrent<=T )
    	{
    		int smax;
      		infile>>smax;
      		getline(infile,line);
      		int total=0;
      		int invites=0;
      		for(int i=1;i<=smax+1;i++)
      		{
      			int si=line[i]-48;
      			if((total+invites)<(i-1))
      				invites+=(i-1)-(total+invites);
      			total+=si;
      		}
      		outfile<<"Case #"<<casecurrent++<<": "<<invites<<endl;
    	}
    	infile.close();
    	outfile.close();
  	}
	else cout << "Unable to open file"; 
}