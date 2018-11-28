#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iterator>
#include <sstream>
#include <cstdlib>
#include <cstring>
using namespace std;
int main (){
    string line;
    int N;
    int numShyness = 0;
    int sum = 0;
    int clappersNeeded = 0;
    ifstream input ("A-large.in");
    ofstream output ("p1.out");
    if (input.is_open()){
        getline (input, line);
        stringstream (line) >> N;
        for (int i = 0; i < N; i ++){
            getline (input, line);
            istringstream iss(line);
            vector<string> tokens{istream_iterator<string>{iss}, istream_iterator<string>{}};
            stringstream (tokens[0])>>numShyness;
            numShyness++;
            int freq[numShyness];
            char strArray [numShyness];
            strcpy(strArray, tokens[1].c_str());

            for (int j = 0; j < numShyness; j++){
                freq[j] = strArray[j]-'0';
            }

            sum+=freq[0];
            //cout << sum <<endl;
            for (int j = 1; j < numShyness; j++){
                if (sum>=j){
                    sum+=freq[j];
                }
                else{
                    int difference = j - sum;
                    clappersNeeded+= difference;
                    sum+= difference + freq[j];
                }
            }
            output << "Case #" << i+1 << ": " << clappersNeeded << endl;
            clappersNeeded = 0;
            sum = 0;
            numShyness = 0;
        }
        input.close();
        output.close();
    }


}
