// writing on a text file
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
using namespace std;

int programa(string numero)
{
	int s,i,flip,k;
	char *c = new char[numero.size()+1];
	strcpy(c,numero.c_str());
	int viradas = 0;
	s = numero.size();

	while(true){
		int virar = 0;
		bool controle = true;
		i = 0;
		if(c[0]=='-')
		while(c[i]!='\0' && c[i]!='+'){

		virar++;

		i++;
		}

		 
		  if(c[0]=='+' || virar==0){
			  bool n = false;
			 
			  for(k=0;k<s;k++)
			  {
				
				if(c[k]=='-')
				  n = true;

				if(c[k]=='+' && n == true)
				  break;
				
				virar++;

				
 
			  }

			if(n==false)
			 controle = false;
		  }

		if(virar>0 && controle == true){
		  for(k=0;k<virar;k++)
		  {
			if(c[k]=='-')
				c[k] = '+';
			else
				c[k] = '-';

		  }
		  viradas++;
		}else{
		  return viradas;
		}
	}

	return viradas;
}

int main (int argc, char ** argv) {
  string line;
  ifstream myfile ("B-large.in");
  freopen("arq","w",stdout);
  long counter = 1;
  if (myfile.is_open())
  {
	getline(myfile,line);
    while ( getline (myfile,line) )
    {
      cout << "Case #" << counter << ": "  << programa(line) << endl;

      counter++;
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}
