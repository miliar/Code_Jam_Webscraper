#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input;
    ofstream output;

    input.open("input.txt");
    output.open("output.txt");

    int nbTestCases = 0, maxShyness = 0;
    string people;

    input >> nbTestCases;

    for(int i = 0 ; i < nbTestCases ; i++)
    {
        input >> maxShyness >> people;

        int nbStandingPeople = 0, nbFriends = 0;
        int nbShynessK = 0;

        for(int k = 0 ; k < people.size() ; k++)
        {
            nbShynessK = people[k] - '0';

            if(nbShynessK != 0)
            {
                if(nbStandingPeople < k)
                {
                    nbFriends += (k - nbStandingPeople);
                    nbStandingPeople = k;
                }

                nbStandingPeople += nbShynessK;
            }
        }

        output << "Case #" << i + 1 << ": " << nbFriends << endl;
    }

    input.close();
    output.close();

    return 0;
}
