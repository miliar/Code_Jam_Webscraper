#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

bool ispalindrome(unsigned long num);

int main()
{
    ifstream file("C-small-attempt0.in");
    ofstream output;
    output.open("output.txt", ios::trunc);

    string iline;

    int cases;
    getline(file,iline);
    stringstream(iline) >> cases;

    for(int x = 1; x <= cases; x++){
        string sourceline;
        getline(file,sourceline);

        unsigned long interval[2];
        for(int k = 0; k <= 1; k++){interval[k] = 0;}

        int currentnum = 1;
        int multiply = 1;

        for(int i = sourceline.length() - 1; i >= 0; i--){
            if(sourceline[i] == ' '){
                multiply = 1;
                currentnum--;
            }
            else{
                interval[currentnum] += (((int) sourceline[i] - 48) * multiply);
                multiply *= 10;
            }
        }

        int fairandsquare = 0;

        for(unsigned long e = interval[0]; e <= interval[1]; e++){
            if(ispalindrome(e) == true){
                unsigned long result = sqrt(e);
                if(result * result == e && ispalindrome(result) == true){
                    fairandsquare++;
                }
            }
        }

        output << "Case #" << x << ": " << fairandsquare << '\n';

    }

    file.close();
    output.close();
    return 0;
}

bool ispalindrome(unsigned long num)
{
    stringstream s;
    s << num;
    string snum = s.str();

    int middle = snum.length() / 2;

    bool pal = true;
    for(int l = 0, r = snum.length() - 1; l < middle; l++, r--){
        if(snum[l] != snum[r]){pal = false;}
    }

    return(pal);
}
