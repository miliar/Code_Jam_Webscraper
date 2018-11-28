
#include <iostream>
#include <string>
#include <set>
#include <fstream>
#include <sstream>
#include <cmath>
using namespace std;
bool isPalyndrome(int a){
	string a_string= to_string(a);
	int i=a_string.length()-1;
	string palin="";
	while(i!=-1){
		palin+=a_string.at(i);
		i--;
	}
	return palin==a_string;
}
bool isSquare(int k){
  return floor(sqrt(k)) == sqrt(k) && isPalyndrome(sqrt(k));
}
bool test(int a){
	if (isSquare(a))
		if(isPalyndrome(a))
			return true;
		else 
			return false;
	else 
		return false;
}
int main(){
	
	int nbLine;
	int num1,num2;
	int c;
	ifstream fichier("C-small-attempt1.in", ios::in);  
	ofstream f("output2.txt", ios::out | ios::trunc);
			
        if(fichier) 
        { 
			fichier >>nbLine;
			c=nbLine;
			while (nbLine!=0){
				nbLine=nbLine-1;
				fichier>>num1>>num2;
				int compteur=0;
				for (int i=num1;i!=num2+1;++i){
					if(test(i))
					++compteur;
				}
			f<<"Case #"<<c-nbLine<<": "<<compteur<<endl; 
			}	
				
		}
		
        fichier.close();  
		f.close();

	system("pause");
	return 0;
}