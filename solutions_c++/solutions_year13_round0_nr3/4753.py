#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <string>
#define loopPaire(v) for(int i=0;i<v.size()/2;i++)
#define loopImpaire(v) for(int i=0;i<v.size()/2+1;i++)

using namespace std;

string convertInt(int number)
{
    if (number == 0)
        return "0";
    string temp="";
    string returnvalue="";
    while (number>0)
    {
        temp+=number%10+48;
        number/=10;
    }
    for (int i=0;i<temp.length();i++)
        returnvalue+=temp[temp.length()-i-1];
    return returnvalue;
}

bool isItPalindrom(string square)
{
    if(square.size()%2==0)
        loopPaire(square)
        {
            if(square[i]!=square[(square.size()-1)-i])
            {
                return false;
            }
        }
    else
        loopImpaire(square)
        {
            if(square[i]!=square[(square.size()-1)-i])
            {
                return false;
            }
        }
    return true;
}


int main() {

    int T;
    int A,B;
    int compteur=0;
    ofstream OUT ("small.out");
    ifstream IN ("small.in");
    IN >> T;
    for(int i=0;i<T;i++)
    {
        IN>>A;
        IN>>B;
        string number;
        string squareNumber;

        int j=0;
        while( (j*j) < A ) j++;
        while( (j*j) <= B ) {
            number=convertInt(j*j);
            squareNumber=convertInt(j);
            if(isItPalindrom(number)&&isItPalindrom(squareNumber))
                    compteur++;
        j++;
        }
        OUT <<"Case #"<<i+1<<": "<<compteur<<endl;
        compteur=0;
    }
    return 0;
}
