// writing on a text file
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstring>
using namespace std;

string programa(string numero)
{
	ostringstream oss;
	char * c;
	c = new char[numero.size() + 1];
	std::copy(numero.begin(), numero.end(), c);
	c[numero.size()] = '\0'; // don't forget the terminating 0


	int num[10], k;
	for(k=0;k<10;++k)
		num[k] = 0;

	long tamanho, mult, i , original;

	original = atol(numero.c_str());
	long count = 2;
	tamanho  = numero.size();	
	bool sair = false;	
	bool insonia = false;
	int ultimo;

	while(!sair){
		bool tempF = true;
		for(i = 0;i<=tamanho;++i){
			int temp = (int)c[i] - '0';
			num[temp]++;		
		}

		for(k=0;k<10;++k)
		{
			
			if(num[k]==0)
			 tempF = false;
			
			if(num[k]>10000)
			 insonia = true;
		}

		if(tempF == true)
			return oss.str();

		if(tempF == true || insonia == true)
			sair = true;

		mult = original * count;
		count++;

		oss.clear();
		oss.str(string());
		oss << mult;
				
		free(c);
		c = new char[oss.str().size()+1];
		strcpy(c,oss.str().c_str());


	}

	delete[] c;

	if(insonia == true)
		return "INSOMNIA";
	else
		return string(c);

	
}

int main (int argc, char ** argv) {
  string line;
  ifstream myfile ("A-large.in");
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
