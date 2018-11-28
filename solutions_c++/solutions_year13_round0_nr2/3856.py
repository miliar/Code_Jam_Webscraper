#include <iostream>
#include <fstream>

using namespace std;

ifstream in("in.in");
ofstream out("out");

void output(int number_case, int clue){
	
	out << "Case #" << number_case+1 << ": "; 
	switch(clue){
		case true:
			out << "YES";
			break;
		case false:
			out << "NO";
			break;
	}
	out << endl;
}

int main(){
	int stevec;
	in >> stevec;
	
	for(int a(0);a<stevec;a++){
		bool unici=false;
		int x, y;
		in >> x >> y;
		
		int tabelca[x][y];
		int najvisji_x[1000]={0};
		int najvisji_y[1000]={0};
		
		//save array
		for(int b(0);b<x;b++){
			for(int c(0);c<y;c++){
				in >> tabelca[b][c];
				//pregledamo najnizjo stevilko v vrsticah
				if(najvisji_x[b] < tabelca[b][c]){
					najvisji_x[b]=tabelca[b][c];
				}
			}
		}
		
		if(x==1 or y==1){
			output(a, 1);
			continue;
		}

		for(int b(0);b<y;b++){
			for(int c(0);c<x;c++){
				//pregledamo najnizjo stevilko v stolpcih
				if(najvisji_y[b] < tabelca[c][b]){
					najvisji_y[b]=tabelca[c][b];
				}
			}
		}
		for(int b(0);b<x and unici==false;b++){
			for(int c(0);c<y and unici==false;c++){
				//vrstica, vse morajo biti visje, ce ni, morajo biti visje v stolpcu, drugace ni mozno
				if(tabelca[b][c]<najvisji_x[b] and tabelca[b][c]<najvisji_y[c]){
					unici=1;
					output(a, 0);
				}
				
			}
		}
		if(unici==false)output(a, 1);
	}
	return 0;
}
