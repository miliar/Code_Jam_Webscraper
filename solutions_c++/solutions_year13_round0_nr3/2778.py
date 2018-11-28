#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#include <math.h>
#include <iomanip>
#include <fstream>
using namespace std;

bool palindrome(string s){
    for(int i = 0; i < s.length(); i++){
        if(s[i] != s[s.length()-1-i])
            return false;
    }
    return true;
}

string convertInt(long long int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

int main() {
    ifstream read;
    read.open("C-small-attempt0.in");
    ofstream write;
    write.open("answer.txt");
    int caseNo;
    read >> caseNo;
    for(int i = 1; i <= caseNo; i++){
        int min, max;
        read >> min >> max;
        int count = 0;
        for(int j = min; j <= max; j++){
            if(!palindrome(convertInt(j)))continue;
            int x = sqrt(j);
            if(x * x != j)continue;
            if(palindrome(convertInt(x)))count++;
        }
        write << "Case #" << i << ": " << count << endl;
    }
    return 0;
}
