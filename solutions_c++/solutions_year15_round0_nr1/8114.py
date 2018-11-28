#include <iostream>
#include <string>
#include <fstream>

using namespace std;






int nb_members( string line , int maxShy) {

    int ret(0);
    int members[line.size()];
    int nbPeople(0);

    //put each int in array
    for (int i = 0; i < line.size(); i++ ) {
        members[i] = line[i] - '0';
    }





    //count missed people
    for (int i = 0;i < line.size(); i++) {

        if ( i > nbPeople && members[i] != 0) {
            int tmp = ( (i - (nbPeople + ret)) < 0 ) ? 0 : (i - (nbPeople + ret));
            ret = ret + tmp;

        }
        nbPeople += members[i];
    }


    return ret;
}





int main () {

    ifstream reading("A-large.in");
    ofstream writing("outputLARGEA.out");
    string line;
    int maxShy(0);


    int nbCases(0);
    reading >> nbCases;

    for (int i = 0; i < nbCases; i++) {
        reading >> maxShy;
        reading.ignore();
        getline(reading, line);
        writing << "Case #" << i+1 << ": " << nb_members(line, maxShy) << endl;
    }




    return 0;
}
