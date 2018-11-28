/*
 * =====================================================================================
 *
 *       Filename:  main.cc
 *
 *    Description:  Standinf Ovation
 *
 *        Version:  1.0
 *        Created:  12/04/15 01:17:52
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Thibault Savin (lppc), savinthiba@eisti.eu
 *   Organization:  Destiny Corporation
 *
 * =====================================================================================
 */

#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector< vector<int> > readFile(string filename)
{
   ifstream input(filename.c_str(), ios::in);

    vector< vector<int> > operaInputs;
    if(input) {
        int nb_lines = 0;
        string str;
        char c;

        getline(input, str);
        nb_lines = atoi(str.c_str());

        for(int i(0); i < nb_lines; i++) {
            vector<int> pop;
            str = "";
            
            c = '\0';
            while(c != ' ') {
                input.get(c);
                str += c;
            }
            pop.push_back(atoi(str.c_str()));
            operaInputs.push_back(pop);
            while(c != '\n') {
                input.get(c);
                cout << c << " ";
                operaInputs[i].push_back(atoi((&c)));
            }
            operaInputs[i].pop_back();
            cout << endl;
        }
        input.close();
   } else {
       cerr << "Can't open file \"" + filename + "\"!" << endl;
   }
   return operaInputs;
}

void writeFile(vector<int> results)
{
    ofstream output("output.txt", ios::out | ios::trunc);

    if(output) {
        for(int i(0); i < results.size(); i++) {
            output << "Case #" << (i+1) << ": " << results[i] << endl;
        }
        output.close();
    } else {
        cerr << "Can't create the file output.txt" << endl;
    }
}

vector<int> getOvation(vector< vector<int> > operaInputs)
{
    vector<int> results;
    int nb_standUp(0), nb_friend(0);
    for(int i(0); i < operaInputs.size(); i++) {
        nb_standUp = 0;
        nb_friend = 0;
        for(int j(1); j < operaInputs[i].size(); j++) {
            nb_standUp += operaInputs[i][j];
            if(nb_standUp < j) {
                nb_standUp++;
                nb_friend++;
            }
        }
        results.push_back(nb_friend);
    }
    return results;
}

int main(int argc, char** argv){
    
    vector< vector<int> > infos = readFile("input.txt");
    vector<int> results = getOvation(infos);
    cout << "Printing..." << endl;
    for(int i(0); i < infos.size(); i++) {
        cout << infos[i][0] << " " << infos[i].size() << " ";
        for(int j(1); j < infos[i].size(); j++)
            cout << infos[i][j];
        cout << endl;
    }
    cout << "done." << endl;
   
    cout << "Printing results...";
    for(int i(0); i < results.size(); i++) {
        cout << results[i] << endl;
    }

    writeFile(results);
    return 0;
}


