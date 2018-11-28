#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <sstream>
#include <stdio.h>

using namespace std;

void escribirArchivo(vector<int> results){
    ofstream output ("output_large_B.txt");
    if (output.is_open())
      {
        for (int i = 0; i< results.size(); i++){
            output << "Case #" << i+1 << ": ";
            output << results[i];
            output << "\n";
        }
        output.close();
      }
      else cout << "Unable to open file";

}

char opuesto(char c){
    if (c == '+')
        return '-';
    else if (c == '-')
        return '+';
    return 'E';
}

int resolver(string line){
    char searching_char = '-';
    int contador = 0;
    for (int i = line.length()-1; i >=0; i--){
        if (line[i] == searching_char){
            contador++;
            searching_char = opuesto(searching_char);
        }
    }
    return contador;
}

int main()
{
  string line;
  ifstream myfile ("B-large.in");
  vector<int> results;
  if (myfile.is_open())
  {
    getline(myfile,line);
    int testCases  = atoi(line.c_str());
    cout << "tests :" << testCases << endl;
    for (int i = 0; i < testCases; i++){
        getline(myfile,line);
        cout << line << endl;
        results.push_back(resolver(line));
        cout << results[i] << endl;
    }
    escribirArchivo(results);
    myfile.close();

  }

  else cout << "Unable to open file";

  return 0;
}
