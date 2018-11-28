

#include <stdlib.h>
#include <iostream>
#include <fstream>
using namespace std;

/*
 * 
 */
int maxHeightRow(int **lawn,int length,int y)
{
    int max = 0;
    for (int i = 0;i < length;i++)
    {
        if (lawn[y][i] > max) max = lawn[y][i];
    }
    return max;
}

int maxHeightCol(int **lawn,int x,int height)
{
    int max = 0;
    for (int i = 0;i < height;i++)
    {
        if (lawn[i][x] > max) max = lawn[i][x];
    }
    return max;
}

int main(int argc, char** argv) {
    
    ifstream myFile;
    ofstream outFile;

    int n;
    int l,h;
    
    myFile.open("B-large.in");
    //myFile.open("input.txt");
    outFile.open("output.txt");
    if (myFile.is_open())
    {
        myFile >> n;
        for (int q = 0;q < n;q++)
        {
            outFile << "Case #" << q+1 << ": ";

            myFile >> h;
            myFile >> l;
            int **lawn;
            lawn = new int *[h];
            for(int i = 0; i <h; i++)
                lawn[i] = new int[l];
            int possible[h][l];
            for (int y = 0;y<h;y++)
            {
                for (int x = 0;x<l;x++)
                {
                    myFile >> lawn[y][x];
                    possible[y][x] = 0;
                }
            }
            // Column checks
            int tallest = 0;
            for (int x = 0;x<l;x++)
            {
                tallest = maxHeightCol(lawn,x,h);
                for (int y = 0;y<h;y++)
                {
                    if (lawn[y][x] == tallest) possible[y][x] = 1;
                    
                }
            }
            // Row checks
            for (int y = 0;y<h;y++)
            {
                tallest = maxHeightRow(lawn,l,y);
                for (int x = 0;x<l;x++)
                {
                    if (lawn[y][x] == tallest) possible[y][x] = 1;
                }
            }
            // Final check to see if lawn is possible
            int good = 1;
            for (int y = 0;y<h;y++)
            {
                for (int x = 0;x<l;x++)
                {
                    //cout << possible[y][x];
                    if (possible[y][x] == 0)
                    {
                        good = 0;
                    }
                }
                //cout << endl;
                delete(lawn[y]);
            }
            delete(lawn);
            if (good == 1) outFile << "YES" << endl;
            else outFile << "NO" << endl;
        }
    }
    return (EXIT_SUCCESS);
}

