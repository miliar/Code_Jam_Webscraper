#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <math.h>

using namespace std;

bool isPalindrome(string number)
{
    int taille = number.length();
    bool veracite = true;
    for(int i=0; i<taille/2; i++){
//        cout << number << endl;
        if(number.at(i) != number.at(taille - i - 1))
            veracite = false;
        if(!veracite)
            return false;
    }

}

int main()
{
    ifstream file("donnees.txt");
    int T;
    ostringstream osA, osB, osJ, osJ2;
    file >> T;

    int A, B, nbPal = 0, sJ;
    string sA, sB;
    bool square;
    for(int i=0; i<T; i++){
        osA.str("");
        osB.str("");
        file >> A;
        file >> B;
        osA << A;
        osB << B;
        sA = osA.str();
        sB = osB.str();
//
//        cout << "Case #" << i+1 << ": A and B"<< A << " " << B << endl;
        for(int j=A; j<=B; j++){
            osJ << j;
            sJ = sqrtf(j);
            if(sJ != sqrtf(j))
                square = false;
            else
                square = true;
            if(square)
                osJ2 << sJ;
            if(isPalindrome(osJ.str()) && square && isPalindrome(osJ2.str())){
                nbPal++;
//                cout << "Case #" << i+1 << ": " << sJ << endl;
            }
            osJ.str("");
            osJ2.str("");
        }
        cout << "Case #" << i+1 << ": "<<nbPal << endl;
        nbPal = 0;
    }



    return 0;
}


