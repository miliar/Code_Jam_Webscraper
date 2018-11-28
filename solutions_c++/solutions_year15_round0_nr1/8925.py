#include<iostream>
#include<cstdlib>
#include<fstream>
#include<cstring>
using namespace std;
main()
{
      ifstream myfile("A-large.in");
      ofstream myfileo;
      myfileo.open("outflarge.in");
      int T,a;
      string str;
	  myfile>>T;
	  
	  for(int i=0;i<T;i++)
	  {
	  	myfileo<<"Case #"<<i+1<<": ";
	  	myfile>>a;
	  	myfile>>str;
	  	int con = str[0]-48;
	  	int count = 0;
		  int j;
		  for( j=0;j<a+1;j++)
	  	{
		  if(	j>con)
	  		{
			  count+= (j-con);
	  		con+=j-con;
	  	}
			  if(j>0) con+=(str[j]-48);
		}
		myfileo<<count<<endl;
	  }
}
