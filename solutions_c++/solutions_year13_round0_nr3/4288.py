// main.cpp
//
//  Fair and Square
//
//     -- Google Code Jam -- Problem C
//
//  By: Victor Grzeda
//
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>


using namespace std;

void createList();


int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        cout << "Usage: \n" << argv[0] << "<input file>" << endl;
        return 1;
    }

    //Open input file
    ifstream listFile;
    ifstream inputFile;
    ofstream outputFile;
    inputFile.open(argv[1], ifstream::in);
    outputFile.open("results.out", ofstream::out);

    if ( !inputFile.is_open() ) {
        cout << "Could not open file" << endl;
        return 1;
    }

    //Variables
    int listCnt;

    int tests;
    int count = 1;
    unsigned long long int A;
    unsigned long long int loCnt;

    unsigned long long int B;
    unsigned long long int hiCnt;

    //createList();
    unsigned long long int list[87];

    listFile.open("proper.txt", ifstream::in);
    if ( !inputFile.is_open() ) {
        return 1;
    }
    listFile >> listCnt;
    for ( int i=0; i < listCnt; i++ )
    {
        listFile >> list[i];
    }
    listFile.close();


    //Open test File
    inputFile >> tests;

    cout << tests << endl;

    while( count <= tests )
    {
        //Grab interval A
        inputFile >> A;

        //Grab interval B
        inputFile >> B;

        cout << "[ " << A << " -- " << B << " ]" << endl;

        loCnt = hiCnt = 0;

        for( int i=0; i < listCnt; i++)
        {
            if( list[i] < A ) {
                loCnt++;
            }
            if( list[i] <= B ) {
                hiCnt++;
            }
        }

        cout << "Case #" << count << ": " << (hiCnt - loCnt) << endl;
        outputFile << "Case #" << count << ": " << (hiCnt - loCnt) << endl;

        count++;
    }

    inputFile.close();
    outputFile.close();


    return 0;
}

//Create Proper list
void createList()
{
    //Open input file
    ifstream inputFile;
    ofstream outputFile;
    inputFile.open("list.txt", ifstream::in);
    outputFile.open("proper.txt", ofstream::out);

    stringstream convert;
    string orig;
    int oSize;
    int oPos;
    string rev;

    int size;
    int count = 1;
    int num;

    unsigned long long int value;
    unsigned long long int root;

    inputFile >> size;

    while( count <= size )
    {
        inputFile >> num;
        inputFile >> value;

        root = sqrt( value );

        convert << root;

        orig = convert.str();

        oSize = orig.size();
        oPos = oSize - 1;
        rev = orig;
        for( unsigned int i=0; i < rev.size(); i++ )
        {
            rev.at(i) = orig.at(oPos);
            oPos--;
        }

        if ( orig.compare(rev) == 0 ) {
            outputFile << value << endl;
        }
        //outputFile << orig << " " << value << endl;

        convert.str(string());
        count++;
    }

    return;
}
/*
//Create Proper list
void createList()
{
    //Open input file
    ifstream inputFile;
    ofstream outputFile;
    inputFile.open("list.txt", ifstream::in);
    outputFile.open("proper.txt", ofstream::out);

    stringstream ss;
    string orig;

    int oSize;
    string rev;

    int size;
    int count = 1;
    int num;

    unsigned long long int value;
    unsigned long long int root;
    unsigned long long int Rroot;

    inputFile >> size;

    while( count <= size )
    {
        inputFile >> num;
        inputFile >> value;

        root = sqrt( value );

        ss << root;
        orig = ss.str();
        oSize = orig.size();
        rev = orig;


        int oPos = oSize - 1;
        for ( unsigned int i=0; i < rev.size(); i++ )
        {
            rev.at(i) = orig.at(oPos);
            oPos--;
        }

        Rroot = atoi(rev.c_str());

        cout << Rroot << " | " << root << endl;

        if ( Rroot == root ) {
            outputFile << root << " " << value << endl;
        }

        count++;
    }

    return;
}
*/
