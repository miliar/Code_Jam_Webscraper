//
//  main.cpp
//  Magic Trick
//
//  Created by Tengqi Ye on 12/04/2014.
//  Copyright (c) 2014 Tengqi Ye. All rights reserved.
//

#include <iostream>
#include <fstream>


int compare(int* cards1, int* cards2, int cards_len);

int main(int argc, const char * argv[])
{


    //open files
    std::ifstream in;
    std::ofstream out;
    
    in.open("A-small-attempt0.in");
    out.open("A-small-attempt0.out");
    
    
    
    //global variables
    int T, answer1, answer2, var;
    int* cards1, *cards2;
    
    
    //in & out
    in >> T;
    for(int i = 0; i < T; i ++ )
    {
        //allocate
        cards1 = new int [4];
        cards2 = new int [4];
        
        in >> answer1;
        
        //read line according to answer1
        for(int row = 0; row < answer1 - 1; row ++)
        {
            for( int column = 0; column < 4; column ++ )
            {
                in >> var;
            }
        }
        
        for( int column = 0; column < 4; column ++ )
        {
            in >> cards1[column];
        }
        

        for(int row = answer1; row < 4; row ++)
        {
            for( int column = 0; column < 4; column ++ )
            {
                in >> var;
            }
        }
        
        
        in >> answer2;
        
        //read line according to answer2
        for(int row = 0; row < answer2 - 1; row ++)
        {
            for( int column = 0; column < 4; column ++ )
            {
                in >> var;
            }
        }
        
        for( int column = 0; column < 4; column ++ )
        {
            in >> cards2[column];
        }
        
        
        for(int row = answer2; row < 4; row ++)
        {
            for( int column = 0; column < 4; column ++ )
            {
                in >> var;
            }
        }
        
        
        //compare
        int result = compare(cards1, cards2, 4);
        out << "Case #" << i + 1 << ": ";
        
        if(result == -1)
        {
            out << "Volunteer cheated!" << std::endl;
        }else if (result == 0)
        {
            out << "Bad magician!" << std::endl;
        }else
        {
            out << result << std::endl;
        }
        
        //release cards
        delete [] cards2;
        delete [] cards1;
    }
    
    
    
    
    //close files
    in.close();
    out.close();
    
    
    return 0;
}



int compare(int* cards1, int* cards2, int cards_len)
{
    int result = -1;
    
    for( int i = 0; i < cards_len; i ++ )
    {
        for( int j = 0; j < cards_len; j ++ )
        {
            if( cards1[i] == cards2[j] )
            {
                if(result == -1)
                {
                    result = cards1[i];
                }else
                {
                    return 0;
                }
            }
        }
    }
    
    return result;
}

