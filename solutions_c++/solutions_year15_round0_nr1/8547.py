#include <iostream>
#include <fstream>
using namespace std;
#define LUNG 1002

int main(){
	ifstream f("ovation.in");
	ofstream g("ovation.out");
	int sets;
	f >> sets;
	int smax;
	char buff[LUNG];
	for(int set = 1; set <= sets; set++){
		f >> smax;
		f >> buff;
		int nec = smax;
		for (int i = smax-1; i >= 0; i--){
			if (buff[i] - '0'){
				 int curent = i + buff[i]-'0';
				 if (curent >= nec)
					 nec = i;
				 else
					 nec -= (buff[i]-'0');
			}
		}
		g << "Case #" << set << ": " << nec << endl;
	}
	f.close();
	g.close();
	return 0;
}