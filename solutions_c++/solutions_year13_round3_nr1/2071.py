

#include <stdio.h>
#include <math.h>
#include "vector"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <stdlib.h>
#include <time.h>
using namespace std;
#define nAtt 4//3//4/*///7//6//5*/
#define nLinha 83
#define nColuna 5//4// 5/*5/*///9//8//7
#define nStates 36864//2304//36864///589824//4782969//5314citiesRecog//c//3^2*nAtt
#define posAns 3//possible answers
#define recall 2//possible recall values
#define indexCost  33
#define numberCases 500


int myPow(int x, int p) {
  if (p == 0) return 1;
  if (p == 1) return x;
  return x * myPow(x, p-1);
}



int main (/*int argc, char **argv*/ )//muda linux
{

		//LEITURA DADOS
	int ncasos;
	vector <int> output;
				ifstream myfile;
				myfile.open("A-small-attempt0.in");
				  int linha=0;
				  string line;
				  if (myfile.is_open())
				  {
					getline(myfile,line);
					std::istringstream iss(line);
					iss >> ncasos;
					
					output.resize(ncasos);
				    int caso=0;
					while ( myfile.good() )
					{
					  getline(myfile,line);
					  int valueRecall;
					  std::istringstream iss(line);
					  string name;
					  int n;
					   iss >> name;
					   iss>>n;
					   vector <int> palavra;
					   palavra.resize(name.size());
					   for (int i=0; i<name.size();i++){
						   if (name[i]=='a' || name[i]=='e' ||name[i]=='i' ||name[i]=='o' ||name[i]=='u')
							   palavra[i]=0;
						   else
							   palavra[i]=1;
					   }
					   for (int i=name.size()-1;i>n-2;i=i-1){
						   int notFinished=1;
						   int soma=0;
						   int pos=0;
						   while (notFinished==1){
							   if (palavra[i-pos]==1)
									soma=soma+palavra[i-pos];
							   else
								   soma=0;
							   if (soma==n || pos==i){
								   notFinished=0;
								   if (soma==n)
									   pos=pos;
								   else
									   pos=i+1;
							   }
							   else
								   pos++;
						   }
						   output[caso]=output[caso]+(i+1-pos);
					   }

					   caso=caso+1;

					}
					myfile.close();
				  }
				  //http://www.cplusplus.com/forum/general/72375/
				  else cout << "Unable to open file\n"; 
				

	
		ofstream  OUT;
		//OUT.open(filename.c_str(), ios::out | ios::binary);
		OUT.open("outputJam.txt");
		for(int j=0;j<ncasos;j++){
				OUT<<"Case #"<<j+1<<": "<<output[j]<<"\n";
		}
		OUT.close();


}//int main