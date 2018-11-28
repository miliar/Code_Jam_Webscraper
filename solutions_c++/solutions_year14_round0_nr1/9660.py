#include <iostream>
#include<fstream>
#include<string.h>
#include<sstream>
#include <stdio.h> 
#include <stdlib.h> 

using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	
	 ofstream cout("burro.txt"); 
	 
	
	 
	int casos;
	cin>>casos;
	
	cin.ignore();
	
	int cuento=1;
while(cuento<=casos){
	
	
	int caso1;
 cin>>caso1;
	cin.ignore();
	
	


 
 int matriz[16];

 int contador=0;
 for(int i=0;i<4;i++){
 
 	 string s;
	getline(cin,s);

	stringstream ss; 
    string var; 
    ss<<s;
 while(ss>>var){
 
 matriz[contador]=atoi(var.c_str());
 
 contador++;
  
}
}

	int caso2;
 cin>>caso2;
	cin.ignore();
	int matriz2[16];
	
 for(int i=0;i<4;i++){
 
 	 string s;
	getline(cin,s);

	stringstream ss; 
    string var; 
    ss<<s;
 while(ss>>var){
 
 matriz[contador]=atoi(var.c_str());
 
 contador++;
  
}
}
// meto la primera matriz

// nuemro que esté en el 1 y en el 2
bool encuentro=false;
int encuentros=0;

for(int i=((caso1-1)*4);i<(((caso1-1)*4)+4);i++){
	for(int j=((caso2-1)*4);j<(((caso2-1)*4)+4);j++){
	  if(matriz[i]==matriz2[j]){
encuentros++;

	  }
	  
	}
}
cout<<"Case #"<<cuento<<": ";
if(encuentros==0){
	cout<<"Volunteer cheated!"<<endl;
	
}else if(encuentros>1){
		cout<<"Bad magician!"<<endl;
}else{
	
for(int i=((caso1-1)*4);i<(((caso1-1)*4)+4);i++){
	for(int j=((caso2-1)*4);j<(((caso2-1)*4)+4);j++){
	  if(matriz[i]==matriz2[j]){
cout<<matriz[i]<<endl;
	  }
	  
	}
}	
}
cuento++;
}

 cout.close(); 
	
	
	return 0;
}
