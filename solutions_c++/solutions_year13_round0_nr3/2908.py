#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <math.h>

using namespace std;
typedef int integer;

int parseInt(string s){
    int n;
    istringstream(s) >> n;
    return n;
}

vector<string> &split(const string &s, char delim, vector<string> &elems) {
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}


vector<string> split(const string &s, char delim) {
    vector<string> elems;
    split(s, delim, elems);
    return elems;
}

int numLength(integer num){
    int numLength = 0;
    while(num != 0){
        numLength ++;
        num /= 10;
    }
    return numLength;
}

inline int getNthDigit(integer num, int n){
    for(int i = 1; i < n; i++){
        num /= 10;
    }
    return num % 10;
}

bool isPalindrome(integer num){
    int nl = numLength(num);
    for(int i = 0; i < nl/2; i++){
        if(getNthDigit(num, i) != getNthDigit(num, nl-i)){
            return false;
        }
    }
    return true;
}

bool isSquare(integer num, integer& result){
    float dnum = (float) num;
    float srt = sqrt(dnum);

    if(srt == (float)(int)srt){
        // It is a perfect sqrt
        result = (integer) srt;
        return true;
    }
    return false;
}

int numFairSquare(integer min, integer max)
{
    integer numFS = 0;
    integer result;
    for(integer i = min; i <= max; i++){
        result = 0;
        if(isPalindrome(i) && isSquare(i, result) && isPalindrome(result)){
            numFS++;
        }
    }
    return numFS;
}

void printResult(int t, int result)
{
    printf("Case #%d: %d\n", t + 1, result);
}

int main(int argc, char** argv)
{
    char* filename = argv[1];
    ifstream input(filename);
    string line;
    int testcases = 0;
    if(input.is_open()){
        getline(input, line);
        testcases = parseInt(line);
    }
    for(int i = 0; i < testcases; i++){
        getline(input, line);
        vector<string> limits = split(line, ' ');
        integer min = parseInt(limits[0]);
        integer max = parseInt(limits[1]);
        printResult(i, numFairSquare(min, max));
    }
}

