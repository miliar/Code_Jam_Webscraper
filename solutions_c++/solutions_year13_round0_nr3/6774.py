#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

bool isPalindrome(unsigned int i)
{
    unsigned int rev = 0, old = i;
    while(i > 0)
    {
        rev = 10 * rev + i % 10;
        i /= 10;
    }

    return (old == rev);
}

int main()
{
    ifstream inFile("C-small-attempt0.in", ios::in);
    ofstream outFile("C-small-attempt0.out", ios::out | ios::trunc);

    unsigned int T;
    inFile >> T;

    for(unsigned int t = 1 ; t <= T ; t++)
    {
        unsigned int A, B;
        inFile >> A;
        inFile >> B;

        unsigned int a = ceil(sqrt(A)), b = floor(sqrt(B));
        unsigned int counter = 0;

        for(unsigned int i = a ; i <= b ; i++)
        {
            if(isPalindrome(i) && isPalindrome(i*i))
                counter++;
        }

        outFile << "Case #" << t << ": " << counter << endl;
    }

    inFile.close();
    outFile.close();

    return 0;
}
