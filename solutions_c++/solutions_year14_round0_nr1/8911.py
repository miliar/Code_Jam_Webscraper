#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;


void main (void){
	
	int T,m,c,u;
	int carta, coincidencias;
	int row1,row2;	//chosen
	int fila1[4];
	int fila2[4];
	string temp;

	getline(std::cin,temp);
	istringstream(temp) >> T;

	for (int t =0; t < T ; t++){
		//cerr << t;

		getline(std::cin,temp);
		istringstream(temp) >> row1;


		for (m=1;m<=4;m++){
			getline(std::cin,temp);

			if (m==row1){
				istringstream (temp) >> fila1[0] >> fila1[1]>> fila1[2]>> fila1[3];
			}
		}

		getline(std::cin,temp);
		istringstream(temp) >> row2;


		for (m=1;m<=4;m++){
			getline(std::cin,temp);

			if (m==row2){
				istringstream (temp) >> fila2[0] >> fila2[1]>> fila2[2]>> fila2[3];
			}
		}
		
		coincidencias=0;
		carta=0;
		//busco coincidencias
		for (u=0;u<4;u++){
			for(c=0;c<4;c++){
				if (fila1[u]==fila2[c]){
					coincidencias++;
					carta=fila1[u];
				}
			}
		}

		if (coincidencias==0){
			cout << "Case #" << t+1 << ": " << "Volunteer cheated!"<< endl  ;	
		}else if (coincidencias == 1){
			cout << "Case #" << t+1 << ": " << carta << endl  ;	
		}else{
			cout << "Case #" << t+1 << ": " << "Bad Magician!" << endl  ;	
		
		}
	}

}