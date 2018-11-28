#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("B-large.in", ios::in);
    if (!fin.is_open())
    {
        cerr << "Unable to open file 'B-large'" << endl;
        exit(10);
    }

    fout.open("B-large-answer.txt", ios::out);
    if(!fout.is_open())
    {
        cerr << "Unable to open file 'B-large-answer'" << endl;
        exit(10);
    }

    int T, numOfFlips;
    string stack;
    string::iterator iterStack;

    fin >> T;

    for (int i = 0; i < T; i++){
        fin >> stack;
        int arrayStackSize = stack.length();
        char arrayStack[arrayStackSize];
        iterStack = stack.begin();
        int arrayStackIndex = 0;

        for (iterStack; iterStack != stack.end(); iterStack++){
            arrayStack [arrayStackIndex] = *iterStack;
            arrayStackIndex++;
        }

        arrayStackIndex = 0;
        numOfFlips = 0;

        if (arrayStackSize == 1){
            if (arrayStack [arrayStackIndex] == '-'){
                arrayStack [arrayStackIndex] = '+';
                numOfFlips++;
            }
        }
        else{
            int arrayIter;
            char pancake;
            for (arrayStackIndex = 0; arrayStackIndex < arrayStackSize-1; arrayStackIndex++){
                if (arrayStack [arrayStackIndex] != arrayStack [arrayStackIndex+1]){
                    arrayIter = arrayStackIndex;
                    pancake = arrayStack [arrayStackIndex+1];
                    while (arrayIter != -1){
                        arrayStack [arrayIter] = pancake;
                        arrayIter--;
                    }
                    numOfFlips++;
                }
            }
            if (arrayStack [arrayStackIndex] == '-'){
                arrayIter = arrayStackIndex;
                while (arrayIter != -1){
                        arrayStack [arrayIter] = '+';
                        arrayIter--;
                    }
                numOfFlips++;
            }
        }

        //cout << "Case #" << i+1 << ": " << numOfFlips << endl;
        fout << "Case #" << i+1 << ": " << numOfFlips << endl;
    }

    fin.close();
    fout.close();

    return 0;
}

