#include <iostream>
#include <fstream>
#include <locale>
#include <cmath>
#include <sstream>
using namespace std;

bool palindrome(int n)
{
    stringstream ss;
    string s;
    int i;

    ss << n;
    ss >> s;

    for(i=0;i<s.length();i++)
    {
        if(s[i] != s[s.length() - (i+1)])
            return false;
    }

    return true;
}

bool fair_and_square(int n)
{
    float sq;
    float number = (float) n;
    sq = sqrt(number);
    int int_sq;

    int_sq = (int) sq;

    if(sq == ceil(sq))
    {
        if((palindrome(n))&&(palindrome(int_sq)))
            return true;
    }

    return false;
}

main()
{
    //Variables
    ifstream infile("FairNSquare.in");
    ofstream outfile("FairNSquare.out");
    int n;
    int i, j, k;
    int a, b;
    int count;

    //Get number of cases
    infile >> n;

    //For each case
    for(i=0;i<n;i++)
    {
        //Print case number
        outfile << "Case #" << i+1 << ": ";
        count = 0;

        infile >> a >> b;

        for(j=a;j<=b;j++)
        {
            if(fair_and_square(j))
            {
                count += 1;
            }
        }

        outfile << count << endl;
    }
}
