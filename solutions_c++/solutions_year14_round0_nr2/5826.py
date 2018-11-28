#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <iomanip>

using namespace std;

int main() {
    ifstream fin("/Users/byung-hoon/Desktop/Programs/Programs/in.txt");
    ofstream fout("/Users/byung-hoon/Desktop/Programs/Programs/out.txt");
    
    int numCases;
    fin >> numCases;
    
    for (int i = 0; i < numCases; i++) {
        double C, F, X;
        fin >> C >> F >> X;
        
        double time = 0;
        double rate = 2;
        
        double finish = X/rate;
        double nextFactory = (C/rate) + (X/(rate+F));
        
        while (finish > nextFactory) {
            time += (C/rate);
            //cout << "Bought Factory, added time " << setprecision(15) << (C/rate) << endl;
            rate += F;
            
            finish = X/rate;
            nextFactory = (C/rate) + (X/(rate+F));
        }
        time += (X/rate);
        //cout << "Finished, added time " << setprecision(15) << (X/rate) << endl;
        
        fout << "Case #" << i+1 << ": " << setprecision(15) << time << endl;
        //<< endl << endl << endl  << endl  << endl  << endl  << endl;
    }
    cin >> numCases;
    
	return 0;
}