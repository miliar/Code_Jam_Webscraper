#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <utility>
#include <stdlib.h>
#include <algorithm>


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

    ofstream fichier("result.txt", ios::out | ios::trunc);

    if(file)
    {
        string row;

        int nb_case = 0;
        bool next = true;

        string result;

        int answer_1, answer_2;
        vector<string> array1(4);
        vector<string> array2(4);

        getline(file, row);

        nb_case = atoi(row.c_str());



        for(int i = 0; i < nb_case; i++)
        {
            getline(file, row);
            answer_1 = atoi(row.c_str());
            for(int j = 0; j < answer_1; j++)
                getline(file, row);
            array1 = explode(row, " ");
            for(int j = answer_1; j < 4; j++)
                getline(file, row);

            getline(file, row);
            answer_2 = atoi(row.c_str());
            for(int j = 0; j < answer_2; j++)
                getline(file, row);

            array2 = explode(row, " ");
            for(int j = answer_2; j < 4; j++)
                getline(file, row);

            next = true;

            for(int j = 0; j < 4; j++)
            {
                if(find(array1.begin(), array1.end(), array2[j]) != array1.end())
                {
                    result = array2[j];
                    if(!next)
                        result = "Bad magician!";
                    next = false;
                }
            }

            if(next)
                result = "Volunteer cheated!";

            cout << "Case #" << i+1 << ": " << result << endl;
            fichier << "Case #" << i+1 << ": " << result << endl;
        }
    }
    else
    {
        cout << "Not found." << endl;
    }

    return 0;
}
