#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main(){
    ifstream input("D-small-attempt0.in");
    ofstream output("smallD.txt");
    int t;
    input >> t;
    for(int x=0;x<t;x++){
        int k, c, s;
        input >> k >> c >> s;

        cout << "Case #" << x+1 << ": ";
        output << "Case #" << x+1 << ": ";
        for(int i=0;i<k;i++){
            cout << fixed << 1 + i * (unsigned long long int)pow(k, c-1) << " ";
            output << fixed << 1 + i * (unsigned long long int)pow(k, c-1) << " ";
        }
        cout << endl;
        output << endl;
    }
	input.close();
	output.close();
	return 0;
}
