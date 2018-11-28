//
//  main.cpp
//  The Repeater
//
//  Created by Tengqi Ye on 03/05/2014.
//  Copyright (c) 2014 Tengqi Ye. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

bool getOperationCount(std::string *words, int word_count, int &result_count);

std::string eraseRepeat(std::string word);//, int* sections, int &section_size);


int main(int argc, const char * argv[])
{

    //open files
    std::ifstream in;
    std::ofstream out;
    
    in.open("A-small-attempt2.in");
    out.open("A-small-attempt2.out");
    
    
    
    //global variables
    int T, N;
    std::string *words;
    
    
    
    //in & out
    in >> T;
    for(int case_index = 0; case_index < T; case_index ++)
    {
        in >> N;
        words = new std::string[N];
        
        for( int i = 0; i < N; i ++ )
        {
            in >> words[i];
        }
        
        int result;
        
        if( getOperationCount(words, N, result) )
        {
            out << "Case #" << case_index + 1 << ": " << result << std::endl;
        }else
        {
            out << "Case #" << case_index + 1 << ": Fegla Won" << std::endl;
        }
        
        
        
        
        
        //release
        delete [] words;
    }
    
    //close files
    out.close();
    in.close();
    
    return 0;
}



bool getOperationCount(std::string *words, int word_count, int &result_count)
{
    std::string abbrive = eraseRepeat(words[0]);
    
    for(int i = 1; i < word_count; i ++)
    {
        if( abbrive != eraseRepeat(words[i]))
        {
            return false;
        }
    }
    
    result_count = 0;
    
    int *section_front = new int [word_count], *section_length = new int [word_count];
    for(int i  = 0; i < word_count; i ++)
    {
        section_front[i] = section_length[i] = 0;
    }
    
    for(int i = 0; i < abbrive.length(); i ++)
    {
        for(int word_index = 0; word_index < word_count; word_index ++)
        {
            int c;
            
            for( c = section_front[word_index]; c < words[word_index].length(); c ++ )
            {
                if(words[word_index][c] != abbrive[i])
                {
                    section_length[word_index] = c - section_front[word_index];
                    section_front[word_index] = c;
                    break;
                }
            }
            if( c == words[word_index].length() )
            {
                section_length[word_index] = words[word_index].length() - section_front[word_index] + 1;
            }
        }
        
        result_count += abs(section_length[1] - section_length[0]);
    }
    
    return true;
}

std::string eraseRepeat(std::string word)//, int* sections, int &section_size)
{
    std::string result = word;
    
    int front = word.front();
    
    for( int i = 1; i < result.length(); i ++ )
    {
        if(front == result[i])
        {
            result.erase(result.begin() + i);
            i --;
        }else
        {
            front = result[i];
        }
    }
    
//    //get secitons front
//    section_size = result.length();
//    front = word.front();
//    int j = 0;
//    
//    for( int i = 1; i < word.length(); i ++ )
//    {
//        if(front != word[i])
//        {
//            sections[j] = i;
//            front = word[i];
//        }
//    }
    
//    std::cout << result << std::endl;
    
    return result;
}