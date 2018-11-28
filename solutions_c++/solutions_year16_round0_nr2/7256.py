#include <iostream>
#include <algorithm>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int main(int argc, char* argv[])
{
    int T =0;
    string N;
    ifstream inF(argv[1]);

    inF >> T;
    
    for(int i = 0; i < T; i++)
    {
        inF>> N;
        int count = 0;
        bool foundPlus = false;
        char last = N[0] ;

        for(int j = 0; j < N.size(); j++)
        {

            if('-' == N[j] && (N.size() > j+1 &&'+' == N[j+1]) && false == foundPlus)
            {
                count++;
            }

            if('+' == N[j-1] && '-' == N[j] )
            {
                count+=2;
            }

            if('+' == N[j])
            {
                foundPlus = true;
            }

        }

        if(false == foundPlus)
        {
            count++;
        }
        cout << "Case #" << i+1 <<": " << count << endl;
    }
   return 0;
}

