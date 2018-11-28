//
//  main.cpp
//  Deceitful War
//
//  Created by Tengqi Ye on 12/04/2014.
//  Copyright (c) 2014 Tengqi Ye. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <list>

int war(std::list<float> blocks1, std::list<float> blocks2);
int deceifulWar(std::list<float> blocks1, std::list<float> blocks2);

int main(int argc, const char * argv[])
{

    //open files
    std::ifstream in;
    std::ofstream out;
    
    in.open("D-large.in");
    out.open("D-large.out");
    
    
    //global variables
    int T, N;
    float block;
    std::list<float> blocks1, blocks2;
    
    //input & output
    in >> T;
    for( int i = 0; i < T; i ++ )
    {
        in >> N;
        for( int j = 0; j < N; j ++ )
        {
            in >> block;
            blocks1.push_back(block);
        }
        
        for( int j = 0; j < N; j ++ )
        {
            in >> block;
            blocks2.push_back(block);
        }
        
        //sort
        blocks1.sort();
        blocks2.sort();
        
        out << "Case #" << i + 1 << ": " << deceifulWar(blocks1, blocks2) << " " << war(blocks1, blocks2) << std::endl;
        
        
        //release
        blocks1.clear();
        blocks2.clear();
    }
    
    
    //close files
    in.close();
    out.close();
    
    
    return 0;
}


int war(std::list<float> blocks1, std::list<float> blocks2)
{
    int result = 0;
    
    while(!blocks1.empty())
    {
        if(blocks1.back() > blocks2.back())
        {
            result ++;
            blocks1.pop_back();
            blocks2.pop_front();
        }else
        {
            blocks1.pop_back();
            blocks2.pop_back();
        }
    }
    
    return result;
}


int deceifulWar(std::list<float> blocks1, std::list<float> blocks2)
{
    int result = 0;
    
    while(!blocks1.empty())
    {
        if(blocks1.front() < blocks2.front())
        {
            blocks1.pop_front();
            blocks2.pop_back();
        }else
        {
            result ++;
            blocks1.pop_front();
            blocks2.pop_front();
        }
    }
    
    return result;
}