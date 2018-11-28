#include <iostream>
#include <string>
#include <limits>
#include <math.h>
#include <sstream>

using namespace std;

bool palindrome(string chaine)
{
    int taille = chaine.size() - 1;
    for (int i = 0; i < chaine.size(); ++i)
    {
        if ((chaine[i] != chaine[taille - i]))
        {
            return false;
        }
    }
    return true;
}

int square(int number)
{
    if (number == 1)
    {
        return true;
    }
    int i = 2;
    while (i < number)
    {
        if (pow(i, 2) == number)
        {
            return i;
        }
        ++i;
    }
    return -1;
}

int calculFair(int min, int max)
{
    int nbFair = 0;
    for (int i = min; i <= max; ++i)
    {
        int sw = square(i);
        string racine = static_cast<ostringstream*>(&(ostringstream() << sw))->str();
        string ch = static_cast<ostringstream*>(&(ostringstream() << i))->str();
        if ((sw != -1) && palindrome(racine) && palindrome(ch))
        {
            ++nbFair;
        }
    }
    return nbFair;
}

bool fair(int val)
{
    string ch = static_cast<ostringstream*>(&(ostringstream() << val))->str();
    if (square(val) && palindrome(ch))
    {
        return true;
    }
}

int main()
{
    int nbTest;
    int min, max;
    cout << "Input : " << endl << endl;
    cin >> nbTest;

    string intervale;
    string resultat[nbTest];
    cin.ignore(numeric_limits<int>::max(), '\n');
    for (int k = 0; k < nbTest; ++k)
    {
        getline(cin, intervale);

        string cmin;
        string cmax;
        int i = 0;
        while (intervale[i] != ' ')
        {
            cmin += intervale[i];
            ++i;
        }

        for (int j = i + 1; j < intervale.size(); ++j)
        {
            if (intervale[j] != ' ')
            {
                cmax += intervale[j];
            }
        }
        istringstream(cmin) >> min;
        istringstream(cmax) >> max;

        resultat[k] = "Case #" + static_cast<ostringstream*>(&(ostringstream() << (k + 1)))->str() + ": " +
                static_cast<ostringstream*>(&(ostringstream() << calculFair(min, max)))->str();
    }

    for (int i = 0; i < nbTest; ++i)
    {
        cout << resultat[i] << endl;
    }

    cout << endl;
        //cout << min << endl << max << endl;
}

