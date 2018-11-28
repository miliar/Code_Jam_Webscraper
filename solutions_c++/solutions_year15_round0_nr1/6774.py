#include <iostream>
#include <string>
#include <boost/lexical_cast.hpp>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int i = 0; i < T; i++)
    {
        int maxS;
        string line;
        cin >> maxS;
        cin >> line;
        int standing = 0;
        int needed = 0;
        for(int j = 0; j < line.length(); j++)
        {
            if(standing >= j)
            {
                int x = boost::lexical_cast<int>(line.at(j));
                standing += x;
            }
            else
            {
                int x = boost::lexical_cast<int>(line.at(j));
                needed += (j-standing);
                standing += (j-standing);
                standing += x;


            }

        }
        cout << "Case #" << i+1<< ": "<< needed << endl;


    }
}

