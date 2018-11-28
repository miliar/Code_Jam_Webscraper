#include<iostream>
#include<string>
#include<sstream>
#include<cmath>


using namespace std;

bool palin(unsigned long long input);
bool square(unsigned long long input);


int main ()
{
    long cases;
    cin >> cases;
    for(int i = 1; i<=cases; i++)
    {
        long counter = 0;
        unsigned long long low, high;
        cin >> low >> high;
        for (low; low <= high; low++)
            if(palin(low) && square(low))
                counter++;
        cout << "Case #" << i << ": " << counter << endl;
    }
}

bool square(unsigned long long input)
{
    if(sqrt(input) != (unsigned long long)sqrt(input))
        return false;
    else {
        unsigned long long test = sqrt(input);
        return palin(test);
    }
}

bool palin(unsigned long long input)
{
    string test;
    ostringstream conv;
    conv << input;
    test = conv.str();
    unsigned long long len = test.length() - 1;

    for(int i = 0; i <= len; i++)
    {
        if(test[i] != test[len - i])
            return false;
    }
    return true;

}
