#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>

using namespace std;

bool isFair(int number)
{
    string numString = "";
    ostringstream convert;
    convert << number;
    numString = convert.str();

    if(numString.length() == 3){
        if(numString[0] == numString[2]){
            return true;
        }
    }

    if(numString.length() == 2){
        if(numString[0] == numString[1]){
            return true;
        }
    }

    if(numString.length() == 1){
            return true;
    }

    return false;
}

bool isSquare(int number)
{
    if((int)sqrt(number) == sqrt(number)){
        return isFair(sqrt(number));
    }

    return false;
}

int main()
{
    int testCases;
    int count;
    int A,B;

    cin >> testCases;

    for(int i = 0; i < testCases; i++)
    {
        count = 0;

        cin >> A;
        cin >> B;

        for(int j = A; j <= B; j++)
        {
            if(isFair(j) && isSquare(j)){
                count++;
            }
        }

        cout << "Case #"<< i+1 << ": " << count << "\n";
    }
}
