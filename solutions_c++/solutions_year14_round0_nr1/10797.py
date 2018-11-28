#include <iostream>
#include <stdio.h>
#include <math.h>
#include <fstream>
#include <sstream>
#include <stdlib.h>



using namespace std;

FILE *fp;
void Openfile(void);
int closeFile(void);

void openFile(){
  // fp = fopen("C:\\Users\\byron\\Documents\\4 Coding\\13 Code Jam\\1 Practice\\1 Reverse Words\\B-small-practice.in", "r");     //relies on file being saved on root
    std::ifstream file("C:\\Users\\byron\\Documents\\4 Coding\\13 Code Jam\\2014\\1CardTrick\\A-small-attempt1.in");
    string str;
    string numProblems, UserRowOne, UserRowTwo;
    ofstream outputfile;
    int cardMatrix [4][4];
    int magicRow [4] ,magicRow2 [4];
    int cardRow, cardCol, numCorrectCards, magicnumber;
    int numRows = 4; int numCols = 4;

    outputfile.open("C:\\Users\\byron\\Documents\\4 Coding\\13 Code Jam\\2014\\1CardTrick\\output.txt");

    getline(file, numProblems);
    int numProblemsInt = atoi(numProblems.c_str());
    //cout << "num Problems:" << numProblemsInt;

    for (int tries = 0; tries < numProblemsInt; tries ++){
        getline(file, UserRowOne);
        int rowOneInt = atoi(UserRowOne.c_str());
        //cout << "Row One:" << rowOneInt;

    //Read in first four rows of cards
        for (cardRow = 0; cardRow < numRows; cardRow++)
        {
            std::getline(file,str);
            std::istringstream iss(str);
            for (cardCol = 0; cardCol < numCols; cardCol ++)
            {
                if ((cardRow +1) == (rowOneInt)){
                    iss >> magicRow[cardCol];
                }
                else{
                    iss >> cardMatrix[cardRow][cardCol];
                }

            }
        }

        getline(file, UserRowTwo);
        int rowTwoInt = atoi(UserRowTwo.c_str());
        //cout << "Row Two:" << rowTwoInt;

    //Read in second four rows of cards
        for (cardRow = 0; cardRow < numRows; cardRow++)
        {
            std::getline(file,str);
            std::istringstream iss(str);
            for (cardCol = 0; cardCol < numCols; cardCol ++)
            {
                if ((cardRow +1) == (rowTwoInt)){
                    iss >> magicRow2[cardCol];
                }
                else{
                    iss >> cardMatrix[cardRow][cardCol];
                }
            }
        }

        //check to see if a match
        //0: Volunteer cheated
        //1: Show number
        //>: Bad Magician
        numCorrectCards = 0;
        magicnumber =0;
        for (int a = 0; a< 4; a++){
            for (int b = 0; b <4; b ++){
                if (magicRow[a] == magicRow2[b]){
                    numCorrectCards ++;
                    magicnumber = b;
                }
            }
        }
        cout << "Case #" << (tries+1) <<": ";
        outputfile << "Case #" << (tries+1) <<": ";

        if (numCorrectCards == 0){
            cout << "Volunteer cheated!";
            outputfile << "Volunteer cheated!";
        }
        if (numCorrectCards == 1){
            cout << magicRow2[magicnumber];
            outputfile << magicRow2[magicnumber];
        }
        else if (numCorrectCards > 1){
            cout << "Bad magician!";
            outputfile << "Bad magician!";
        }
        cout << "\n";
        outputfile << "\n";
    }



    outputfile.close();
    file.close();
}

int closeFile(){
    int closeValue;
    closeValue = fclose(fp);
    return closeValue;
}

void ReadLine()
{
    char tempChar;

    while ((tempChar = fgetc(fp))!= EOF ){

    }
}

int main()
{
    char x;
    char cardMatrix [0];
    int numCases;

    openFile();     //opens text file


    return 0;
}
