#include <iostream>
#include <fstream>
using namespace std;

bool consonant(char letter){
	switch (letter){
		case 'a': return false; break;
		case 'e': return false; break;
		case 'i': return false; break;
		case 'o': return false; break;
		case 'u': return false; break;
		default: return true;
    }
}


int main(){
	ifstream fin;
	ofstream fout;
	fin.open("fin.txt");
	fout.open("fout.txt");
	int cases;
	fin >> cases;
	for(int a=0;a<cases;a++){
		int nvalue=0,n;
		string name;
		fin >> name >> n;
		for(int x=0;x<=name.length()-n;x++){
			for(int y=x+n-1;y<name.length();y++){
				int consonants=0;
				for(int o=x;(o<=y);o++){
					if(consonant(name[o])==true) consonants++;
					else if(consonant(name[o])==false) consonants=0;
					if(consonants==n) break;
				}
				if(consonants>=n) nvalue++;
			}
		}
		fout << "Case #" << a+1 << ": " << nvalue << "\n";
	}
	return 0;
}
