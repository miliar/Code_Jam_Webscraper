#include <iostream>
#include <fstream>
#include <string>

using namespace std;



void main () {
	string x;

 string line;
  ifstream myreadfile ("A-small-attempt5.in");
  ofstream myfile;
  myfile.open ("answer.txt");
  if (myreadfile.is_open()	)
  {
	 getline(myreadfile,line);
    int a=stoi(line);
	int row,lineas=0,ii,jj;
	int posibles1[4];
	int posibles2[4];
	int posibles3[4];
	
	
	

	int x;
	string cifra,answer;
	char espacio=' ';
	
	cout<<a;
	  for(int i=0;i<a;i++) ///numero de casos
	  {
		  
		  for(int dos=0;dos<2;dos++) ///revolver
		  {
			  cifra="";
				x=0;
		  getline(myreadfile,line); ///leer lineas
		  row=stoi(line);
		  for(lineas=0;lineas<row;lineas++)
			  getline(myreadfile,line); ///linea correcta

		  for(int cont=0;cont<line.length();cont++) ///vector de opciones
		  {
			
			if(line[cont]!=espacio)
			cifra=cifra+line[cont];
			else
			{
				if(dos==0)
				posibles1[x++]=stoi(cifra+"");
				else
				posibles2[x++]=stoi(cifra+"");
				cifra="";
			  }	
			
		  }
		
				if(dos==0)
				posibles1[x++]=stoi(cifra+"");
				else
				posibles2[x++]=stoi(cifra+"");
				cifra="";

		  for(lineas;lineas<4;lineas++)
			  getline(myreadfile,line);
		  }
		////comparar vectores
		  x=0;
		  for(ii=0;ii<4;ii++)
		  {
			  for(jj=0;jj<4;jj++)
			  {
				if(posibles1[ii]==posibles2[jj])
					posibles3[x++]=posibles1[ii];
			  }
		  }

		  answer="Case #"+to_string(i+1)+": ";
		  if(x==1)
		  {
			  
			  answer=answer+to_string(posibles3[0])+"\n";
		  }
		  if(x>1)
		  {
			  answer=answer+"Bad magician!\n";
		  }
		  if(x==0)
			answer=answer+"Volunteer cheated!\n";

			  
		  myfile<<answer;
		  answer="Ninguno\n";
	
	  }
    
  }

  else cout << "Unable to open file"; 

 
	
	
	

  
  //myfile << x;
  myfile.close();
  myreadfile.close();

  
 System::Console::ReadKey();

}
