#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cstdlib>

using namespace std;

int get_int(string line, int ** intarray){
    size_t startpos = 0;
    size_t spacepos = 0;
    spacepos = (line.find(" ", startpos));
    (*intarray)[0] = atoi(line.substr(startpos, spacepos-startpos).c_str());
    startpos = spacepos + 1;
    spacepos = (line.find(" ", startpos));
    (*intarray)[1] = atoi(line.substr(startpos, spacepos-startpos).c_str());
    startpos = spacepos + 1;
    spacepos = (line.find(" ", startpos));
    (*intarray)[2] = atoi(line.substr(startpos, spacepos-startpos).c_str());
    startpos = spacepos + 1;
    (*intarray)[3] = atoi(line.substr(startpos).c_str());

    return 0;
}

int compare_two_array(int * firstarray, int * secondarray){
    int i, j;
    int match = 0;
    int result;
    for (i = 0; i < 4; i++){
        for (j = 0; j < 4; j++){
            if (firstarray[i] == secondarray[j]){
                match++;
                result = firstarray[i];
            }
        }
    }
    if (match > 1)
        return -1;
    if (match)
        return result;
    return match;
}

int main(){
    ofstream output;
    ifstream input;
    string line;

    int totalcase;
    int currentcase;

    int firstguess;
    int secondguess;

    int * firstarray = (int *)malloc(4 * sizeof(int));
    int * secondarray = (int *)malloc(4 * sizeof(int));

    int match;
    int currentline;

    input.open("A-small-attempt1.in");
    output.open("output.txt");
    if (input.is_open()){
        getline(input, line);
        totalcase = atoi(line.c_str());
        currentcase = 1;
        while (currentcase <= totalcase){
            currentline = 1;
            while (currentline <= 10) {
                getline(input, line);
                if (currentline == 1){
                    firstguess = atoi(line.c_str());
                }
                if (currentline == firstguess + 1){

                    get_int(line, &firstarray);
                }
                if (currentline == 6){
                    secondguess = atoi(line.c_str());
                }
                if (currentline == secondguess + 6){
                    get_int(line, &secondarray);
                }
                currentline++;
            }
            match = compare_two_array(firstarray, secondarray);
          //  cout << currentcase << "\n";
         //   cout << firstarray[0] << " " << firstarray[1] << " " << firstarray[2] << " " << firstarray[3] <<"\n";
        //    cout << secondarray[0] << " " << secondarray[1] << " " << secondarray[2] << " " <<secondarray[3] <<"\n";
            switch (match){
            case 0:
                output << "Case #" << currentcase << ": Volunteer cheated!\n";
                break;
            case -1:
                output << "Case #" << currentcase << ": Bad magician!\n";
                break;
            default:
                output << "Case #" << currentcase << ": " << match << "\n";

            }
            currentcase++;
        }

    }
    output.close();
    return 0;
}

