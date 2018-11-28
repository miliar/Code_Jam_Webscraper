#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

int main()
{
    ifstream in("prob a.in");
    ofstream out("prob a.out");

    int T;
    in >> T;

    for(int t = 0; t < T; ++t) {
        int first, second, throwaway;
        in >> first;
        
        int row[4];
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                if (i + 1 != first)
                    in >> throwaway;
                else
                    in >> row[j];
            }
        }
        
        in >> second;
        int count = 0;
        int value;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                if (i + 1 != second)
                    in >> throwaway;
                else {
                    int tmp;
                    in >> tmp;
                    for(int k =0; k < 4; ++k) {
                        
                        if(row[k] == tmp) {
                            count++;
                            value = tmp;
                        }
                    }
                }
            }
        }
        
        out << "Case #" << t+1 << ": ";
        if(count == 0)
            out << "Volunteer cheated!" << endl;
        if(count == 1)
            out << value << endl;
        if(count > 1)
            out << "Bad magician!" << endl;
    }

    out.close();
}
