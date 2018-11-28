#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

int main()
{
    fstream file, output;
    file.open("A-small-attempt2.in", ios::in);
    output.open("Output.txt", ios::out);


    int cases;

    file>>cases;




    for(int c=0; c<cases; c++)
    {

    string line;
    stringstream shy;
    int maxshy, numperlevel, stood=0, needed=0;



    file>>maxshy;
    file>>line;

    for(int currentlevel=0; currentlevel<=maxshy; currentlevel++)
    {


        shy.clear();
        shy<<line[currentlevel];
        shy>>numperlevel;

        if(currentlevel<=stood || numperlevel==0)stood+=numperlevel;
        else
        {
            needed+=currentlevel-stood;
            stood+=needed+numperlevel;
        }
    }

    output<<"Case #"<<c+1<<": "<<needed<<endl;
    }

    file.close();
    output.close();

    return 0;
}
