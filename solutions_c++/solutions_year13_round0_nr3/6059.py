#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

string intToString(const long long i)
{
    stringstream ss;
    string s;
    ss << i;
    s = ss.str();

    return s;
}

bool checkPalindrome(string &number)
{
    int length = number.length();
    for (int i = 0; i <= length / 2; i++)
        if (number[i] != number[length - 1 - i])
            return false;

    return true;
}

void createPalSqFile()
{
    ofstream out("pal_sq.txt");
    if (!out)
    {
        cout << "failed to save file: " << out << endl;
        return;
    }

    string s;
    long long temp;
    for (long long i = 1; i < 1000000000; i++)
    {
        s = intToString(i);
        if (checkPalindrome(s))
        {
            temp = i * i;
            s = intToString(temp);
            if (checkPalindrome(s))
                out << temp << endl;
        }
    }
}

int main()
{
    cout.setf(ios::fixed);
    vector <long long> correct;

    ifstream in1("pal_sq.txt");
    if(!in1)
       createPalSqFile();

    while (!in1.eof())
    {
        long long temp;
        in1 >> temp;
        correct.push_back(temp);
    }
    in1.close();
    ifstream in("C:\\Users\\Nikos\\Downloads\\input.txt");
    if(!in)
    {
        cout << endl << "failed to load data file" << endl;
        return -1;
    }
    long long examples, minNumber, maxNumber, count, temp;
    in >> examples;
    string s;
    long double squared;
    vector <long long> cache;

    for (int ex = 1; ex <= examples; ex++)
    {
        count = 0;
        in >> minNumber;
        in >> maxNumber;
        for (long long i = minNumber ; i <= maxNumber; i++)
        {
            if (find(correct.begin(), correct.end(), i) != correct.end())
                count++;
//            s = intToString(i);
//            if (!checkPalindrome(s))
//                continue;

//            squared = sqrt(i);
//            if (fmod(squared, 1) > 0.000001)
//                continue;

//            s = intToString((long long)(squared));
//            if (checkPalindrome(s))
//            {
//                count++;
// //               cout << i << " ";
//            }
        }
//        cout << endl;
        cout << "Case #" << ex << ": " << count << endl;
    }
    return 0;
}

