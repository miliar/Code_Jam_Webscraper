#include <iostream>
#include <string>
#include <set>
#include <fstream>
#include <sstream>
#include <cmath>
using namespace std;

bool isSameO(string line){
	return (line=="OOOO" || line=="TOOO" || line=="OTOO" || line == "OOTO" || line == "OOOT");

}
bool isSameX(string line){
	return (line=="XXXX" || line=="TXXX" || line=="XTXX" || line == "XXTX" || line == "XXXT");
}

int haveWin(string line1,string line2,string line3,string line4){
	string line5,line6,line7,line8,line9,line10;
	line5.push_back(line1.at(0));
	line5.push_back(line2.at(0));
	line5.push_back(line3.at(0));
	line5.push_back(line4.at(0));

	line6.push_back(line1.at(1));
	line6.push_back(line2.at(1));
	line6.push_back(line3.at(1));
	line6.push_back(line4.at(1));

	line7.push_back(line1.at(2));
	line7.push_back(line2.at(2));
	line7.push_back(line3.at(2));
	line7.push_back(line4.at(2));

	line8.push_back(line1.at(3));
	line8.push_back(line2.at(3));
	line8.push_back(line3.at(3));
	line8.push_back(line4.at(3));

	line9.push_back(line1.at(0));
	line9.push_back(line2.at(1));
	line9.push_back(line3.at(2));
	line9.push_back(line4.at(3));

	line10.push_back(line1.at(3));
	line10.push_back(line2.at(2));
	line10.push_back(line3.at(1));
	line10.push_back(line4.at(0));

	if (isSameO(line1)||isSameO(line2)||isSameO(line3)||isSameO(line4)||isSameO(line5)||isSameO(line6)||isSameO(line7)||isSameO(line8)||isSameO(line9)||isSameO(line10))
		return 1;
	else if (isSameX(line1)||isSameX(line2)||isSameX(line3)||isSameX(line4)||isSameX(line5)||isSameX(line6)||isSameX(line7)||isSameX(line8)||isSameX(line9)||isSameX(line10))
		return 2;
	else 
		return 0;
}
bool haveDraw(string line1,string line2,string line3,string line4){
	if(line1.at(0) == '.' || line1.at(1)=='.' || line1.at(2)=='.' || line1.at(3)=='.')
		return false;
	if(line2.at(0) == '.' || line2.at(1)=='.' || line2.at(2)=='.' || line2.at(3)=='.')
		return false;
	if(line3.at(0) == '.' || line3.at(1)=='.' || line3.at(2)=='.' || line3.at(3)=='.')
		return false;
	if(line4.at(0) == '.' || line4.at(1)=='.' || line4.at(2)=='.' || line4.at(3)=='.')
		return false;
	return true;
}
int main(){

	int nbGame;
	int c;
	string line1,line2,line3,line4;
	ifstream fichier("A-large.in", ios::in);  
	ofstream f("output2.txt", ios::out | ios::trunc);
			
        if(fichier) 
			
        {if(f){
		
			
			fichier >>nbGame;
		
			c=nbGame;
			while (nbGame!=0){
				--nbGame;
				
				fichier>>line1>>line2>>line3>>line4;
		
				int win=haveWin(line1,line2,line3,line4);
				if (win==1)
					f<<"Case #"<<c-nbGame<<": "<<"O won"<<endl;
				else if (win==2)
					f<<"Case #"<<c-nbGame<<": "<<"X won"<<endl;
				else if(haveDraw(line1,line2,line3,line4))
						f<<"Case #"<<c-nbGame<<": "<<"Draw"<<endl;
				else
					f<<"Case #"<<c-nbGame<<": "<<"Game has not completed"<<endl;
			
			}

		
				
		}
		else
                cerr << "Impossible d'ouvrir le fichier !" << endl;}

        fichier.close();  
		f.close();

	system("pause");
	return 0;
}