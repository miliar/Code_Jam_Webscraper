#include <iostream>
#include <string>
#include <limits>
#include <sstream>

using namespace std;

bool rechercheVictoire(string tabCarac[4], char *lettre)
{
    int nbX = 0;
    for (int i = 0; i < 4; ++i)
    {
        if ((tabCarac[i][i] == 'X') || (tabCarac[i][i] == 'T'))
        {
            ++nbX;
        }
    }
    if (nbX == 4)
    {
        *lettre = tabCarac[0][0];
        return true;
    }

    int nbO = 0;
    for (int i = 0; i < 4; ++i)
    {
        if ((tabCarac[i][i] == 'O') || (tabCarac[i][i] == 'T'))
        {
            ++nbO;
        }
    }
    if (nbO == 4)
    {
        *lettre = tabCarac[0][0];
        return true;
    }

    nbX = 0;
    int j = 3;
    for (int i = 0; i < 4; ++i)
    {
        if ((tabCarac[i][j] == 'X') || (tabCarac[i][j] == 'T'))
        {
            ++nbX;
        }
        --j;
    }
    if (nbX == 4)
    {
        *lettre = tabCarac[0][3];
        return true;
    }

    nbO = 0;
    j = 3;
    for (int i = 0; i < 4; ++i)
    {

        if ((tabCarac[i][j] == 'O') || (tabCarac[i][j] == 'T'))
        {
            ++nbO;
        }
        --j;
    }
    if (nbO == 4)
    {
        *lettre = tabCarac[0][3];
        return true;
    }


    // parcour de toutes les lignes

    for (int i = 0; i < 4; ++i)
    {
        char carcP = tabCarac[i][0];
        int nbXorO = 1;
        if ((carcP == 'O') || (carcP == 'X') || (carcP == 'T'))
        {
            for (int j = 1; j < 4; ++j)
            {
                char carcS = tabCarac[i][j];
                if ((carcS == carcP) || carcS == 'T')
                {
                    ++nbXorO;
                }
                else
                {
                    break;
                }
            }
            if (nbXorO == 4)
            {
                *lettre = carcP;
                return true;
            }
        }
    }

    // parcour de toutes les colones
    for (int i = 0; i < 4; ++i)
    {
       char carcP = tabCarac[0][i];
       int nbXorO = 1;
       if ((carcP == 'O') || (carcP == 'X') || (carcP == 'T'))
       {
           for (int j = 1; j < 4; ++j)
           {
               char carcS = tabCarac[j][i];
               if ((carcS == carcP) || carcS == 'T')
               {
                   ++nbXorO;
               }
               else
               {
                   break;
               }
           }
           if (nbXorO == 4)
           {
               *lettre = carcP;
               return true;
           }
       }
    }
    return false;
}

