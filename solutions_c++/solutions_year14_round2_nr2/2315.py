//
//  main.cpp
//  New Lottery Game
//
//  Created by Tengqi Ye on 03/05/2014.
//  Copyright (c) 2014 Tengqi Ye. All rights reserved.
//

#include <iostream>
#include <fstream>


long long getWinner(int A, int B, int K);


int main(int argc, const char * argv[])
{

    //open files
    std::ifstream in;
    std::ofstream out;
    
    in.open("B-small-attempt1.in");
    out.open("B-small-attempt1.out");
    
    
    
    //global variables
    int T, A, B, K;
    
    
    
    
    //in & out
    in >> T;
    for(int case_index = 0; case_index < T; case_index ++)
    {
        in >> A >> B >> K;
        
        out << "Case #" << case_index + 1 << ": " << getWinner(A, B, K) << std::endl;
    }
    
    //close files
    out.close();
    in.close();

    return 0;
}



long long getWinner(int A, int B, int K)
{
    int product;
    long long count = 0;
    for( int i = 0; i < A; i ++ )
    {
        for( int j = 0; j < B; j ++ )
        {
            product = i&j;
            if(product < K && i != j)
            {
                count ++;
//                std::cout << "i=" << i << ", j=" << j << std::endl;
            }
        }
        
    }
    
    for( int i = 0; i < A && i < B; i ++ )
    {
        product = i & i;
        if(product < K)
        {
            count ++;
//            std::cout << "i=" << i << ", j=" << i << std::endl;
        }
    }
    
    return count;
}