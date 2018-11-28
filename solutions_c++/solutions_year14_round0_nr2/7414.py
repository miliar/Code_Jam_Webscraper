#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	int n;
	ifstream myfile;
	myfile.open ("jotain.in");
	myfile >> n;
	ofstream outf;
	outf.open ("ans.txt");
	outf.precision(12);
	int an = n;
	while(n--){
		double c, f, x; myfile >> c >> f >> x;
		
		
	
		if(x < c){
			outf << "Case #" << an-n << ": " << x / 2.000000000<< "\n";
			continue;
		}

		double cookies = 2;
		double cost = x / cookies;
		double ccost = 0;
		
		while(true){
			
			 
			ccost +=c / cookies;
			cookies +=f;
			double ncost =  ccost + x / cookies;
			

			if(ncost > cost){
				break;			
			}
			cost = ncost;
		
		
		}
		outf << "Case #" << an-n << ": " << cost<< "\n";

	
	}

	myfile.close();
	outf.close();
	return 0;
}

