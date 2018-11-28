#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main(){
	ifstream reader;
	ofstream writer;
	
	reader.open("input.txt");
	writer.open("output.txt");

	int cases;

	reader >> cases;
	writer << fixed;
	
	for(int c = 0; c < cases; c ++)
	{
		if (cases%10) cout << "On case #" << c+1 << endl;
		double C,F,X, rate = 2.0, time = 0.0;
		
		reader >> C >> F >> X;
	
		while(true){
			double proj1, proj2;
			proj1 = (X)/rate;
			proj2 = C/rate + X/(rate + F);

			if(proj1 < proj2){
				writer << "Case #" << c+1 << ": " << setprecision(7) << time + proj1 << endl;
				break;
			}else{
				time += C/rate;
				rate += F;
			}
		}
	}
}
