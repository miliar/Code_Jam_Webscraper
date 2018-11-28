#include <iostream>
#include <string>
#include <math.h>
#include <iomanip>
#include <locale>
#include <sstream>
#include <fstream>

using namespace std;

string N2S (int a)
{
     ostringstream ss;
     ss << a;
     return ss.str();
}

int palindrom(string a)
{
    if (a.size()== 1) {return 1;}
    int test = a.size();
    int i, counter = 0;
    for (i=0; i<test/2; i++)
    {
        if (a[i]!=a[test-i-1]) {counter++;}
        //cout << counter << endl;
    }
    if (counter > 0) { return 0;}
    if (counter == 0) { return 1;}

}

int main()
{
    ofstream out;
    out.open ("output.txt");
    int i;
    string Result1, Result2;
    ostringstream convert;
    int testcase, test;
    cin >> testcase;
    int counter[testcase];
    int number1[testcase], number2[testcase];
    int number3 = 0;
    double number4 = 0.0;
    for (test=0; test<testcase; test++)
    {
        counter[test] = 0;
        cin >> number1[test];
        cin >> number2[test];
        for (i=number1[test]; i<=number2[test]; i++)
        {
            number3 = sqrt(i);
            number4 = sqrt(i);
            Result1 = N2S(i);
            Result2 = N2S(number3);
            if (number3 == number4)
            {
                if (palindrom(Result1)==1 && palindrom(Result2)==1) {counter[test]++;}
            }
        }
    }
    cout << "\n";
    for (i=0; i<testcase; i++)
    {
        cout << "Case #" << i+1 <<": " << counter[i] << endl;
        out << "Case #" << i+1 <<": " << counter[i] << endl;
    }

    cout << "\n";
    out << "\n";
    out.close();
    return 0;
}

