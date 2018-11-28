//
//  main.cpp
//  GoogleCodeJam2013_Lawnmower
//
//  Created by Surasak Sermluxananon on 4/13/56 BE.
//  Copyright (c) 2556 Surasak Sermluxananon. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <vector>
using namespace std;

typedef vector<int>      CVec;
typedef vector<CVec>     CLawnVec;
CLawnVec mLawn  = CLawnVec();

void createLawn(ifstream &input_file, int iRow, int iCol)
{
    mLawn.clear();
    for(int i = 0; i < iRow;++i)
    {
        CVec mColVec = CVec();
        string input_line;
        getline(input_file, input_line);
        stringstream sInput(input_line);
        for(int j = 0; j < iCol; ++j)
        {
            int iValue = 0;
            sInput.seekg(sInput.str().length() - j, ios::end);
            sInput >> iValue;
            mColVec.push_back(iValue);
        }
        
        if(!mColVec.empty())
        {
            mLawn.push_back(mColVec);
        }
    }
}

void findMinGrass(int &iMinGrass, int &iMinRow, int &iMinCol)
{
    for(int i = 0; i < mLawn.size();++i)
    {
        for(int j = 0; j < mLawn.at(0).size();++j)
        {
            int iValue = mLawn.at(i).at(j);
            //cout << "I : " << i << " J : " << j
            //     << " Value : " << iValue<< endl;
            if(iMinGrass > iValue)
            {
                //Find minimum possible grass height
                iMinGrass = iValue;
                iMinRow = i;
                iMinCol = j;
            }
        }
    }

}

int main(int argc, const char * argv[])
{
    string input_line;
    ifstream input_file;
    ofstream output_file;
    
    input_file.open (argv[1]);
    output_file.open(argv[2]);
    if (input_file.is_open())
    {
        int iCase = 0, iTotalCase = 0;
        while (input_file.good())
        {
            getline (input_file, input_line);
            if(iTotalCase == 0)
            {
                iTotalCase = atoi(input_line.c_str());
                iCase = iTotalCase;
            }
            else if(input_line != "")
            {
                int iRow = 0, iCol = 0;
                stringstream sInput(input_line);
                sInput >> iRow >> iCol;
                createLawn(input_file, iRow, iCol);
                
                bool bPossible = true;
                while(!mLawn.empty())
                {
                    int iMinRow = 0, iMinCol = 0, iMinGrass = 100;
                    int iRowCount = 0, iColCount = 0;
                    
                    findMinGrass(iMinGrass, iMinRow, iMinCol);

                    //Verify row that all of them should be equal to minimum grass height
                    for(int j = 0; j < mLawn.at(iMinRow).size();++j)
                    {
                        if(iMinGrass == mLawn.at(iMinRow).at(j))    { ++iRowCount; }
                    }
                    
                    //Verify column that all of them should be equal to minimum grass height
                    for(int i = 0; i < mLawn.size(); ++i)
                    {
                        if(iMinGrass == mLawn.at(i).at(iMinCol))    { ++iColCount; }
                    }
                    
                    if(iRowCount != mLawn.at(iMinRow).size() &&
                       iColCount != mLawn.size())
                    {
                        bPossible = false;
                        break;
                    }
                    else
                    {
                        //Remove verified row / column
                        if(iColCount == mLawn.size())
                        {
                            for(int i = 0; i < mLawn.size(); ++i)
                            {
                                mLawn.at(i).erase(mLawn.at(i).begin() + iMinCol);
                                if(mLawn.at(i).empty())
                                {
                                    mLawn.erase(mLawn.begin() + i);
                                }
                            }
                            continue;
                        }
                        else if(iRowCount == mLawn.at(iMinRow).size())
                        {
                            mLawn.erase(mLawn.begin() + iMinRow);
                            continue;
                        }
                    }

                }
                
                string sOutput = bPossible ? "YES" : "NO";
                --iCase;
                cout << "Case #" << iTotalCase - iCase << ": " << sOutput << endl;
                output_file << "Case #" << iTotalCase - iCase << ": " << sOutput << endl;
            }
        }
    }
    
    input_file.close();
    output_file.close();
    return 0;
}

