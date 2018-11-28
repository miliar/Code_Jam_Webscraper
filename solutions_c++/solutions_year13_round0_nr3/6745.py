#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

bool checkPalindrome (int num)
{
    int n = 0, rev = 0, dig = 0;
    n = num;
    rev = 0;
    while (num > 0)
    {
        dig = num % 10;
        rev = rev * 10 + dig;
        num = num / 10;
    }
    return rev == n;
}

bool squareRoot (int start, int &frac)
{
    double sqrtNum = 0.0, fractPart = 0.0, intpart = 0.0;
    sqrtNum = sqrt (start);
    fractPart = modf (sqrtNum, &intpart);
    if (fractPart == 0.0)
    {
        frac = int (sqrtNum);
        return true;
    }
    else
        return false;
}

int calculate (int start,int end)
{
    int count = 0;
    bool isPalindrome = false, gotPerfectSquareRoot = false;
    for (;start <= end;start++)
    {
        if (start == 1)
            count++;
        else
        {
            isPalindrome = checkPalindrome (start);
            if (isPalindrome)
            {
                int num = 0;
                gotPerfectSquareRoot = squareRoot (start, num);
                if (gotPerfectSquareRoot && checkPalindrome (num))
                    count++;
            }
        }
    }
    return count;
}

int main (void)
{
    const char* filename = "input";
    const char* ofilename = "output";
    ifstream infile (filename);
    ofstream ofile (ofilename);
    int i, start, end, iterator = 0;
    infile >> i;
    while (iterator < i)
    {
        infile>>start;
        infile>>end;
        int count = 0;
        count = calculate (start, end);
        ofile << "Case #"<<iterator+1<<": "<<count<<endl;
        iterator++;
    }
    return 0;
}
