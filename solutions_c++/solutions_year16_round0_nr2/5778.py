#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

void flip(int n, std::vector<bool> *pila){
    if(n >= 0){
        std::reverse(pila->begin(), pila->begin()+n+1);
        for(int i = 0; i < n+1; ++i){
            //cout << pila->at(i) << endl;
            pila->at(i) = !(pila->at(i));
            //cout << pila->at(i) << endl << endl;
        }
    } else {
        pila->flip();
    }
}

int main()
{
    ifstream input_file;
    input_file.open("B-large.in", ifstream::in);
    ofstream output_file;
    output_file.open("B-large-output.txt", ofstream::out);
    string temp;
    getline(input_file, temp);

    int caso = 1;
    while(getline(input_file, temp)){
        vector<bool> pila;
        for(int i = 0; i < temp.length(); ++i){
            if(temp.at(i) == '+'){
                pila.push_back(true);
            } else {
                pila.push_back(false);
            }
        }

        int cant_flips = 0;

        int n = pila.size()-1;
        while(n >= 0 && pila[n]){
            pila.erase(pila.end());
            n--;
        }
        n = 0;
        while(n+1 < pila.size() && pila[n] == pila[n+1]){
            n++;
        }
        while(pila.size() > 0){
            flip(n, &pila);
            ++cant_flips;

            n = pila.size()-1;
            while(n >= 0 && pila[n]){
                pila.erase(pila.end());
                n--;
            }
            n = 0;
            while(n+1 < pila.size() && pila[n] == pila[n+1]){
                n++;
            }
        }

        output_file << "Case #" << caso << ": " << cant_flips << endl;
        ++caso;
    }

    input_file.close();
    output_file.close();
    return 0;
}
