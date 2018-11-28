#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    ofstream output;
    ifstream input ("D-large.in");
    output.open ("D-large.out");

    if(input.is_open())
    {
        int t;

        input >> t;
        for(int i = 1; i <= t; i++)
        {
            int n, DWar, War, indexNaomi;
            double temp;
            vector<double> Naomi, Ken;

            input >> n;
            for(int j = 0; j < n; j++)
            {
                input >> temp;
                Naomi.push_back(temp);
            }
            for(int j = 0; j < n; j++)
            {
                input >> temp;
                Ken.push_back(temp);
            }

            sort (Naomi.begin(), Naomi.end());
            sort (Ken.begin(), Ken.end());
            /*for(int j = 0; j < n; j++)
                cout << Naomi[j] << " ";
            cout << endl;
            for(int j = 0; j < n; j++)
                cout << Ken[j] << " ";
            cout << endl;*/

            DWar = 0, War = n;
            indexNaomi = n - 1;
            for(int j = n - 1; j >= 0; j--)
                if(Naomi[indexNaomi] > Ken[j])
                {
                    DWar++;
                    indexNaomi--;
                }
            indexNaomi = 0;
            for(int j = 0; j < n; j++)
                if(Naomi[indexNaomi] < Ken[j])
                {
                    War--;
                    indexNaomi++;
                }

            output << "Case #" << i << ": " << DWar << " " << War << endl;
        }
        output.close();
    }

    return 0;
}
