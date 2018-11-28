#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){

    ifstream myFile("input.txt");
    ofstream output("output.txt");
    int t,smax;
    string au;

    int total = 0;
    int result = 0;
    if(myFile.is_open())
    {
        myFile >> t;

        for(int i = 0; i < t ; i++){
            myFile >> smax >> au;
            total = 0;
            result = 0;
            for(int i = 1; i < smax + 1 ; i++){
                for(int j = 0; j < i ; j++){
                    total += (int)au.at(j) - '0';
                }

                while(total + result < i)
                    result++;
                total = 0;
            }

        output << "Case #" << i+1 << ": " << result << "\n";
        }



    }
}