bool rechercheEvidence(string tabCarac[4], char *lettreV)
{
    int nbChoixO = 0;
    int nbChoixX = 0;
    int nbX = 0;
    for (int i = 0; i < 3; ++i)
    {
        if ((tabCarac[i][i] == 'X') || (tabCarac[i][i] == 'T'))
        {
            ++nbX;
        }
    }
    if (nbX == 3)
    {
        ++nbChoixX;
    }

    int nbO = 0;
    for (int i = 0; i < 3; ++i)
    {
        if ((tabCarac[i][i] == 'O') || (tabCarac[i][i] == 'T'))
        {
            ++nbO;
        }
    }
    if (nbO == 3)
    {
        ++nbChoixO;
    }

    nbX = 0;
    int j = 3;
    for (int i = 0; i < 3; ++i)
    {
        if ((tabCarac[i][j] == 'X') || (tabCarac[i][j] == 'T'))
        {
            ++nbX;
        }
        --j;
    }
    if (nbX == 3)
    {
        ++nbChoixX;
        if (nbChoixX == 2)
        {
            *lettreV = 'X';
            return true;
        }
    }

    nbO = 0;
    j = 3;
    for (int i = 0; i < 3; ++i)
    {

        if ((tabCarac[i][j] == 'O') || (tabCarac[i][j] == 'T'))
        {
            ++nbO;
        }
        --j;
    }
    if (nbO == 3)
    {
        ++nbChoixO;
        if (nbChoixO == 2)
        {
            *lettreV = 'O';
            return true;
        }
    }


    else if (nbChoixO == 2)
    {
        *lettreV = 'O';
        return true;
    }

    // parcour de toutes les lignes

    for (int i = 0; i < 4; ++i)
    {
        char carcP = tabCarac[i][0];
        int nbXorO = 1;
        if ((carcP == 'O') || (carcP == 'X') || (carcP == 'T'))
        {
            for (int j = 1; j < 3; ++j)
            {
                char carcS = tabCarac[i][j];
                if ((carcS == carcP) || carcS == 'T')
                {
                    ++nbXorO;
                }
                else
                {
                    break;
                }
            }
            if (nbXorO == 3 and carcP == 'X')
            {
                ++nbChoixX;
                if (nbChoixX == 2)
                {
                    *lettreV = 'X';
                    return true;
                }
            }
            else if (nbXorO == 3 and carcP == '0')
            {
                ++nbChoixO;
                if (nbChoixO == 2)
                {
                    *lettreV = 'O';
                    return true;
                }
            }
        }
    }

    // parcour de toutes les colones
    for (int i = 0; i < 4; ++i)
    {
       char carcP = tabCarac[0][i];
       int nbXorO = 1;
       if ((carcP == 'O') || (carcP == 'X') || (carcP == 'T'))
       {
           for (int j = 1; j < 3; ++j)
           {
               char carcS = tabCarac[j][i];
               if ((carcS == carcP) || carcS == 'T')
               {
                   ++nbXorO;
               }
               else
               {
                   break;
               }
           }
           if (nbXorO == 3 and carcP == 'X')
           {
               ++nbChoixX;
               if (nbChoixX == 2)
               {
                   *lettreV = 'X';
                   return true;
               }
           }
           else if (nbXorO == 3 and carcP == '0')
           {
               ++nbChoixO;
               if (nbChoixO == 2)
               {
                   *lettreV = 'O';
                   return true;
               }
           }
       }
    }
    return false;
}

int main()
{
    int nbTest = 0;
    string tabCarac[4];
    bool victoire = false;
    int nbCaracPoint = 0;
    char *lettreV = new char;

    cout << "Input" << endl << endl;
    cin >> nbTest;
    string resultat[nbTest];

    cin.ignore(numeric_limits<int>::max(), '\n');
    for (int k = 0; k < nbTest; ++k)
    {
        for (int i = 0; i < 4; ++i)
        {
            getline(cin, tabCarac[i]);
            for (int j = 0; j < 4; ++j)
            {
                if (tabCarac[i][j] == '.')
                {
                    ++nbCaracPoint;
                }
            }
        }

        victoire = rechercheVictoire(tabCarac, lettreV);
        if (victoire)
        {
            resultat[k] = "Case #" +
                    static_cast<ostringstream*>(&(ostringstream() << (k + 1)))->str() + ": " + *lettreV + " won";
        }
        else
        {
            if (nbCaracPoint == 0)
            {
                resultat[k] = "Case #" +
                        static_cast<ostringstream*>(&(ostringstream() << (k + 1)))->str() + ": Draw";
            }
            else
            {
                    resultat[k] = "Case #" +
                            static_cast<ostringstream*>(&(ostringstream() << (k + 1)))->str() + ": Game has not completed";
            }
        }
        nbCaracPoint = 0;
    }
    cout << endl;

    for (int i = 0; i < nbTest; ++i)
    {
        cout << resultat[i] << endl;
    }

    cout << endl;
    return 0;
}

