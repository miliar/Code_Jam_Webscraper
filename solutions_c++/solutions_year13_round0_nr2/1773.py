#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <istream>
#include <ostream>
#include <sstream>

using namespace std;

int main()
{
    ifstream myfile("B-large.in");
    ofstream outputfile;
    outputfile.open("output.txt");

    int loops;
    int width;
    int length;
    int **array;

    int *rows;
    int *columns;

    bool result;

    myfile >> loops;

    for (int loop_number = 0; loop_number < loops; loop_number++)
    {
        myfile >> length >> width;

        array = new int*[length];

        for (int i = 0; i < length; i++)
            array[i] = new int[width];

        for (int i = 0; i < length; i++)
            for (int j = 0; j < width; j++)
                myfile >> array[i][j];

        rows = new int[length];
        columns = new int[width];

        for (int i = 0; i < length; i++)
            rows[i] = 0;
        for (int i = 0; i < width; i++)
            columns[i] = 0;
        for (int i = 0; i < length; i++)
            for (int j = 0; j < width; j++)
            {
                if (rows[i] <= array[i][j])
                    rows[i] = array[i][j];
                if (columns[j] <= array[i][j])
                    columns[j] = array[i][j];
            }

        result = true;
        for (int i = 0; i < length; i++)
            for (int j = 0; j < width; j++)
                if (array[i][j] < rows[i] && array[i][j] < columns[j])
                    result = false;

        if (result)
            outputfile << "Case #" << loop_number+1 << ": YES" << endl;
        else
            outputfile << "Case #" << loop_number+1 << ": NO" << endl;


//        for (int i = 0; i < length; i++)
//            cout << rows[i] << " ";
//        cout << endl;
//
//        for (int i = 0; i < width; i++)
//            cout << columns[i] << " ";
//        cout << endl << endl;

//        for (int i = 0; i < length; i++)
//        {
//            for (int j = 0; j < width; j++)
//                cout << array[i][j] << " ";
//            cout << endl;
//        }

//        cout << endl;

        delete [] array;
        delete [] rows;
        delete [] columns;
    }
    return 0;
}
