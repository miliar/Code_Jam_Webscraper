#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
#include <sstream>

using namespace std;



bool isPal(int nb)
{
    ostringstream convert;
    convert << nb;
    string str = convert.str();

    for(int i=0 ; i<str.length()/2 ; i++)
        if(str[i] != str[str.length()-1-i])
            return false;
    return true;
}

int nbPal(int a, int b)
{
    int min = ceil(sqrt(a));
    int max = sqrt(b);
    int nb=0;

    for(int i=min ; i<=max ; i++)
    {
        if(isPal(i) && isPal(i*i))
            nb++;
    }

    return nb;
}


int main()
{
    ifstream in("in.txt", ios::in);
    ofstream out("out.txt", ios::out | ios::trunc);

    int nb;
    in >> nb;

    for(int n=0 ; n<nb ; n++)
    {

        int a, b;
        in >> a;
        in >> b;

        out << "Case #" << n+1 << ": " << nbPal(a, b) << endl;
    }

    out.close();
    in.close();

    return 0;
}
