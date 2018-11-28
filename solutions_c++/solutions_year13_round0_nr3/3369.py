#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <math.h>
int isPalindrome(int num);
using namespace std;
int main()
{
    vector <string> outputStr;
    int T = 0;
    ifstream inFile;
    ofstream outFile;
    stringstream ss;
    string line;
    //stringstream ss;
    int temp;
    double dtemp;
    string output;

    inFile.open("C-small-attempt0.in");
    if(!inFile.is_open())
    {
        printf("Input file is invalid\n");
    }
    getline(inFile, line);
    //std::istringstream ss(line);
    ss << line;

    ss >> T;
    ss.clear();

    cout << T << endl;

    for (int case_ = 0; case_ < T; case_++ ){
        getline(inFile, line);
        std::stringstream stream(line);
        int count = 0;
        int b, e;
        while(1) {
           int n;
           stream >> n;
           if(!stream)
              break;
           if (count==0) b = n;
           else e = n;
           count ++;
        }
        cout << "begin: " << b<< ", end:" << e << endl;
        int palCount = 0;
        for (int i = b; i <= e; i++){
            if (isPalindrome(i)==1){
                int s = (int) (sqrt((float)i) + 0.5f);
                if((s*s) == i)
                {
                    if (isPalindrome(s) == 1) {
                        cout << s << "  "<< i << endl;
                        palCount++;
                    }
                }
            }
        }
        string res;
        string resLine("Case #");
        stringstream s2;
        s2 << case_+1;
        stringstream s3;
        s3 << palCount;
        //ss.str();
        resLine.append(s2.str()).append(": ");
        s2.clear();
        resLine.append(s3.str()).append("\n");
        outputStr.push_back(resLine);
    }
    inFile.close();
    fstream plik( "output.in", ios::out );

    for (int i = 0; i < T; i++){
        plik << outputStr.at(i);
    }
    plik.close();
    cout << T << endl;
    return 0;
    return 0;
}
int isPalindrome(int num){
    if ((num % 10)==0) return 0;
    int n = num;
    int rev = 0;
    while (n > 0)
    {
        int dig = n % 10;
        rev = rev * 10 + dig;
        n = n / 10;
    }
    if (rev == num) return 1;
    return 0;
}
