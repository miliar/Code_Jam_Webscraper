#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;
int main(int argc, const char * argv[])
{

    ifstream input("C:/Users/Utente/Documents/Workspace/C/Fractiles/bin/Debug/input.in");
    ofstream output("C:/Users/Utente/Documents/Workspace/C/Fractiles/bin/Debug/output.txt");


    int cases;
    input >> cases;
    for(int i = 1; i<= cases ; i++)
    {
        int k,c,s;
        input >> k;
        input >> c;
        input >> s;
        output << "Case #" << i <<": " ;

        if(c ==1 || k == 1)
        {
            output << "1 ";
        }
        for(int j = 2; j <=k; j++)
        {
            output << j <<" ";
        }
        output << endl;
    }
    return 0;
}
