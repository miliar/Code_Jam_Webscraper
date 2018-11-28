//****************************************************************************/
// PROJECT      : Google Code Jam
//---------------------------------------------------------------------------
//
// INFORMATION  : Code snippets compiled together to assist in codejam problems.
// File         : FileIo.h
// Details      : Standard File Io calls I reuse.
// Copyright    : 
// Contributor  : BlindGarret
// Created      : 4/1/2016
/****************************************************************************/
#ifndef FILE_IO_HEADER
#define FILE_IO_HEADER

#include <vector>
#include <string>
#include <fstream>

std::vector<std::string> GetLines(std::string fileName);

template<typename V> void PrintLines(std::string fileName, V strings)
{
    std::ofstream myfile;
    myfile.open(fileName.c_str());
    for(auto string : strings)
    {
        myfile << string + "\n";        
    }
    myfile.close();
}

#endif