#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <utility>
#include <stdlib.h>
#include <algorithm>
#include <iomanip>
#include <math.h>

using namespace std;

vector<string> explode(string inputstring, string delimiter)
{
    vector<string> explodes;
    inputstring.append(delimiter);
    while(inputstring.find(delimiter)!=string::npos){
        explodes.push_back(inputstring.substr(0, inputstring.find(delimiter)));
        inputstring.erase(inputstring.begin(), inputstring.begin()+inputstring.find(delimiter)+delimiter.size());
    }
    return explodes;
}

int main()
{
    ifstream file("file.txt");

    vector<string> data(3);

    ofstream fichier("result.txt", ios::out | ios::trunc);

    if(file)
    {
        string row;
        getline(file, row);

        int nb_case = atoi(row.c_str());

        double c = 0, f = 0, x = 0;

        double r_lim = 0, time = 0;
        int nb_farm = 0;


        for(int a = 0; a < nb_case; a++)
        {
            time = 0;

            getline(file, row);

            data = explode(row, " ");

            c = atof(data[0].c_str());
            f = atof(data[1].c_str());
            x = atof(data[2].c_str());

            // Here we calculate the cookies per sec value limit for optimality.

            r_lim = f*(x/c-1);

            // Time for having a rate of cookies/sec >= r_lim

            nb_farm = floor((r_lim - 2)/f) + 1;

            if(nb_farm < 0)
                nb_farm = 0;

            for(int i = 0; i < nb_farm; i++)
                time += c/(2+i*f);

            time += x/(2+ nb_farm*f);

            cout << "Case #" << a+1 << ": " << fixed << setprecision(10) << time << endl;
            fichier << "Case #" << a+1 << ": " << fixed << setprecision(10) << time << endl;
        }


    }
    else
    {
        cout << "Not found." << endl;
    }

    return 0;
}
