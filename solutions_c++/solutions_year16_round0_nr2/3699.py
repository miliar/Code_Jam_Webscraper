#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define RIGHT '+'
#define WRONG '-'

int main(int argc, const char * argv[])
{
    int T;
    string faces;

    ifstream input("C:/Users/Utente/Documents/Workspace/C/Revenge of the Pancakes/bin/Debug/input.in");
    ofstream output("C:/Users/Utente/Documents/Workspace/C/Revenge of the Pancakes/bin/Debug/output.txt");

    input >> T;

    for(int h = 0; h < T; h ++)
    {
        int changes = 0;
        input >> faces;

        for(int j = 0; j < faces.length() - 1; j++)
        {
            if(faces[j] != faces[j + 1])
            {
                changes++;
            }
        }
        if(faces[faces.length() -1] == WRONG)
        {
            changes++;
        }

        output << "Case #" << h + 1 << ": " << changes << endl;
        cout << "Case #" << h + 1 << ": " << changes << endl;
    }
}
