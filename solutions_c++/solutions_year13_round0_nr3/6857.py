#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <sstream>

using namespace std;

bool isFair(int n)
{
    stringstream ss;
    ss << n;
    string s = ss.str();

    for(unsigned int i(0); i<s.length(); ++i)
        if(s[i] != s[s.length()-i-1])
            return false;
    return true;
}

int square(int x)
{
    return x*x;
}

int findFairAndSquare(int a, int b)
{
    int n = (int)ceil(sqrt(a));
    int cpt = 0;

    while (square(n) <= b)
    {
        if (isFair(n) && isFair(square(n)))
            ++cpt;
        ++n;
    }
    return cpt;
}

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        cout << "Nombre d'arguments incorrect" << endl;
        return 1;
    }

    ifstream in(argv[1]);
    ofstream out(argv[2]);

    if (!in || !out)
    {
        cout << "Erreur lors de l'ouverture du fichier " << endl;
        return 1;
    }

    int tests, n(1), a, b;
    in >> tests;

    while (n <= tests)
    {
        in >> a >> b;
        out << "Case #" << n << ": " << findFairAndSquare(a, b) << endl;
        ++n;
    }
    return 0;
}

