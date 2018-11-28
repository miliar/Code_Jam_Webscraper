#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int isNumberPalindrome(int num){
    // reverse the number
    int origNum = num;
    int revNum = 0;
    
    while (num>0) {
        int digit = num%10;
        revNum = revNum*10 + digit;
        num = num/10;
    }
    
    // check if orig number and the reversed num are equal
    if (origNum == revNum) {
        return 1;
    }
    
    return 0;
}

int isNumberFairAndSquare(int num){
    if(isNumberPalindrome(num)==0){
        return 0;
    }

    double root = sqrt(num);

    double fractPart, intPart;
    fractPart = modf(root, &intPart);

    if (fractPart != 0) {
        return 0;
    }

    if (isNumberPalindrome(root)==0) {
        return 0;
    }
    
    return 1;
}

int main () {
    string line;
    ifstream infile ("data.txt");
    ofstream outfile;
    outfile.open ("output.txt");

    if (infile.is_open() && outfile.is_open())
    {
            // get number of cases - between 1 and 100
            int cases;
            getline (infile,line);
            cases = atoi(line.c_str());
            
            // for each case
            for (int i=1; i<=cases; i++) {                
                // limits between 1 and 1000
                string minlimit, maxlimit;
                getline (infile, minlimit, ' ');
                getline (infile, maxlimit);
                
                int min = atoi(minlimit.c_str());
                int max = atoi(maxlimit.c_str());

                int count = 0;
                
                for (int j=min; j<=max; j++) {
                    if (isNumberFairAndSquare(j) == 1) {
                        count += 1;
                    }
                }
                
                // write output
                outfile << "Case #" << i << ": " << count << "\n";
            }
        
        outfile.close();
        infile.close();
    }
    
    else cout << "Unable to open file";
    
    return 0;
}