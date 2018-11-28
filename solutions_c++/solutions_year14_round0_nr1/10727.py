#include <iostream>
#include <cstdlib>
#include <fstream>
using namespace std;

struct pairs
{
    int count;
    int answer;
};

 struct pairs magician_output(ifstream &file)
{
    int input1, input2, array1[4][4], array2[4][4];
    file >> input1;
    for (int i=0;i<4;i++)
    {
    for (int j=0; j<4; j++)
        {
            file >> array1[i][j];
        }
    }
    file >> input2;
    for (int i=0;i<4;i++)
    {
        for (int j=0; j<4; j++)
        {
            file >> array2[i][j];
        }
    }
    int counting = 0;
    int answering = 0;

    for (int i=0; i<4; i++)
    {
        for (int j=0; j<4; j++)
        {
            if (array1[input1 - 1][i] == array2[input2 - 1][j])
            {
                counting = counting + 1;
                answering = array1[input1 - 1][i];
            }
        }
    }
    struct pairs value;
    value.count = counting;
    value.answer = answering;
    return value;
}

int main()
{
    ifstream inFile;
    inFile.open("myinputsmagic.in", ios::in);
    int T;
    inFile >> T;
    int counts[T];
    int answers[T];
    for (int i=0; i < T; i++)
    {
        struct pairs value_new;
        value_new = magician_output(inFile);
        counts[i] = value_new.count;
        answers[i] = value_new.answer;
    }
    ofstream myfile;
    myfile.open ("example.txt", ios::out);

    for (int i=0; i < T; i++)
    {
        if (counts[i] == 0)
        {
            myfile << "Case #" << i+1 << ": ";
            myfile << "Volunteer Cheated!";
            myfile << "\n";
        }
        if (counts[i] == 1)
        {
            myfile << "Case #" << i+1 << ": ";
            myfile << answers[i];
            myfile << "\n";
        }
        if (counts[i] > 1)
        {
            myfile << "Case #" << i+1 << ": ";
            myfile << "Bad Magician!";
            myfile << "\n";
        }
    }
    myfile.close();
    inFile.close();
}



