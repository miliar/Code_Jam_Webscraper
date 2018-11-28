#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input("input.txt", ios::in);
    ofstream output("output.txt", ios::out | ios::trunc);

    if(input && output)
    {
        int nbTest;

        input >> nbTest;

        cout << "nombre de tests : " << nbTest << endl;


        for(int i(0); i < nbTest; i++)
        {
            int sMax;

            input >> sMax;
            input.get();

            cout << "sMax : " << sMax << endl;

            int *s = new int[sMax+1];

            for(int j(0); j <= sMax; j++)
            {
                s[j] = input.get() - '0';
                if(s[j] != -49)
                    cout << s[j] << " ";
            }
            cout << endl;
            input.get();

            output << "Case #" << i+1 << ": ";

            int compteur(0);
            int friends(0);
            for(int j(0); j <= sMax; j++)
            {
                compteur += s[j];
                while(j >= (compteur+friends))
                {
                    friends++;
                }
            }

            output << friends << endl;

            delete[] s;
        }

        input.close();
        output.close();
    }
    else
        cout << "Fail load";

    return 0;
}


