#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int getSenadoresTotales(vector<int> &senadores) {
    int senadores_restantes = 0;
    for(int i = 0; i < senadores.size(); ++i){
        senadores_restantes += senadores[i];
    }
    return senadores_restantes;
}

void getPorcentajes(vector<int> &senadores, vector<double> &porcentajes){
    int senadores_totales = getSenadoresTotales(senadores);
    for(int i = 0; i < senadores.size(); ++i){
        porcentajes.push_back(senadores[i] / (double)senadores_totales);
    }
}

int findMax(vector<double> &elems){
    double maximo = -1;
    int index = -1;
    for(int i = 0; i < elems.size(); ++i){
        if(elems[i] >= maximo){
            index = i;
            maximo = elems[i];
        }
    }
    return index;
}

bool checkPorcentajes(vector<double> porcentajes){
    for(int i = 0; i < porcentajes.size(); ++i){
        if(porcentajes[i] > 0.5){
            return false;
        }
    }
    return true;
}

int main()
{
    ifstream input_file;
    input_file.open("A-large.in", ifstream::in);
    ofstream output_file;
    output_file.open("A-large-output.txt", ofstream::out);

    string temp;
    getline(input_file, temp);

    int caso = 1;
    string evac;
    while(getline(input_file, temp)){
        int N = std::stoi(temp, 0, 10);
        evac = "";

        vector< int > senadores;

        getline(input_file, temp);
        stringstream ss;
        ss << temp;
        string t;
        while(getline(ss, t, ' ')){
            senadores.push_back(std::stoi(t, 0, 10));
        }


        /*for(int i = 0; i < senadores.size(); ++i){
            cout << senadores[i] << " ";
        }
        cout << endl;*/

        vector< double > porcentajes;

        while(getSenadoresTotales(senadores) > 0){
            porcentajes.clear();
            getPorcentajes(senadores, porcentajes);
            int senador_se_va = findMax(porcentajes);
            //cout << senador_se_va << endl;
            senadores[senador_se_va]--;
            evac += ((char)(senador_se_va+65));

            if(getSenadoresTotales(senadores) > 0){
                porcentajes.clear();
                getPorcentajes(senadores, porcentajes);
                int senador_se_va = findMax(porcentajes);
                //cout << senador_se_va << endl;
                senadores[senador_se_va]--;

                porcentajes.clear();
                getPorcentajes(senadores, porcentajes);
                if(checkPorcentajes(porcentajes)){
                    evac += ((char)(senador_se_va+65));
                } else {
                    senadores[senador_se_va]++;
                }
            }

            evac.append(" ");
        }

        output_file << "Case #" << caso << ": " << evac << endl;
        ++caso;
    }

    input_file.close();
    output_file.close();
    return 0;
}
