#include <iostream>
#include <fstream>

using namespace std;



int main()
{
    ifstream input;
    input.open("input.txt");
    ofstream output;
    output.open("output.txt");
    int T;
    input >> T;
    for (int i = 0; i < T; i++){
        int ammount = 0;
        int n1, n2, n3;
        input >> n1 >> n2 >> n3;
        for (int a = 0; a < n1; a++){
            for (int b = 0; b < n2; b++){
                int c = a & b;
                if ((a & b) < n3){
                ammount++;
                }
            }
        }
        output << "Case #" << i+1 << ": " << ammount << endl;
    }
    return 0;
}
